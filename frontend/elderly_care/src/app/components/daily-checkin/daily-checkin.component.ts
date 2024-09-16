import { Component } from '@angular/core';
import { DailyCheckService } from '../../services/daily-check.service';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HeaderComponent } from '../header/header.component';
import { NavbarComponent } from '../navbar/navbar.component';
import { FooterComponent } from '../footer/footer.component';

@Component({
  selector: 'app-daily-checkin',
  standalone: true,
  imports: [CommonModule, FormsModule, ReactiveFormsModule, HeaderComponent, NavbarComponent, FooterComponent],
  templateUrl: './daily-checkin.component.html',
  styleUrls: ['./daily-checkin.component.css'],
})
export class DailyCheckInComponent {
  // Activity Tracking
  tookWalk = false;
  didPhysicalActivity = false;
  stepCount: number | null = null;
  activityDuration: number | null = null;

  // Mood Tracking
  moodOptions = [
    { label: 'Happy', icon: '😊', value: 'happy' },
    { label: 'Sad', icon: '😢', value: 'sad' },
    { label: 'Neutral', icon: '😐', value: 'neutral' },
  ];
  selectedMood: string | null = null;
  feelingOptions = ['Calm', 'Energetic', 'Anxious', 'Depressed'];

  // Sleep Tracking
  sleepQuality: string | null = null;
  commonIssues: { [key: string]: boolean } = {
    snoring: false,
    legCramps: false,
    restlessLegs: false,
    nightSweats: false,
  };

  notes: string = '';

  // Meal Logging
  mealTypes = ['Breakfast', 'Lunch', 'Dinner', 'Snack'];
  selectedMeal: string | null = null;
  description: string = '';
  enjoyedMeal = false;
  goodAppetite = false;
  enoughFluids = false;

  // Pain Tracking
  painAreas = ['Head', 'Back', 'Legs', 'Arms'];
  selectedPainAreas: string[] = [];

  constructor(private dailyCheckService: DailyCheckService) {}

  // Activity Tracking Methods
  updateWalkStatus(status: boolean) {
    this.tookWalk = status;
  }

  updatePhysicalActivityStatus(status: boolean) {
    this.didPhysicalActivity = status;
  }

  // Mood Tracking Method
  selectMood(mood: string) {
    this.selectedMood = mood;
  }

  // Sleep Tracking Methods
  setSleepQuality(quality: string) {
    this.sleepQuality = quality;
  }

  toggleIssue(issue: string) {
    if (issue in this.commonIssues) {
      this.commonIssues[issue] = !this.commonIssues[issue];
    }
  }

  // Meal Logging Method
  logMeal() {
    console.log('Meal logged:', {
      type: this.selectedMeal,
      description: this.description,
      enjoyedMeal: this.enjoyedMeal,
      goodAppetite: this.goodAppetite,
      enoughFluids: this.enoughFluids,
    });
    // Here you would typically call a service method to save the meal data
  }

  // Pain Tracking Methods
  togglePainArea(area: string) {
    const index = this.selectedPainAreas.indexOf(area);
    if (index > -1) {
      this.selectedPainAreas.splice(index, 1);
    } else {
      this.selectedPainAreas.push(area);
    }
  }

  // Submit all the data
  submitCheckIn() {
    const checkInData = {
      tookWalk: this.tookWalk,
      didPhysicalActivity: this.didPhysicalActivity,
      stepCount: this.stepCount,
      activityDuration: this.activityDuration,
      selectedMood: this.selectedMood,
      sleepQuality: this.sleepQuality,
      commonIssues: this.commonIssues,
      notes: this.notes,
      meal: {
        type: this.selectedMeal,
        description: this.description,
        enjoyedMeal: this.enjoyedMeal,
        goodAppetite: this.goodAppetite,
        enoughFluids: this.enoughFluids,
      },
      selectedPainAreas: this.selectedPainAreas,
    };

    this.dailyCheckService.submitDailyCheck(checkInData).subscribe(
      (response) => {
        console.log('Daily check-in data submitted successfully', response);
      },
      (error) => {
        console.error('Error submitting daily check-in data', error);
      }
    );
  }

  skipCheckIn() {
    console.log('Check-in skipped');
    // Implement skip logic here, e.g., navigating to another page or resetting form
  }

  cancelTracking() {
    console.log('Tracking canceled');
    // Implement cancel logic here, e.g., resetting form fields or navigating away
  }

  saveTracking() {
    console.log('Tracking saved');
    // Implement save logic here, similar to submitCheckIn but for sleep tracking specifically
  }
  getCommonIssuesKeys(): string[] {
    return Object.keys(this.commonIssues);
  }
}