import { ComponentFixture, TestBed } from '@angular/core/testing';
import { FormsModule } from '@angular/forms';
import { DailyCheckinComponent } from './daily-checkin.component';
describe('DailyCheckInComponent', () => {
  let component: DailyCheckinComponent;
  let fixture: ComponentFixture<DailyCheckinComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DailyCheckinComponent, FormsModule]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DailyCheckinComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});