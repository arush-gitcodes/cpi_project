import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule, RouterOutlet } from '@angular/router';

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
  
}


