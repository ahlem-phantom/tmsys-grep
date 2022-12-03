import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

declare const $: any;
declare interface RouteInfo {
    path: string;
    title: string;
    icon: string;
    class: string;
}
export const ROUTES: RouteInfo[] = [
    { path: '/app/inbox', title: 'Inbox',  icon: 'fas fa-envelope', class: '' },
    { path: '/app/apps', title: 'Apps',  icon:'fas fa-plus', class: '' },
    { path: '/app/modules', title: 'Modules',  icon:'fas fa-check', class: '' },
];

export const ROUTESTMS: RouteInfo[] = [
  { path: '/tms/dashboard', title: 'Dashboard',  icon: 'fas fa-chart-pie', class: '' },
  { path: '/tms/tracking', title: 'Tracking',  icon: 'fas fa-map-marker-alt', class: '' },
  { path: '/tms/load', title: 'Load Management',  icon: 'fas fa-box-check', class: '' },
  { path: '/tms/order', title: 'Order Management',  icon: 'fas fa-file-alt', class: '' },
  { path: '/tms/driver', title: 'Driver Management',  icon: 'fas fa-id-card', class: '' },
  { path: '/tms/truck', title: 'Truck Management',  icon: 'fas fa-truck', class: '' },
  { path: '/tms/client', title: 'Client Management',  icon: 'fas fa-user-alt', class: '' },

];

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit {

  menuItems: any[];
  menuItemsTMS: any[];

  constructor(public router: Router) { }

  ngOnInit() {
    this.menuItems = ROUTES.filter(menuItem => menuItem);
    this.menuItemsTMS = ROUTESTMS.filter(menuItem => menuItem);

  }

  isMobileMenu() {
      if ($(window).width() > 991) {
          return false;
      }
      return true;
  };
}
