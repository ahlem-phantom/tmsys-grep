import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { Location, LocationStrategy, PathLocationStrategy, PopStateEvent } from '@angular/common';
import { Router, NavigationEnd, NavigationStart } from '@angular/router';


@Component({
  selector: 'app-tms-layout',
  templateUrl: './tms-layout.component.html',
  styleUrls: ['./tms-layout.component.scss']
})
export class TmsLayoutComponent implements OnInit {

  constructor( public location: Location, private router: Router) {}

  ngOnInit() {
  
  }
  ngAfterViewInit() {
  }


}
