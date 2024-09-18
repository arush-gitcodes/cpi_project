import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
interface Event {
  type: string;
  time: string;
  description: string;
}
interface Appointment {
  doctorName: string;
  date: string;
  address: string;
}
@Component({
  selector: 'app-schedule',
  standalone: true,
  imports: [CommonModule,FormsModule,ReactiveFormsModule],
  templateUrl: './schedule.component.html',
  styleUrl: './schedule.component.css'
})
export class ScheduleComponent {
  todayEvents: Event[] = [
    { type: 'pill', time: '10:00 AM', description: 'Medication reminder' },
    { type: 'heartbeat', time: '11:00 AM', description: 'Physical Therapy' },
    { type: 'video', time: '5:00 PM', description: 'Zoom call with family' }
  ];

  tomorrowEvents: Event[] = [
    { type: 'pill', time: '10:00 AM', description: 'Medication reminder' },
    { type: 'heartbeat', time: '11:00 AM', description: 'Physical Therapy' },
    { type: 'video', time: '5:00 PM', description: 'Zoom call with family' }
  ];
  appointments: Appointment[] = [
    {
      doctorName: 'Dr. Andrew Johnson',
      date: 'Wed, Jan 10, 2023',
      address: '123 Main St, Apt 1A'
    },
    {
      doctorName: 'Dr. Andrew Johnson',
      date: 'Wed, Jan 20, 2023',
      address: '123 Main St, Apt 1A'
    },
    {
      doctorName: 'Dr. Andrew Johnson',
      date: 'Wed, Jan 30, 2023',
      address: '123 Main St, Apt 1A'
    }
  ];
  constructor() { }

  ngOnInit(): void {
  }

  getEventIcon(type: string): string {
    const icons: { [key: string]: string } = {
      pill: '<svg>...</svg>',
      heartbeat: '<svg>...</svg>',
      video: '<svg>...</svg>'
    };
    return icons[type as keyof typeof icons] || '';
  }
}
