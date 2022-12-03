import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Truck } from '../../models/truck';


@Injectable({
  providedIn: 'root'
})
export class TruckService {

  private truckUrl = 'http://localhost:5000/api/v1/trucks';  // URL to REST API

  constructor(private http: HttpClient) { }

  /** GET users from the server */
  getTrucks(): Observable<Truck[]> {
    return this.http.get<Truck[]>(this.truckUrl + '/all-trucks');
  }
  
  /** GET user by id. Will 404 if id not found */
  getTruck(id: number): Observable<any> {
    const url = `${this.truckUrl}/get-truck/${id}`;
    return this.http.get<Truck>(url);
  }
  
  /** POST: add a new user to the server */
  addTruck(truck: Truck) {
    return this.http.post(this.truckUrl + '/add-truck', truck);
  }
  
  /** PUT: update the user on the server */
  updateTruck(id ,truck: Truck) {
    return this.http.put(this.truckUrl + `/update-truck/${id}`, truck);
  }
  
  /** DELETE: delete the user from the server */
  deleteTruck(id: number) {
    return this.http.delete(this.truckUrl + `/delete-truck/${id}`);
  }
  
}