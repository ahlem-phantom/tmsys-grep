import { Component, OnDestroy, OnInit, ElementRef } from '@angular/core';
import * as Leaflet from 'leaflet';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
// @ts-ignore
import { HttpClient } from "@angular/common/http";
import { ShipmentService } from 'src/app/core/services/shipment/shipment.service';
import { OrderService } from 'src/app/core/services/order/order.service';
import { Shipment, shipmentState } from 'src/app/core/models/shipment';
import { StringPipe } from 'src/app/core/helpers/pipes/statepipe';

const myIconGreen =  new Leaflet.Icon({
  iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
});

const myIconBlue=  new Leaflet.Icon({
  iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-blue.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
});

const myIconRed=  new Leaflet.Icon({
  iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
});

const myIconOrange=  new Leaflet.Icon({
  iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-orange.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
});

const myIconYellow=  new Leaflet.Icon({
  iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-yellow.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
});
@Component({
  selector: 'app-shipment',
  templateUrl: './shipment.component.html',
  styleUrls: ['./shipment.component.css']
})
export class ShipmentComponent implements OnInit, OnDestroy {
  title = 'leafletApps';
  map: Leaflet.Map;
  shippments: any = [];
  color : any;
  pos : Leaflet.LatLng ;
  hide :boolean = false;
  search : any ;
  shipments : Shipment[] = [];
  page: number = 1;
  count: number = 0;
  listSize: number = 7;
  listsSizes: any = [3, 6, 9, 12];

  constructor(private httpClient: HttpClient, private router: Router,private elementRef: ElementRef, private shipmentService: ShipmentService) { 
  }

  ngOnInit(): void {
    this.map = Leaflet.map('map-shipment').setView([34.079, 9.701], 7);
    Leaflet.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    }).addTo(this.map);
    this.getShipments();


 
  }

  getShipments(): void {
		this.shipmentService.getShipments().subscribe(shipments => { 
      this.shipments = shipments['shipments'];
      console.log(this.shipments)
      for (let i = 0; i < this.shipments.length; i++) {
        console.log(this.shipments[i]['shipment_id'])
        this.pos = new (Leaflet.latLng as any)(this.shipments[i]['order']['order_lat'],this.shipments[i]['order']['order_lng']);
        Leaflet.marker([ this.shipments[i]['order']['order_lat'], this.shipments[i]['order']['order_lng'] ], {icon: this.getIcon(this.shipments[i]['shipment_status'])}).addTo(this.map)
        .bindPopup(`<b>Longtitude :</b>${this.shipments[i]['order']['order_lng']}  <br/> <br/>
                    <b> Latitude </b> ${this.shipments[i]['order']['order_lat']} <br/> <br/>
                    <div style="text-align:center;">
                    <button type="button" class="edit btn btn-outline-secondary btn-pills waves-effect waves-themed" >View Tracking</button>
                    </div>
                    
                  `).on("popupopen", () => {
                    this.elementRef.nativeElement
                      .querySelector(".edit")
                      .addEventListener("click", e => {
                        this.editArtwork(this.shipments[i]['shipment_id']);
                      });
                  })
        .on('click', () => {
          this.map.flyTo([this.shipments[i]['order']['order_lat'], this.shipments[i]['order']['order_lng']],11);
          });

      }

    });
	}

  colorStatus(status : any){
    if (status === shipmentState.ON_ROUTE){
      this.color = 'green';
    } 
    else if (status === shipmentState.LATE ){
      this.color = 'red';
    }  
    else {
      this.color = 'black';
    }  
  }

  getColor (status : any){
    if(status==shipmentState.ON_ROUTE)
      return "green";
    else if(status==shipmentState.LOADING)
      return "blue";
    else if(status==shipmentState.UNLOADING)
      return "yellow";
    else if(status==shipmentState.LATE)
      return "red";
    else if(status==shipmentState.STOPPED)
      return "orange";
    else if(status==shipmentState.READY_TO_SHIP)
      return "green";
    else 
      return "black";
  }
  markerIcon = {
    icon: Leaflet.icon({
      iconSize: [25, 41],
      iconAnchor: [10, 41],
      popupAnchor: [2, -40],
      // specify the path here
      iconUrl: "https://unpkg.com/leaflet@1.4.0/dist/images/marker-icon.png",
      shadowUrl: "https://unpkg.com/leaflet@1.4.0/dist/images/marker-shadow.png"
    })
  };
  getIcon(status : any){
    if(status==shipmentState.READY_TO_SHIP)
      return myIconGreen;
    else if(status==shipmentState.ON_ROUTE)
      return myIconGreen;
    else if(status==shipmentState.LOADING)
      return myIconBlue;
    else if(status==shipmentState.UNLOADING)
      return myIconYellow;
    else if(status==shipmentState.LATE)
      return myIconRed;
      else if(status==shipmentState.STOPPED)
      return myIconOrange;
    else  
    return myIconRed;
  }

  getUserIdsFirstWay($event) {
    let i = Number((<HTMLInputElement>document.getElementById('userIdFirstWay')).value);
    i = Number(i)-1;
    this.map.flyTo([this.shipments[i]['order']['order_lat'], this.shipments[i]['order']['order_lng']],14);
  }  
  myfunc() {
    this.router.navigate(['/tms/track-details',this.shippments.id])
  }

  editArtwork(id : any) {
    console.log(id)
    this.router.navigate(['/tms/track-details',id])
  }

  onListDataChange(event: any) {
    this.page = event;
    this.getShipments();
  }
  onListSizeChange(event: any): void {
    this.listSize = event.target.value;
    this.page = 1;
    this.getShipments();
  }


  ngOnDestroy(): void {
    this.map.remove();
  }

}

