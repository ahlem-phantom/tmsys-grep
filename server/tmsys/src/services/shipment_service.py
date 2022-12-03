from pydoc import cli
from src.app import db
from src.models import Shipment, shipment
from src.models import Order as O
from src.models import Truck as T
from src.services.truck_service import get_length
from flask import jsonify, make_response
import math
from sklearn.cluster import KMeans
import numpy as np
from src.app import create_app
import os 
from apscheduler.schedulers.background import BackgroundScheduler

env_name = os.environ['FLASK_ENV']
app = create_app(env_name)

def updateShipmentTime():
    with app.app_context():
        times = Shipment.query.with_entities(Shipment.shipment_id,Shipment.shipment_time).all()
        for time in times :
            if (time.shipment_time == 7):
                shipment = Shipment.query.get(time.shipment_id)
                shipment.shipment_status = 'LATE'
                db.session.commit()
                print('Count: ',time.shipment_id,time.shipment_time)
sched = BackgroundScheduler(daemon=True)
sched.add_job(updateShipmentTime,'cron',second='30')
sched.start()

#Create Shipment
def create_shipment(body):
        truck_id = body['truck_id'];
        order_id = body['order_id'];
        shipment_seq = body['shipment_seq'];
        data = Shipment(order_id,truck_id,shipment_seq)
        db.session.add(data)
        db.session.commit()
        return jsonify({ 
            'status': True 
        })

# Constraints
MAX_DELIVERIES = 10 #capacity
DRIVE_SPEED_KMPH = 20 # max speed per hour for truck
PRICE_PER_TRUCK = 100
PRICE_PER_KM = 0.061
MAX_TIME_PER_TRUCK = 10  #driver working hours 


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


class Truck:
    id = 1

    def __init__(self):
        self.capacity_left = MAX_DELIVERIES
        self.x = 0
        self.y = 0
        self.current_time = 0 # truck starts at the beginning og the day 0h
        self.id = Truck.id
        self.deliveries = []  # [truck_id, order_id, seq_no]
        self.current_order = 1
        self.delivered = False
        Truck.id += 1
    
    def __repr__(self):
        return 'Truck { id : %s, capacity_left : %s, x : %s, y: %s, current_time : %s, deliveries : %s, current_order : %s, delivered : %s}' % (self.id, self.capacity_left, self.x, self.y, self.current_time, self.deliveries, self.current_order, self.delivered)

    def can_deliver_order(self, order):
        """
        Checks whether the truck can deliver the order and reach the depot in
        time.
        """
        if self.capacity_left == 0:
            return False

        time_to_reach_order = distance(
            self.x, self.y, order.x, order.y
        ) / DRIVE_SPEED_KMPH

        if self.current_time + time_to_reach_order >= order.end_time:
            return False

        time_to_reach_depot = distance(
            order.x, order.y, 0, 0
        ) / DRIVE_SPEED_KMPH

        if (
            max(self.current_time + time_to_reach_order, order.start_time)
                + time_to_reach_depot > MAX_TIME_PER_TRUCK
        ):
            return False

        #print("True")
        return True

    def deliver_order(self, order):
        dist = distance(self.x, self.y, order.x, order.y)

        # update current_time
        self.current_time = max(
            self.current_time + (dist / DRIVE_SPEED_KMPH),
            order.start_time
        )

        # update capacity
        self.capacity_left -= 1

        # update location
        self.x = order.x
        self.y = order.y

        # add order to deliveries
        self.deliveries.append([self.id, order.id, self.current_order])
        self.current_order += 1

    def deliver(self):
        self.delivered = True
        return self.deliveries[::]

    def has_delivered(self):
        return self.delivered


class Order:
    def __init__(self, id, x, y, start_time):
        self.id = id
        self.x = x
        self.y = y
        self.start_time = start_time
        self.end_time = self.start_time + 1


def clustered(orders, kmeans):
    clusters = {
        i: np.where(kmeans.labels_ == i)[0]
        for i in range(kmeans.n_clusters)
    }
    deliveries = []

    current_truck = Truck() # first value of truck  ==> initialisation
    # loop over each cluster
    for cluster in clusters.values():
        curr_len = len(deliveries)
        orders_in_cluster = [orders[idx] for idx in cluster]

        for order in sorted(orders_in_cluster, key=lambda x: x.end_time):
            """
            Checks whether the current_truck can deliver 
            the order and reach the depot in time.  
            """
            if current_truck.can_deliver_order(order):  
                current_truck.deliver_order(order)
            else:
                """
                Else check the next truck whether it can deliver 
                the order and reach the depot in time.
                
                1 - current_truck.deliver() ==> all deliveries for current_truck
                2 - deliveries ==> list of all trucks dliveries ==> la somme de current_truck.deliver()
                """
                deliveries.extend(current_truck.deliver()) 
                current_truck = Truck() # next truck id=id+1
                current_truck.deliver_order(order)

    if not current_truck.has_delivered():
        deliveries.extend(current_truck.deliver())

    return deliveries

## Assign Shipment
def assign_shipment():
    # Get Trucks 
    TOTAL_CLUSTERS = 55
    #TOTAL_CLUSTERS = int(T.query.filter_by(truck_status="Available").count())
    print(TOTAL_CLUSTERS)
    trucks = T.query.with_entities(T.truck_id).filter_by(truck_status="Available")
    truck_output = []
    for truck in trucks:
        truck_data = {}
        truck_data['truck_id'] = truck.truck_id
        truck_output.append(truck.truck_id)
    print(truck_output)

    # Get Orders
    orders = O.query.all()
    output = []
    orders_to_cluster = []
    orders_output = []
    for order in orders:
        order_data = {}
        order_data['order_id'] = order.order_id
        order_data['order_lat'] = order.order_lat
        order_data['order_lng'] = order.order_lng
        order_data['order_time_window'] = order.order_time_window
        output.append(order_data)
        orders_to_cluster.append([order_data['order_lat'],order_data['order_lng']])
        order_output = Order(order_data['order_id'], order_data['order_lat'],order_data['order_lng'],order_data['order_time_window'])
        orders_output.append(order_output)
    #print(output)
    #print(orders_to_cluster)
    #print(orders_output)


    kmeans = KMeans(n_clusters=TOTAL_CLUSTERS, random_state=0)
    kmeans.fit(orders_to_cluster)
    ans_list = clustered(orders_output, kmeans)
    #print(ans_list)
    order_list = []
    truck_list = []
    print("before",truck_list)

    for row in ans_list:
        truck_list.append(row[0])
    print("original",truck_list)
    '''
    j = 0
    #while (j < len(truck_list)) :
    if (truck_list[j] == truck_list[j+1]):
        truck_list[j] = truck_output[j]
        #j = j+1
    print("after",truck_list)
    '''

    for row in ans_list:
        order_data = {}
        order_data['truck_id'] = row[0]
        order_data['order_id'] = row[1]
        order_data['sequence_number'] = row[2]
        time = O.query.with_entities(O.order_time_window).filter_by(order_id=row[1]).first()
        data = Shipment(order_data['order_id'], order_data['truck_id'], order_data['sequence_number'], time.order_time_window)
        db.session.add(data)
        db.session.commit()
        order_list.append(order_data)
    #print(order_list)

    return jsonify({'shipments' : order_list, 'success' : True})


