import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ClientComponent } from './client/client.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { DriverComponent } from './driver/driver.component';
import { LoadComponent } from './load/load.component';
import { OrderComponent } from './order/order.component';
import { TrackDetailsComponent } from './tracking/track-details/track-details.component';
import { TrackingComponent } from './tracking/tracking.component';
import { TruckComponent } from './truck/truck.component';
import { TruckDetailsComponent } from './truck/truck-details/truck-details.component';
export const TmsLayoutRoutes: Routes = [  
  {
    path: 'dashboard',
    component: DashboardComponent
   },
   {
     path: 'tracking',
     component: TrackingComponent,
    },
    {
      path: 'track-details/:id', // child route path
      component: TrackDetailsComponent, // child route component that the router renders
    },
    {
     path: 'load',
     component: LoadComponent
    },
    {
     path: 'order',
     component: OrderComponent
    },
    {
     path: 'driver',
     component: DriverComponent
    },
    {
     path: 'truck',
     component: TruckComponent
    },
    {
      path: 'truck-details/:id', // child route path
      component: TruckDetailsComponent, // child route component that the router renders
    },
    {
     path: 'client',
     component: ClientComponent
    }
];

