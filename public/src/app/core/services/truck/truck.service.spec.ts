import { TestBed } from '@angular/core/testing';

import { TruckService } from './truck.service';

describe('TruckService', () => {
  let service: TruckService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TruckService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
