import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AdminLayoutRoutes } from './admin-layout.routing';
import { AppsComponent } from './apps/apps.component';
import { InboxComponent } from './inbox/inbox.component';
import { ModulesComponent } from './modules/modules.component';


@NgModule({
  imports: [
    CommonModule,
    RouterModule.forChild(AdminLayoutRoutes),
    FormsModule,
    ReactiveFormsModule,
  ],
  declarations: [  
    InboxComponent,
    AppsComponent,
    ModulesComponent
  ],
  exports:[
  ]

})

export class AdminLayoutModule {}
