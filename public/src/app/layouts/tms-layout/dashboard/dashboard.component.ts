import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})

export class DashboardComponent implements OnInit {

  constructor() { }
  
  ngOnInit(): void {
    this.loadScript("assets/js/app.bundle.js");
    this.loadScript("assets/js/statistics/peity/peity.bundle.js");
    this.loadScript("assets/js/statistics/flot/flot.bundle.js");
    this.loadScript("assets/js/statistics/easypiechart/easypiechart.bundle.js");
    this.loadScript("assets/js/datagrid/datatables/datatables.bundle.js");
  }

  public loadScript(url) {
    let node = document.createElement('script');
    node.src = url;
    node.type = 'text/javascript';
    document.getElementsByTagName('head')[0].appendChild(node);
}

}
