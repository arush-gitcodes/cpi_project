import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule, RouterOutlet } from '@angular/router';

interface Medication {
  time: string;
  name: string;
  taken: boolean;
}

@Component({
  selector: 'app-daily-checkin',
  standalone: true,
  imports: [CommonModule,FormsModule,ReactiveFormsModule,RouterOutlet,RouterModule],
  templateUrl: './daily-checkin.component.html',
  styleUrl: './daily-checkin.component.css'
})

export class DailyCheckinComponent implements OnInit {
  stepCount: number = 0;
  activityDuration: number = 0;
  tookWalk: boolean = false;
  didPhysicalActivity: boolean = false;
  moodOptions = [
    { icon: '☹', value: 0, label: '0' },
    { icon: '😐', value: 1, label: '1' },
    { icon: '🙂', value: 2, label: '2' },
    { icon: '😊', value: 3, label: '3' }
  ];

  feelingOptions = [
    "I'm feeling great",
    "I'm feeling good",
    "I'm okay",
    "I'm not doing well",
    "I'm feeling terrible"
  ];

  selectedMood: number | null = null;

  sleepQuality: string = '';
  commonIssues: { [key: string]: boolean } = {
    snoring: false,
    legCramps: false,
    restlessLegs: false,
    nightSweats: false
  };
  notes: string = '';
  mealTypes = ['Breakfast', 'Lunch', 'Snacks', 'Dinner'];
  selectedMeal: string = '';
  description: string = '';
  enjoyedMeal: boolean = false;
  goodAppetite: boolean = false;
  enoughFluids: boolean = false;


  painAreas = [
    'No pain', 'Pain in the head', 'Pain in the neck', 'Pain in the shoulder',
    'Pain in the chest', 'Pain in the heart', 'Pain in the stomach', 'Pain in the arm',
    'Pain in the elbow', 'Pain in the back', 'Pain in the leg', 'Pain in the knee',
    'Pain in the foot', 'Pain in the hip', 'Pain in the hand', 'Pain in the wrist',
    'Pain in the jaw'
  ];

  selectedPainAreas: string[] = [];

  morningMedications: Medication[] = [
    { time: '8:00 AM', name: 'Vitamin D 1000IU', taken: false },
    { time: '8:00 AM', name: 'Lipitor 20mg', taken: false }
  ];

  afternoonMedications: Medication[] = [
    { time: '2:00 PM', name: 'Aspirin 81mg', taken: false }
  ];

  eveningMedications: Medication[] = [
    { time: '8:00 PM', name: 'Metformin 1000mg', taken: false },
    { time: '8:00 PM', name: 'Losartan 50mg', taken: false }
  ];

  sideEffects: string = '';


  togglePainArea(area: string) {
    const index = this.selectedPainAreas.indexOf(area);
    if (index > -1) {
      this.selectedPainAreas.splice(index, 1);
    } else {
      this.selectedPainAreas.push(area);
    }
  }

  logMeal() {
    console.log('Logging meal:', {
      mealType: this.selectedMeal,
      description: this.description,
      enjoyedMeal: this.enjoyedMeal,
      goodAppetite: this.goodAppetite,
      enoughFluids: this.enoughFluids
    });
  }


  selectMood(mood: number) {
    this.selectedMood = mood;
  }

  constructor() { }

  ngOnInit(): void {
  }

  updateWalkStatus(status: boolean): void {
    this.tookWalk = status;
  }

  updatePhysicalActivityStatus(status: boolean): void {
    this.didPhysicalActivity = status;
  }

  submitCheckIn(): void {
    // Implement the logic to submit the check-in data
    console.log('Check-in submitted', {
      tookWalk: this.tookWalk,
      didPhysicalActivity: this.didPhysicalActivity,
      stepCount: this.stepCount,
      activityDuration: this.activityDuration
    });
  }

  skipCheckIn(): void {
    // Implement the logic to skip the check-in
    console.log('Check-in skipped');
  }
  setSleepQuality(quality: string) {
    this.sleepQuality = quality;
  }

  toggleIssue(issue: string) {
    this.commonIssues[issue] = !this.commonIssues[issue];
  }

  saveTracking() {
    console.log('Sleep quality:', this.sleepQuality);
    console.log('Common issues:', this.commonIssues);
    console.log('Notes:', this.notes);
    // Here you would typically send this data to a service
  }

  cancelTracking() {
    // Reset the form or navigate away
  }

  toggleMedication(medication: Medication): void {
    medication.taken = !medication.taken;
  }

  submitSideEffects(): void {
    console.log('Side effects submitted:', this.sideEffects);
    // Here you would typically send this data to a server
    this.sideEffects = ''; // Clear the input after submission
  }
  
}


