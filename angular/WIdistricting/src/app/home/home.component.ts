import { Component, OnInit } from '@angular/core';
import {MetricService} from '../metric.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(private metrics: MetricService) { }

  ngOnInit() {
    this.metrics.getAllDistrictMetrics().subscribe(data => console.log(data));
  }

}
