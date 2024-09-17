import { Component } from '@angular/core';
import { FormBuilder, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { HealthRiskService } from '../../services/healthrisk.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-health-risk',
  standalone:true,
  imports:[CommonModule,FormsModule,ReactiveFormsModule],
  templateUrl: './healthrisk.component.html',
  styleUrls: ['./healthrisk.component.css'],
})
export class HealthriskComponent {
  healthForm: FormGroup;
  predictionResult: any = null;
  isLoading = false;
  errorMessage: string = '';

  constructor(private fb: FormBuilder, private healthRiskService: HealthRiskService) {
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
        this.predictionResult = result;
        this.isLoading = false;
      },
      (error) => {
        this.errorMessage = 'Error occurred while predicting risk';
        console.error(error);
        this.isLoading = false;
      }
    );
  }
}
