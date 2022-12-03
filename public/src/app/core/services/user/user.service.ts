import { Injectable } from '@angular/core';
import {Observable, throwError} from "rxjs";
import {HttpClient} from "@angular/common/http";
import {User} from "../../models/user";
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  url = "http://localhost:5000/data"
  constructor(private http: HttpClient) {}
  getAllUsers() : Observable<User[]> {
    return this.http.get<User[]>(this.url);
  }


  getAll() {
      return this.http.get<User[]>(`${environment.apiUrl}/users`);
  }

  getById(id: number) {
      return this.http.get<User>(`${environment.apiUrl}/users/${id}`);
  }
}
