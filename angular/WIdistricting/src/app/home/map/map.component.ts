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
    mapboxgl.accessToken = 'pk.eyJ1Ijoic2tidW9ubyIsImEiOiJjamMxNTZqOGYwNDd2MndwaGxzMmx4dGI5In0.7b1mLqadQxU7eJci9wukGw';
    this.map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/mapbox/streets-v9',
      position: 'relative',
      center: [-90, 44.8],
      zoom: 6
    });
    this.map.setStyle('mapbox://styles/skbuono/cjfrd0dh85pdh2so5ixruvpwk')
    // this.map.addControl(new mapboxgl.NavigationControl());
  }

}
