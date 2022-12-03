import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ToggleMenuComponent } from './toggle-menu.component';

describe('ToggleMenuComponent', () => {
  let component: ToggleMenuComponent;
  let fixture: ComponentFixture<ToggleMenuComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ToggleMenuComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ToggleMenuComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
