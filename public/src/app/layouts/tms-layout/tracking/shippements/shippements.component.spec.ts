import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShippementsComponent } from './shippements.component';

describe('ShippementsComponent', () => {
  let component: ShippementsComponent;
  let fixture: ComponentFixture<ShippementsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ShippementsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ShippementsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
