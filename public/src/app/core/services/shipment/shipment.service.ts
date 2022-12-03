import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable} from 'rxjs';
import { Shipment } from '../../models/shipment';

@Injectable({
  providedIn: 'root'
})
export class ShipmentService {
  private shipmentUrl = 'http://localhost:5000/api/v1/shipments';  // URL to REST API

  constructor(private http: HttpClient) { }

  /** GET users from the server */
  getShipments(): Observable<Shipment[]> {
    return this.http.get<Shipment[]>(this.shipmentUrl + '/get-shipments');
  }
  
  /** GET user by id. Will 404 if id not found */
  getShipment(id: number): Observable<any> {
    const url = `${this.shipmentUrl}/get-shipment/${id}`;
    return this.http.get<Shipment>(url);
  }
  
  
  
}