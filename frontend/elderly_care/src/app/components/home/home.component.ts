import { CommonModule, DatePipe } from '@angular/common';
import { ChangeDetectorRef, Component, NgZone, OnInit, OnDestroy } from '@angular/core';
import { FormBuilder, FormGroup, FormsModule, Validators } from '@angular/forms';
import { Router, RouterModule, RouterOutlet } from '@angular/router';
import { HeaderComponent } from '../header/header.component';
import { NavbarComponent } from '../navbar/navbar.component';
import { FooterComponent } from '../footer/footer.component';
import { MatDialog, MatDialogModule } from '@angular/material/dialog';
import { DailyQuotesComponent } from '../daily-quotes/daily-quotes.component';
import { HealthRiskService } from '../../services/healthrisk.service';
import { HealthriskComponent } from '../healthrisk/healthrisk.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    RouterOutlet,
    RouterModule,
    HeaderComponent,
    NavbarComponent,
    FooterComponent,
    MatDialogModule, // Add this import
    HealthriskComponent
  ],
  providers: [DatePipe],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent implements OnInit, OnDestroy {
  userName: string = '';
  currentDateTime: string | null = '';
  private audioContext: AudioContext;
  private oscillator: OscillatorNode | null = null;
  private clockTimer: any;

  constructor(
    public dialog: MatDialog,
    private datePipe: DatePipe,
    private cdr: ChangeDetectorRef,
    private ngZone: NgZone,
    private router: Router,
    private fb: FormBuilder, private healthRiskService: HealthRiskService
  ) {
    this.audioContext = new (window.AudioContext || (window as any).webkitAudioContext)();
    this.healthForm = this.fb.group({
      heart_rate: ['', Validators.required],
      systolic_bp: ['', Validators.required],
      diastolic_bp: ['', Validators.required],
      blood_sugar: ['', Validators.required],
      body_temperature: ['', Validators.required],
      bmi: ['', Validators.required],
      respiratory_rate: ['', Validators.required],
      age: ['', Validators.required],
    });
  }
 

  ngOnInit() {
    this.updateClock();
    this.startClockTimer();
    this.openDailyQuote(); // Add this to open the quote on init
  }

  ngOnDestroy() {
    this.stopClockTimer();
  }

  private startClockTimer() {
    this.ngZone.runOutsideAngular(() => {
      this.clockTimer = setInterval(() => {
        this.ngZone.run(() => {
          this.updateClock();
        });
      }, 1000);
    });
  }

  private stopClockTimer() {
    if (this.clockTimer) {
      clearInterval(this.clockTimer);
    }
  }

  private updateClock() {
    const now = new Date();
    this.currentDateTime = this.datePipe.transform(now, 'medium');
    this.cdr.markForCheck();
  }

  playAlarm() {
    if (this.oscillator) {
      this.oscillator.stop();
    }
    this.oscillator = this.audioContext.createOscillator();
    this.oscillator.type = 'square';
    this.oscillator.frequency.setValueAtTime(440, this.audioContext.currentTime);
    this.oscillator.connect(this.audioContext.destination);
    this.oscillator.start();

    setTimeout(() => {
      if (this.oscillator) {
        this.oscillator.stop();
        this.oscillator = null;
      }
    }, 5000);
  }

  navigateToCheckIn() {
    this.router.navigate(['/daily-check-in']);
  }

  openDailyQuote(): void {
    const dialogRef = this.dialog.open(DailyQuotesComponent, {
      width: '400px',
      height: '500px'
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
    });
  }
  healthForm: FormGroup;
  predictionResult: any = null;
  isLoading = false;
  errorMessage: string = '';

  

  // Handle form submission
  onSubmit() {
    if (this.healthForm.invalid) {
      return;
    }

    this.isLoading = true;
    const healthData = this.healthForm.value;

    // Call the service to get the prediction result
    this.healthRiskService.predictRisk(healthData).subscribe(
      (result) => {
        this.predictionResult = result; // Store the entire response
        this.isLoading = false;
      },
      (error) => {
        this.errorMessage = 'Error occurred while predicting risk';
        console.error(error);
        this.isLoading = false;
      }
    );
  }// Close the popup card
  closePopup() {
    this.predictionResult = null;
  }

  hasProbabilities() {
    return this.predictionResult && this.predictionResult.risk_probabilities;
}
navigateTohealthrisk() {
  this.router.navigate(['/healthrisk']);
}

}