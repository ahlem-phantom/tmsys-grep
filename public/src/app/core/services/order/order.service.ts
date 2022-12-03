import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Order } from '../../models/order';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class OrderService {

  private clientUrl = 'http://localhost:5000/api/v1/orders';  // URL to REST API

  constructor(private http: HttpClient) { }

  /** GET users from the server */
  getOrders(): Observable<Order[]> {
    return this.http.get<Order[]>(this.clientUrl + '/all-orders');
  }
  
  /** GET user by id. Will 404 if id not found */
  getOrder(id: number): Observable<any> {
    const url = `${this.clientUrl}/order/${id}`;
    return this.http.get<Order>(url);
  }
  
  /** POST: add a new user to the server */
  addOrder(order: Order) {
    return this.http.post(this.clientUrl + '/add-order', order);
  }
  
  /** PUT: update the user on the server */
  updateOrder(id ,order: Order) {
    return this.http.put(this.clientUrl + `/update-order/${id}`, order);
  }
  
  /** DELETE: delete the user from the server */
  deleteOrder(id: number) {
    return this.http.delete(this.clientUrl + `/delete-order/${id}`);
  }
  
}