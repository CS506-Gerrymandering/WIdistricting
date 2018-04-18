import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import {MatCardModule, MatRadioModule, MatTableModule, MatToolbarModule} from '@angular/material';
import { MatSidenavModule } from '@angular/material';

import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';

import { AppRouting } from './app-routing/app-routing';
import { MapComponent } from './home/map/map.component';
import { TableComponent } from './home/table/table.component';
import { AboutComponent } from './about/about.component';
import { MetricGuideComponent } from './metric-guide/metric-guide.component';
import { DevGuideComponent } from './dev-guide/dev-guide.component';
import { NavbarComponent } from './navbar/navbar.component';
import {MetricService} from './metric.service';
import {HttpClientModule} from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    MapComponent,
    TableComponent,
    AboutComponent,
    MetricGuideComponent,
    DevGuideComponent,
    NavbarComponent
  ],
  imports: [
    BrowserModule,
    RouterModule,
    AppRouting,
    MatToolbarModule,
    MatSidenavModule,
    HttpClientModule,
    MatTableModule,
    MatCardModule,
    MatRadioModule
  ],
  providers: [MetricService],
  bootstrap: [AppComponent]
})
export class AppModule { }
