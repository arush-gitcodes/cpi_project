import { Component, OnInit, OnDestroy, ChangeDetectorRef, NgZone, ChangeDetectionStrategy } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HealthRiskService } from '../../services/healthrisk.service';
import { CommonModule, DatePipe } from '@angular/common';
import { HeaderComponent } from '../header/header.component';
import { FooterComponent } from '../footer/footer.component';
import { NavbarComponent } from '../navbar/navbar.component';
import { Router, RouterModule } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-health-risk',
  standalone: true,
  imports: [
    CommonModule,
    HeaderComponent,
    FooterComponent,
    NavbarComponent,
    RouterModule,
    ReactiveFormsModule
  ],
  templateUrl: './healthrisk.component.html',
  styleUrls: ['./healthrisk.component.css'],
  providers: [DatePipe],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class HealthriskComponent implements OnInit,OnDestroy {
  healthForm: FormGroup;
  predictionResult: any = null;
  isLoading = false;
  errorMessage: string = '';
  private audioContext: AudioContext;
  private oscillator: OscillatorNode | null = null;
  private clockTimer: any;
  userName: string = '';
  currentDateTime: string | null = '';



  constructor(private fb: FormBuilder, private healthRiskService: HealthRiskService,
    private datePipe: DatePipe,
    private cdr: ChangeDetectorRef,
    private ngZone: NgZone,
    private router:Router
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
    this.ngZone.runOutsideAngular(() => {
      this.clockTimer = setInterval(() => {
        this.ngZone.run(() => {
          this.updateClock();
        });
      }, 1000);
    });
  }

  ngOnDestroy() {
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
    this.oscillator = this.audioContext.createOscillator();
    this.oscillator.type = 'square';
    this.oscillator.frequency.setValueAtTime(440, this.audioContext.currentTime);
    this.oscillator.connect(this.audioContext.destination);
    this.oscillator.start();

    // Stop the alarm after 5 seconds
    setTimeout(() => {
      if (this.oscillator) {
        this.oscillator.stop();
      }
    }, 5000);
  }

  // Handle form submission
  onSubmit() {
    if (this.healthForm.invalid) {
      this.errorMessage = 'Please fill out all required fields.';
      return;
    }

    this.isLoading = true;
    const healthData = this.healthForm.value;

    // Call the service to get the prediction result
    this.healthRiskService.predictRisk(healthData).subscribe(
      (result: any) => { // Specify the type based on your service's response
        this.predictionResult = result; // Store the entire response
        this.isLoading = false;
      },
      (error) => {
        this.errorMessage = 'Error occurred while predicting risk';
        console.error(error);
        this.isLoading = false;
      }
    );
  }

  // Close the popup card
  closePopup() {
    this.predictionResult = null;
  }

  hasProbabilities() {
    return this.predictionResult && this.predictionResult.risk_probabilities;
  }

 
}

