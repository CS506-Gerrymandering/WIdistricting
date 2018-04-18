import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';


@Injectable()
export class MetricService {

  constructor(private http: HttpClient) { }

  getAllDistrictMetrics(): any {
    return this.http.get('http://35.196.52.158:8000/api/get_all_district_metrics');
  }

  getStateWideMetrics(): any {
    return this.http.get('http://35.196.52.158:8000/api/get_statewide_metrics');
  }
}

