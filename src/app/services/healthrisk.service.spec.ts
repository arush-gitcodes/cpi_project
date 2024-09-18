import { TestBed } from '@angular/core/testing';

import { HealthriskService } from './healthrisk.service';

describe('HealthriskService', () => {
  let service: HealthriskService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(HealthriskService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
