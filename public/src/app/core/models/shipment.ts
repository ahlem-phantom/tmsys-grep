import { Order } from 'src/app/core/models/order';
import { Driver } from 'src/app/core/models/driver';
import { Truck } from 'src/app/core/models/truck';

export enum shipmentState {
  READY_TO_SHIP = "\"READY_TO_SHIP\"",
  ON_ROUTE = "\"ON_ROUTE\"",
  LOADING = "\"LOADING\"",
  UNLOADING = "\"UNLOADING\"",
  LATE = "\"LATE\"",
  STOPPED = "\"STOPPED\"",
  NO_CONNECTION = "\"NO_CONNECTION\""
}

export class Shipment {
  shipment_id: number;
  order_id: number;
  created_at: Date;
  shipment_status: shipmentState;
  shipment_code: string;
  order: Order;
  driver: Driver;
  truck: Truck;
}
