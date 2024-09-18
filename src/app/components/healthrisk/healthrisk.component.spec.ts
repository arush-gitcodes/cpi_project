import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HealthriskComponent } from './healthrisk.component';

describe('HealthriskComponent', () => {
  let component: HealthriskComponent;
  let fixture: ComponentFixture<HealthriskComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HealthriskComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(HealthriskComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
