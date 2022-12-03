import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { TmsLayoutRoutes } from './tms-layout-routing.module';
import { DashboardComponent } from './dashboard/dashboard.component';
import { TrackingComponent } from './tracking/tracking.component';
import { LoadComponent } from './load/load.component';
import { OrderComponent } from './order/order.component';
import { DriverComponent } from './driver/driver.component';
import { TruckComponent } from './truck/truck.component';
import { ClientComponent } from './client/client.component';
import { MapDetailsComponent } from './tracking/map-details/map-details.component';
import { MapComponent } from './tracking/map/map.component';
import { TruckDetailsComponent } from './truck/truck-details/truck-details.component';
import { TrackDetailsComponent } from './tracking/track-details/track-details.component';
import { ShippementsComponent } from './tracking/shippements/shippements.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatTableModule } from '@angular/material/table';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatSortModule } from '@angular/material/sort';
import { NgxPaginationModule } from 'ngx-pagination';
import { StringPipe } from '../../core/helpers/pipes/statepipe';
import { ShipmentComponent } from './shipment/shipment.component'

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forChild(TmsLayoutRoutes),
    FormsModule,
    ReactiveFormsModule,
    MatPaginatorModule,
    MatSortModule,
    MatTableModule,
    NgxPaginationModule,
  ],
  declarations: [
    DashboardComponent,
    TrackingComponent,
    LoadComponent,
    OrderComponent,
    DriverComponent,
    TruckComponent,
    ClientComponent,
    MapDetailsComponent,
    MapComponent,
    TruckDetailsComponent,
    TrackDetailsComponent,
    ShippementsComponent,
    StringPipe,
    ShipmentComponent
  ],
  exports : [
    MatPaginatorModule,
    MatSortModule
  ],
  schemas: [CUSTOM_ELEMENTS_SCHEMA]


})
export class TmsLayoutModule { }



