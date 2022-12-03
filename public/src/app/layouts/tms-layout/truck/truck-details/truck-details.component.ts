import { Component, OnDestroy, OnInit } from '@angular/core';
import * as Leaflet from 'leaflet';
import 'leaflet-routing-machine';
import * as _ from 'lodash';
declare let L;
import * as modal from 'leaflet-modal';
import { TruckService } from 'src/app/core/services/truck/truck.service';
import { Truck } from 'src/app/core/models/truck';
import { ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup } from '@angular/forms';

const locator =  new Leaflet.Icon({
  iconUrl: 'assets/img/locator.png',
  iconSize: [60, 60],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41] 
});

const routing = new Leaflet.Icon({
  iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
});

@Component({
  selector: 'app-truck-details',
  templateUrl: './truck-details.component.html',
  styleUrls: ['./truck-details.component.css']
})
export class TruckDetailsComponent implements OnInit,OnDestroy{
  map: Leaflet.Map;
  map_trip: Leaflet.Map;
  map_test: Leaflet.Map;
  truck: Truck;
  hide : any;
  editForm: FormGroup;
  tripForm: FormGroup;
  distance: any;
  tripH: any;
  tripMin: any;
  tripDuration :any ;
  inputs : any;

  constructor(private fb: FormBuilder, private truckService: TruckService, private route:ActivatedRoute) { }

  ngOnInit(): void {
    /** Map 1 **/

    this.map = Leaflet.map('map').setView([36.7859, 10], 10);
    Leaflet.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    }).addTo(this.map);
    Leaflet.marker([ 36.7859, 10 ], {icon: locator}).addTo(this.map)

    this.editForm = this.fb.group({
      name : [''],
      plate : [''],
      year : [''],
      model : [''],
      capacity: [''],
      size : [''],
      engine: [''],
      color :[''],
      type : [''],
      status : [''] 
     });
     
     this.tripForm = this.fb.group({
      from : [''],
      to : [''],
      year : [''],
      date : [''],
      driver: [''],
      distance : [''],
      duration: [''],
     });

    /*this.map_test = Leaflet.map('map-test').setView([36.7859, 10], 10);
    Leaflet.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    }).addTo(this.map_test);
    Leaflet.marker([ 36.7859, 10 ], {icon: locator}).addTo(this.map_test);
    this.map_test.on('shown.bs.modal',  () => {
          this.map_test.invalidateSize(true)
    });*/
    this.getTruck(this.route.snapshot.paramMap.get('id'))
    console.log("ok"+this.route.snapshot.paramMap.get('id'))
  }

  

  getTruck(id): void {
		this.truckService.getTruck(id).subscribe(truck=> { this.truck = truck['truck']; console.log(this.truck)});
	}

   planTrip (){
   
    setTimeout(()  => { 
          this.tripForm.patchValue({
            from : "Hjalmar Brantingsgatan"
        });
      }, 1000 );
     
      setTimeout(()  => { 
        this.tripForm.patchValue({
          to : "Linnégatan"
      });
    }, 2000 );

    setTimeout(()  => { 
      this.tripForm.patchValue({
        date : "2022-08-31"
    });
  }, 3000 );

  setTimeout(()  => { 
    this.tripForm.patchValue({
      driver : "flen ben foulen"
  });
}, 4000 );

setTimeout( () => {
  this.map_trip = Leaflet.map('map-trip').setView([57.69, 11.9], 10);
  Leaflet.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  }).addTo(this.map_trip);      
  Leaflet.marker([ 57.74, 11.94], {icon: routing}).addTo(this.map_trip)
  Leaflet.marker([ 57.6792, 11.949], {icon: routing}).addTo(this.map_trip)
  }, 5000)

    setTimeout(() => {
      this.hide = 'show'
      $('#map-trip').hide();
      },7000);
    /** Map 2 **/
    setTimeout( () => {
      this.hide = 'hide'
      $('#map-trip').show();
    var routeControl = L.Routing.control({
      waypoints: [
        L.latLng(57.74, 11.94),
        L.latLng(57.6792, 11.949)
      ],
      createMarker: function (i: number, waypoint: any, n: number) {
        const marker = L.marker(waypoint.latLng, {
          draggable: true,
          bounceOnAdd: false,
          bounceOnAddOptions: {
            duration: 1000,
            height: 800,
          },
          icon: routing 
        });
        return marker;
      }
    }).addTo(this.map_trip);
    
    routeControl.on('routesfound', (e) =>  {
      var routes = e.routes;
      var summary = routes[0].summary;
      console.log(routes[0])
      this.distance = (summary.totalDistance/ 1000).toFixed(2) + " km"
      this.tripDuration =  Math.floor(summary.totalTime/ 3600)+ " h " + Math.round(summary.totalTime % 3600 / 60) + " min "
      // alert time and distance in km and minutes
      alert('Total distance is ' + summary.totalDistance / 1000 + ' km ' + Math.round(summary.totalTime % 3600 / 60) + 'min ' + summary.totalTime);
    });
    
    }, 10000)

    /** Map 3 **/ 
   




  }

  

    ngOnDestroy(): void {
    this.map.remove();
    this.map_trip.remove();
  }


  

}
