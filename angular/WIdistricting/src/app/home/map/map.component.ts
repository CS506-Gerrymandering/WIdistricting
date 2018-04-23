import { Component, Input, OnInit } from '@angular/core';
import { MetricService } from '../../metric.service';
import * as mapboxgl from 'mapbox-gl';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {

  public map: any;
  private metrics: any;

  constructor(private metricService: MetricService) {}

  ngOnInit() {
    this.metricService.getAllDistrictMetrics().subscribe(data => (this.handleMetrics(data)));
    this.createMap();
  }

  handleMetrics(data: any) {
    this.metrics = data;
    this.handlePointerEvents(data);
  }

  createMap() {
    mapboxgl.accessToken = 'pk.eyJ1Ijoic2tidW9ubyIsImEiOiJjamMxNTZqOGYwNDd2MndwaGxzMmx4dGI5In0.7b1mLqadQxU7eJci9wukGw';
    this.map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/skbuono/cjfrd0dh85pdh2so5ixruvpwk',
      position: 'relative',
      center: [-90, 44.8],
      zoom: 6,
    });
    this.map.addControl(new mapboxgl.NavigationControl());
    // disabling scrolling
    this.map.scrollZoom.disable();
  }

  handlePointerEvents(data: any) {
    let map = this.map;
    let popup;
    let metrics = data;
    let hover_disabled = false;
    //hover events
    this.map.on('mousemove', function (e) {
      if (!hover_disabled) {
        const features = map.queryRenderedFeatures(e.point);
        //determine district type
        let type;
        if (features[0].properties.District_S) {
          type = "Assembly";
        }
        else if (features[0].properties.SEN_NUM) {
          type = "Senate";
        }
        else {
          type = "Congress";
        }
        //remove previous popup to give appearance of following pointer
        if (popup) {
          popup.remove();
        }
        if (features[0].properties.STATENAME == "Wisconsin" || features[0].layer["source-layer"] == "Wisconsin_Senate_Districts_20-aki1n5"
        || features[0].layer["source-layer"] == "Wisconsin_Assembly_Districts_-akm189") {
          let district;
          let popup_text: string;
          //set popup data according to district 
          if (type == "Congress") {
            popup_text = "Congressional District " + features[0].properties.DISTRICT;
            // map.setFilter("congress-hover", ["==", "DISTRICT", features[0].properties.DISTRICT]); 
            district = metrics.filter(dist => dist.fields.office == "House").filter(dist => dist.fields.district_no == features[0].properties.DISTRICT)[0];
          }
          else if (type == "Assembly") {
            popup_text = "State Assembly District " + features[0].properties.District_S;
            // map.setFilter("assembly-hover", ["==", "District_S", features[0].properties.District_S]);                        
            district = metrics.filter(dist => dist.fields.office == "State Assembly").filter(dist => dist.fields.district_no == features[0].properties.District_S)[0];
          }
          else {
            popup_text = "State Senate District " + features[0].properties.SEN_NUM;
            // map.setFilter("senate-hover", ["==", "SEN_NUM", features[0].properties.SEN_NUM]);                        
            district = metrics.filter(dist => dist.fields.office == "State Senate").filter(dist => dist.fields.district_no == features[0].properties.SEN_NUM)[0];            
          }
          popup = new mapboxgl.Popup({closeButton: false})
            .setLngLat(e.lngLat)
            .setHTML("<div class='center'>" + popup_text +
              "</br> Convex Hull Ratio: " + district.fields.convex_hull_ratio +
              "</br> Polsby Popper: " + district.fields.polsby_popper +
              "</br> Schwartzberg: " + district.fields.shwartzberg + "</div>")
          popup.addTo(map);
      }
     }
    });
    //click events
    this.map.on('click', function (e) {
      const features = map.queryRenderedFeatures(e.point);
      //determine district type
      let type;
      if (features[0].properties.District_S) {
        type = "Assembly";
      }
      else if (features[0].properties.SEN_NUM) {
        type = "Senate";
      }
      else {
        type = "Congress";
      }
      if (features[0].properties.STATENAME == "Wisconsin" || features[0].layer["source-layer"] == "Wisconsin_Senate_Districts_20-aki1n5"
      || features[0].layer["source-layer"] == "Wisconsin_Assembly_Districts_-akm189") {
        hover_disabled = true;
        let popup_text: string;
        let district;
        //set popup data according to district type
        if (type == "Congress") {
          popup_text = "Congressional District " + features[0].properties.DISTRICT;          
          // map.setFilter("congress-hover", ["==", "DISTRICT", features[0].properties.DISTRICT]); 
          district = metrics.filter(dist => dist.fields.office == "House").filter(dist => dist.fields.district_no == features[0].properties.DISTRICT)[0];          
        }
        else if (type == "Assembly") {
          popup_text = "State Assembly District " + features[0].properties.District_S;
          // map.setFilter("assembly-hover", ["==", "District_S", features[0].properties.District_S]);                              
          district = metrics.filter(dist => dist.fields.office == "State Assembly").filter(dist => dist.fields.district_no == features[0].properties.District_S)[0];          
        }
        else {
          popup_text = "State Senate District " + features[0].properties.SEN_NUM;
          map.setFilter("senate-hover", ["==", "SEN_NUM", features[0].properties.SEN_NUM]);                                  
          district = metrics.filter(dist => dist.fields.office == "State Senate").filter(dist => dist.fields.district_no == features[0].properties.SEN_NUM)[0];                  
        }
        popup = new mapboxgl.Popup()
          .setLngLat(e.lngLat)
          .setHTML("<div class='center'>" + popup_text + "</br> Convex Hull Ratio: " + district.fields.convex_hull_ratio +
          "</br> Polsby Popper: " + district.fields.polsby_popper +
          "</br> Schwartzberg: " + district.fields.shwartzberg + "</div>")
        popup.addTo(map);
        //re-enables hover listening when click popup is closed
        popup.on('close', function(e) {
          hover_disabled = false;
        })
      }
    });
    // Reset the hover layers' filter when the mouse leaves the layers.
    // this.map.on("mouseleave", "assembly", function() {
    //   if (!hover_disabled)
    //     map.setFilter("assembly-hover", ["==", "District_S", ""]);
    // });
    // this.map.on("mouseleave", "senate", function() {
    //   if (!hover_disabled)
    //     map.setFilter("senate-hover", ["==", "SEN_NUM", ""]);
    // });
    // this.map.on("mouseleave", "congress", function() {
    //   if (!hover_disabled)
    //     map.setFilter("congress-hover", ["==", "DISTRICT", ""]);
    // });
  }

  //switches Mapbox style to display different district types
  switchMap(value: String) {
    let id;
    if (value == "Congress") {
      id = "cjfrd0dh85pdh2so5ixruvpwk";
    }
    else if (value == "State Senate") {
      id = "cjfwo9ix012gc2snwbqiq1hae";
    }
    else if (value == "State Assembly") {
      id = "cjfwogwk616q32rmidytk7ov8";
    }
    this.map.setStyle('mapbox://styles/skbuono/' + id);
  }

}
