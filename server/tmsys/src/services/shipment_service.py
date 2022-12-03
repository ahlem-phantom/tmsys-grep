from pydoc import cli
from src.app import db
from src.models import Shipment
from src.models import Order as O
from flask import jsonify, make_response
import math
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import csv
import os
#Create Shipment
def create_shipment(body):
        truck_id = body['truck_id'];
        order_id = body['order_id'];
        shipment_code = body['shipment_code'];
        data = Shipment(order_id,truck_id,shipment_code)
        db.session.add(data)
        db.session.commit()
        return jsonify({ 
            'status': True 
        })

#Assign Shipment
MAX_DELIVERIES = 10
DRIVE_SPEED_KMPH = 20
PRICE_PER_TRUCK = 100
PRICE_PER_KM = 0.061
MAX_TIME_PER_TRUCK = 10

TOTAL_CLUSTERS = 20


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


class Truck:
    id = 0

    def __init__(self):
        self.capacity_left = MAX_DELIVERIES
        self.x = 0
        self.y = 0
        self.current_time = 0
        self.id = Truck.id
        self.deliveries = []  # [truck_id, order_id, seq_no]
        self.current_order = 1
        self.delivered = False
        Truck.id += 1

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


def bruteforce(orders):
    deliveries = []
    current_truck = Truck()

    while orders:
        top = orders.pop()
        if current_truck.can_deliver_order(top):
            current_truck.deliver_order(top)
        else:
            deliveries.extend(current_truck.deliveries[::])
            current_truck = Truck()
            current_truck.deliver_order(top)

    if len(deliveries) < 500:
        deliveries.extend(current_truck.deliveries[::])

    return deliveries


def clustered(orders, kmeans):
    clusters = {
        i: np.where(kmeans.labels_ == i)[0]
        for i in range(kmeans.n_clusters)
    }
    deliveries = []

    current_truck = Truck()

    # loop over each cluster
    for cluster in clusters.values():
        curr_len = len(deliveries)

        orders_in_cluster = [orders[idx] for idx in cluster]

        for order in sorted(orders_in_cluster, key=lambda x: x.end_time):
            if current_truck.can_deliver_order(order):
                current_truck.deliver_order(order)
            else:
                deliveries.extend(current_truck.deliver())
                current_truck = Truck()
                current_truck.deliver_order(order)

    if not current_truck.has_delivered():
        deliveries.extend(current_truck.deliver())

    return deliveries

def assign_shipment():
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
    print(output)
    print(orders_to_cluster)
    print(orders_output)


    kmeans = KMeans(n_clusters=TOTAL_CLUSTERS, random_state=0)
    kmeans.fit(orders_to_cluster)

    # ans_list = bruteforce(orders)
    ans_list = clustered(orders_output, kmeans)
    #print(ans_list)
    order_list = []
    for row in ans_list:
        order_data = {}
        order_data['truck_id'] = row[0]
        order_data['order_id'] = row[1]
        order_data['sequence_number'] = row[2]
        order_list.append(order_data)
    print(order_list)
    return jsonify({'shipments' : order_list, 'success' : True})
