enum OrderStatus {
    "CREATED",
    "SHIPPING",
    "DELIVERD",
    "CANCELED",
  }

  enum item {
    "CARTON",
    "CUBE",
    "BOX"
  }
// CREATE, SHIPPEMENT, DELIVERED, PAID
export class Order {
    order_id : number ;
    client_id : number ;
    order_address : string;
    order_reference : string;
    order_date : string;
    order_code: string;
    order_ht : string;
    order_tva : string;
    order_ttc : string;
    order_lng : number ;
    order_lat : number ;
    order_status : OrderStatus; 
} 