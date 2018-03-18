import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MetricGuideComponent } from './metric-guide.component';

describe('MetricGuideComponent', () => {
  let component: MetricGuideComponent;
  let fixture: ComponentFixture<MetricGuideComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MetricGuideComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MetricGuideComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
