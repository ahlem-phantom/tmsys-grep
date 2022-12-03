import { Component, OnDestroy, OnInit, ElementRef } from '@angular/core';
import * as Leaflet from 'leaflet';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
// @ts-ignore
import { HttpClient } from "@angular/common/http";

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
  selector: 'app-tracking',
  templateUrl: './tracking.component.html',
  styleUrls: ['./tracking.component.css']
})
export class TrackingComponent implements OnInit, OnDestroy  {
  title = 'leafletApps';
  map: Leaflet.Map;
  shippments: any = [];
  color : any;
  pos : Leaflet.LatLng ;
  hide :boolean = false;
  search : any ;
  constructor(private httpClient: HttpClient, private router: Router,private elementRef: ElementRef) { 
  }

  ngOnInit(): void {
    
    this.map = Leaflet.map('map').setView([34.079, 9.701], 7);
    Leaflet.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    }).addTo(this.map);

    this.httpClient.get("assets/data/data.json").subscribe(
      data =>{
      console.log(data);
      this.shippments = data;
      for (let i = 0; i < this.shippments.length; i++) {
        this.pos = new (Leaflet.latLng as any)(this.shippments[i]['lat'], this.shippments[i]['long']);
        Leaflet.marker([ this.shippments[i]['lat'], this.shippments[i]['long'] ], {icon: this.getIcon(this.shippments[i]['status'])}).addTo(this.map)
        .bindPopup(`<b>Longtitude :</b>${this.shippments[i]['long']}  <br/> <br/>
                    <b> Latitude </b> ${this.shippments[i]['lat']} <br/> <br/>
                    <div style="text-align:center;">
                    <button type="button" class="edit btn btn-outline-secondary btn-pills waves-effect waves-themed" >View Tracking</button>
                    </div>
                    
                  `).on("popupopen", () => {
                    this.elementRef.nativeElement
                      .querySelector(".edit")
                      .addEventListener("click", e => {
                        this.editArtwork(this.shippments[i]['id']);
                      });
                  })
        .on('click', () => {
          this.map.flyTo([this.shippments[i]['lat'], this.shippments[i]['long']],11);
          });
        }
        
        
    })
 


    // Leaflet.marker([36.5607, 10.2629], {icon: myIconYellow}).addTo(this.map).bindPopup('Ben Arous').openPopup();
   //  antPath([[28.644800, 77.216721], [34.1526, 77.5771]],
    //  { color: '#FF0000', weight: 5, opacity: 0.6 })
     // .addTo(this.map);
  }

  colorStatus(status : any){
    if (status === 'On route' ){
      this.color = 'green';
    } 
    else  if (status === 'Late' ){
      this.color = 'red';
    }  
    else {
      this.color = 'black';
    }  
  }

  getColor (status : any){
    if(status=='On route')
      return "green";
    else if(status=='Loading')
      return "blue";
    else if(status=='Unloading')
      return "yellow";
    else if(status=='Late')
      return "red";
      else if(status=='Stopped')
      return "orange";
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
  getIcon (status : any){
    if(status=='On route')
      return myIconGreen;
    else if(status=='Loading')
      return myIconBlue;
    else if(status=='Unloading')
      return myIconYellow;
    else if(status=='Late')
      return myIconRed;
      else if(status=='Stopped')
      return myIconOrange;
    else  
    return myIconRed;
  }

  getUserIdsFirstWay($event) {
    let i = Number((<HTMLInputElement>document.getElementById('userIdFirstWay')).value);
    i = Number(i)-1;
    this.map.flyTo([this.shippments[i]['lat'], this.shippments[i]['long']],14);
  }  
  myfunc() {
    this.router.navigate(['/tms/track-details',this.shippments.id])
  }

  editArtwork(id : any) {
    console.log(id)
    this.router.navigate(['/tms/track-details',id])
  }


  ngOnDestroy(): void {
    this.map.remove();
  }

}

