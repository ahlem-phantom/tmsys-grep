import { Component, OnInit } from '@angular/core';
import { Apps } from 'src/app/core/models/apps';
import { AppsService } from 'src/app/core/services/apps/apps.service';
@Component({
  selector: 'app-apps',
  templateUrl: './apps.component.html',
  styleUrls: ['./apps.component.css']
})
export class AppsComponent implements OnInit {
  app: Apps;


  constructor( private appService: AppsService ) { }

  ngOnInit(): void {
  }

  addToModules(app: Apps) {
    this.appService.addToApp(app);
    window.alert('Your app has been downloaded successfully!');
  }

}
