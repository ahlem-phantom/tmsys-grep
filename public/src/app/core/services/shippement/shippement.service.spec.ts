import { TestBed } from '@angular/core/testing';

import { ShippementService } from './shippement.service';

describe('ShippementService', () => {
  let service: ShippementService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ShippementService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
