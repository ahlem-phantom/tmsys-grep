import { Injectable } from '@angular/core';
import { Apps } from '../../models/apps';
@Injectable({
  providedIn: 'root'
})
export class AppsService {
  apps: Apps[] = [];

  constructor() { }
  addToApp(app : Apps) {
    this.apps.push(app);
  }

  getApps() {
    return this.apps;
  }

  clearApps() {
    this.apps = [];
    return this.apps;
  }
}
