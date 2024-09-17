import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DailyQuotesComponent } from './daily-quotes.component';

describe('DailyQuotesComponent', () => {
  let component: DailyQuotesComponent;
  let fixture: ComponentFixture<DailyQuotesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DailyQuotesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DailyQuotesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
