import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InterfaceSettingsComponent } from './interface-settings.component';

describe('InterfaceSettingsComponent', () => {
  let component: InterfaceSettingsComponent;
  let fixture: ComponentFixture<InterfaceSettingsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ InterfaceSettingsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(InterfaceSettingsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
