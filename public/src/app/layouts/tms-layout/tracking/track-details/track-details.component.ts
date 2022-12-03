import { Component, OnDestroy, OnInit } from '@angular/core';
import  'leaflet';
import { HttpClient } from '@angular/common/http';
import 'leaflet-routing-machine';
import { icon, Icon } from 'leaflet';
import { ShippementService } from 'src/app/core/services/shippement/shippement.service';
import { find } from 'rxjs';
declare let L;

@Component({
  selector: 'app-track-details',
  templateUrl: './track-details.component.html',
  styleUrls: ['./track-details.component.css']
})
export class TrackDetailsComponent implements OnInit,OnDestroy {
  map: L.Map;
  progress : any ;
  orders : any;
  shippments: any = [];

  private truckIcon: Icon = icon({
    iconUrl: 'assets/img/svg/truck.svg',
    iconSize: [50, 51], // => random values you have to choose right ones for your case
  });

  constructor(private httpClient: HttpClient, private shippementService :  ShippementService) { }

  ngOnInit(): void {
    this.shippementService.get().subscribe(data => {
      item => item.id === 2
  });
    this.shippementService.get().subscribe(
      find((data :any) => 
        data.id == 5
      ));
    this.map = L.map('map-d').setView([34.079, 9.701], 9);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    }).addTo(this.map);
    
    this.httpClient.get("https://nominatim.openstreetmap.org/search?format=json&limit=3&q=" + "ariana ghazela").subscribe(
      data =>{
        console.log(data[0]['boundingbox'][0],data[1]['boundingbox'][1]);
      });
    
      var router = L.Routing.control({
        waypoints: [
            L.latLng(57.74, 11.94),
            L.latLng(57.6792, 11.949)
        ],
        lineOptions: {
          styles: [{ color: 'blue', opacity: 1, weight: 5 }]
        },
        routeWhileDragging: true,
        reverseWaypoints: true,
        showAlternatives: true,
        createMarker: function (i: number, waypoint: any, n: number) {
          const marker = L.marker(waypoint.latLng, {
            draggable: true,
            bounceOnAdd: false,
            bounceOnAddOptions: {
              duration: 1000,
              height: 800,
            },
            icon: L.icon({
              iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
              shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
              iconSize: [25, 41],
              iconAnchor: [12, 41],
              popupAnchor: [1, -34],
              shadowSize: [41, 41]
            })
          });
          return marker;
        }
      }).addTo(this.map);
      L.marker([ "57.72","11.945" ], {icon: this.truckIcon}).addTo(this.map).bindPopup("This is the Transamerica Pyramid");

   //   router ;
   /*var arrayOfPoints = router.getLatLngs();
   console.log(arrayOfPoints);*/

      
  }

  shipStatus(orders){
   return this.progress= 100 /orders;
   
  }

  ngOnDestroy(): void {
    this.map.remove();
  }


}
