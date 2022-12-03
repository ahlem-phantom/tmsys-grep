import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule } from '@angular/router';
import { AppRoutingModule } from './app.routing';
import { AppComponent } from './app.component';
import { AdminLayoutComponent } from './layouts/admin-layout/admin-layout.component';
import { AuthLayoutComponent } from './layouts/auth-layout/auth-layout.component';
import { UsersComponent } from './components/users/users.component';
import { FooterComponent } from './shared/components/footer/footer.component';
import { SidebarComponent } from './shared/components/sidebar/sidebar.component';
import { NavbarComponent } from './shared/components/navbar/navbar.component';
import { HeaderComponent } from './shared/components/header/header.component';
import { MenuComponent } from './shared/components/menu/menu.component';
import { InterfaceSettingsComponent } from './shared/components/interface-settings/interface-settings.component';
import { AuthEntityComponent } from './layouts/auth-entity/auth-entity.component';
import { TmsLayoutComponent } from './layouts/tms-layout/tms-layout.component';
import { ToggleMenuComponent } from './shared/components/toggle-menu/toggle-menu.component';
import { INIT_COORDS } from './tokens';
import { MatDialogModule } from '@angular/material/dialog';
import { MatTableModule } from '@angular/material/table';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatSortModule } from '@angular/material/sort';

@NgModule({
  imports: [
    FormsModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
    HttpClientModule,
    RouterModule,
    AppRoutingModule,
    MatDialogModule ,
    MatPaginatorModule,
    MatSortModule,
    MatTableModule
  ],
  declarations: [
    AppComponent,
    AdminLayoutComponent, 
    AuthLayoutComponent,
    TmsLayoutComponent,
    UsersComponent,
    FooterComponent,
    SidebarComponent,
    HeaderComponent,
    NavbarComponent,
    MenuComponent,
    InterfaceSettingsComponent,
    AuthEntityComponent,
    ToggleMenuComponent
  ],
  providers: [
    { provide: INIT_COORDS, useValue: {lat: 32.9756, long: -96.89} }

  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
