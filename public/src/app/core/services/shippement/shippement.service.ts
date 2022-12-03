import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { find, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ShippementService {

    
  private _jsonURL = 'assets/data/data.json';
  constructor(private http: HttpClient) {
    this.get().subscribe((data) => data);
  }

  public get(): Observable<any> {
    return this.http.get("assets/data/data.json");
}

  public find(id: number) {
    return this.get().subscribe((data: any) => data.id == id);
  }
}

