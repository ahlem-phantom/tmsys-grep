enum state {
    "IN TRANSIT",
    "DELIVERED",
    "READY TO SHIP",
    "DRAFT",
    "idle timeout",
    "no connection"
}
export class Shipment {
shipement_id : number;
order_id : number; 
origin_city : string;
destination_city :string;
estimated_pickup : Date ;
estimated_delivery : Date ;
last_updated : Date ;
stock : number;
description : string;
volume : number;
width : number; 
height : number; 
length : number ;
net_weight : number ;
brut_weight : number;
distance : number ; 
shippement_status : state ;
} 