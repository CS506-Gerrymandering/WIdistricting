import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';


@Injectable()
export class MetricService {

  constructor(private http: HttpClient) { }

  getAllDistrictMetrics(): any {
    return this.http.get('http://localhost:8000/api/get_all_district_metrics');
  }

}
