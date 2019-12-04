import { TestBed } from '@angular/core/testing';

import { FlaskserviceService } from './flaskservice.service';

describe('FlaskserviceService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: FlaskserviceService = TestBed.get(FlaskserviceService);
    expect(service).toBeTruthy();
  });
});
