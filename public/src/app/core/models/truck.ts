enum state {
    "ON",
    "OFF"
  }

export class Truck {
    truck_id : number;
    driver_id : number;
    load_id : number ;
    truck_name : string;
    truck_plate : string;
    truck_year : number; 
    truck_model : string; 
    truck_type : string;
    truck_capacity : number;
    truck_size : number;
    truck_engine : string;
    truck_color : string; 
    truck_status : state; 
    isfull : boolean; 
} 