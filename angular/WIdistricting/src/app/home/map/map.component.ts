import { Component, OnInit } from '@angular/core';
import * as mapboxgl from 'mapbox-gl';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {

  private map;
  
  constructor() { }

  ngOnInit() {
    this.createMap();
  }

  createMap() {
    mapboxgl.accessToken = 'pk.eyJ1IjoiaHNhcmFidSIsImEiOiJjamV5c2hwYzcxbHZsMndtbTh0eGg4OHA0In0.F9BQxFrDAtgt9ouBarFRbg';
    this.map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/mapbox/streets-v9',
      position: 'relative'
    });
  }

}
