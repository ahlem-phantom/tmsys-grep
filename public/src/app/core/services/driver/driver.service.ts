import { Injectable } from '@angular/core';
import { Driver } from '../../models/driver';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DriverService {
  private driverUrl = 'http://localhost:5000/api/v1/drivers';  // URL to REST API

  constructor(private http: HttpClient) { }

 /** GET users from the server */
 getDrivers(): Observable<Driver[]> {
  return this.http.get<Driver[]>(this.driverUrl + '/all-drivers');
}

/** GET user by id. Will 404 if id not found */
getDriver(id: number): Observable<any> {
  const url = `${this.driverUrl}/get-driver/${id}`;
  return this.http.get<Driver>(url);
}

/** POST: add a new user to the server */
addDriver(driver: Driver) {
  return this.http.post(this.driverUrl + '/add-driver', driver);
}

/** PUT: update the user on the server */
updateDriver(id ,driver: Driver) {
  return this.http.put(this.driverUrl + `/update-driver/${id}`, driver);
}

/** DELETE: delete the user from the server */
deleteDriver(id: number) {
  return this.http.delete(this.driverUrl + `/delete-driver/${id}`);
}

}