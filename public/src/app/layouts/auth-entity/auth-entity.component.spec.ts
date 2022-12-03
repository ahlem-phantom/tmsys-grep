import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AuthEntityComponent } from './auth-entity.component';

describe('AuthEntityComponent', () => {
  let component: AuthEntityComponent;
  let fixture: ComponentFixture<AuthEntityComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AuthEntityComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AuthEntityComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
