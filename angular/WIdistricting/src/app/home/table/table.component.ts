import { Component, OnInit } from '@angular/core';
import {MetricService} from '../../metric.service';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
export class TableComponent implements OnInit {

  public dataSource: StatewideMetrics[] = [];
  constructor(private metricService: MetricService) { }
  ngOnInit() {
    this.metricService.getStateWideMetrics().subscribe(data => this.processStatewideMetrics(data))
  }


  processStatewideMetrics(statewideMetrics: any): void {
    var data = statewideMetrics;
    for(var i = 0; i < 3; i++){
      data = data[i].fields;
      console.log(data);
      this.dataSource[i].avg_convex_hull = data.avg_convex_hull;
      this.dataSource[i].avg_polsby_popper = data.avg_polsby_popper;
      this.dataSource[i].avg_schwartzberg = data.avg_schwartzberg;
      this.dataSource[i].equal_population = data.equal_population;
      this.dataSource[i].name = data.name;
      this.dataSource[i].year = data.year;
    }
    console.log(this.dataSource);
  }

}

// TODO: update when we get more metrics in here
export interface StatewideMetrics{
  avg_convex_hull: number;
  avg_polsby_popper: number;
  equal_population: number;
  name: string;
  year: number;
  avg_schwartzberg: number;
}
