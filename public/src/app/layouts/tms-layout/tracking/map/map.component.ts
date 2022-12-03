import { Component, OnDestroy, OnInit } from '@angular/core';
import * as Leaflet from 'leaflet';
@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit, OnDestroy {
  map: Leaflet.Map;

  constructor() { }

  ngOnInit(): void {
    this.map = Leaflet.map('map').setView([34.079, 9.701], 9);
    Leaflet.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    }).addTo(this.map);
  }

    ngOnDestroy(): void {
    this.map.remove();
  }

}
