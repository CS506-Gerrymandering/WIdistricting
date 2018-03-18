import { Routes, Router, RouterModule } from '@angular/router';
import { AppComponent } from 'app/app.component';
import { HomeComponent } from 'app/home/home.component';
import { MetricGuideComponent } from 'app/metric-guide/metric-guide.component';
import { DevGuideComponent } from 'app/dev-guide/dev-guide.component';
import { AboutComponent } from 'app/about/about.component';

export const appRoutes: Routes = [
    {path: 'home', component: HomeComponent},
    {path: 'metric-guide', component: MetricGuideComponent},
    {path: 'dev-guide', component: DevGuideComponent},
    {path: 'about', component: AboutComponent},
    {path: '**', redirectTo: 'home'}
]

export const AppRouting = RouterModule.forRoot(appRoutes, {
    useHash: false
})