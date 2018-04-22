import { Component, OnInit } from '@angular/core';
import {MetricService} from '../../metric.service';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
export class TableComponent implements OnInit {

  public dataSource: StatewideMetrics[];
  public displayedColumns = ['Name', 'Average Convex Hull', 'Average Polsyby Popper', 'Average Schwartzberg', 'Equal Population', 'Year'];
  constructor(private metricService: MetricService) { }
  ngOnInit() {
    this.metricService.getStateWideMetrics().subscribe(data => this.processStatewideMetrics(data));
  }


  processStatewideMetrics(statewideMetrics: any): void {
    //console.log(statewideMetrics);
    // initializing the array <-- LMAO can't believe that worked
    this.dataSource = [{} as StatewideMetrics, {} as StatewideMetrics, {} as StatewideMetrics];
    for (let i = 0; i < 3; i++) {
      this.dataSource[i].avg_convex_hull = statewideMetrics[i].fields.avg_convex_hull;
      this.dataSource[i].avg_polsby_popper = statewideMetrics[i].fields.avg_polsby_popper;
      this.dataSource[i].avg_schwartzberg = statewideMetrics[i].fields.avg_schwartzberg;
      this.dataSource[i].equal_population = statewideMetrics[i].fields.equal_population;
      this.dataSource[i].name = statewideMetrics[i].fields.name;
      this.dataSource[i].year = statewideMetrics[i].fields.year;
    }
  }

}

// TODO: update when we get more metrics in here
export interface StatewideMetrics {
  avg_convex_hull: number;
  avg_polsby_popper: number;
  equal_population: number;
  name: string;
  year: number;
  avg_schwartzberg: number;
}
