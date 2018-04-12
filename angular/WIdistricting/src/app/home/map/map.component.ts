import { Component, OnInit } from '@angular/core';
import * as mapboxgl from 'mapbox-gl';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {

  public map;
  
  constructor() { }

  ngOnInit() {
    this.createMap();
  }

  createMap() {
    mapboxgl.accessToken = 'pk.eyJ1Ijoic2tidW9ubyIsImEiOiJjamMxNTZqOGYwNDd2MndwaGxzMmx4dGI5In0.7b1mLqadQxU7eJci9wukGw';
    this.map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/skbuono/cjfrd0dh85pdh2so5ixruvpwk',
      position: 'relative',
      center: [-90, 44.8],
      zoom: 6,
      interactive: false
    });
  }
  
  //switches Mapbox style to display different district types
  switchMap(value: String) {
    let id;
    if (value == "Congress") {
      id = "cjfrd0dh85pdh2so5ixruvpwk"
    }
    else if (value == "State Senate") {
      id = "cjfwo9ix012gc2snwbqiq1hae"
    }
    else if (value == "State Assembly") {
      id = "cjfwogwk616q32rmidytk7ov8"
    }
    this.map.setStyle('mapbox://styles/skbuono/' + id);    
  }

}
