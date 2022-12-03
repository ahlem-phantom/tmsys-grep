import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Client } from '../../models/client';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class ClientService {

  private clientUrl = 'http://localhost:5000/api/v1/clients';  // URL to REST API

  constructor(private http: HttpClient) { }

  /** GET users from the server */
  getClients(): Observable<Client[]> {
    return this.http.get<Client[]>(this.clientUrl + '/all-clients');
  }
  
  /** GET user by id. Will 404 if id not found */
  getClient(id: number): Observable<any> {
    const url = `${this.clientUrl}/user/${id}`;
    return this.http.get<Client>(url);
  }
  
  /** POST: add a new user to the server */
  addClient(client: Client) {
    return this.http.post(this.clientUrl + '/add-client', client);
  }
  
  /** PUT: update the user on the server */
  updateClient(id ,client: Client) {
    return this.http.put(this.clientUrl + `/update-client/${id}`, client);
  }
  
  /** DELETE: delete the user from the server */
  deleteClient(id: number) {
    return this.http.delete(this.clientUrl + `/delete-client/${id}`);
  }
  
}