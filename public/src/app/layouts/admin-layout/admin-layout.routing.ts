import { Routes } from '@angular/router';
import { AdminLayoutComponent } from './admin-layout.component';
import { AppsComponent } from './apps/apps.component';
import { InboxComponent } from './inbox/inbox.component';
import { ModulesComponent } from './modules/modules.component';



export const AdminLayoutRoutes: Routes = [     
        {
         path: 'inbox',
         component: InboxComponent
        },
        {
          path: 'apps',
          component: AppsComponent
         },
         {
          path: 'modules',
          component: ModulesComponent
         }
];
