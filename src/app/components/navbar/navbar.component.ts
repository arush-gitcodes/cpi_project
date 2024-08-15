import { Component } from '@angular/core';
import { Router, RouterModule, RouterOutlet } from '@angular/router';
import { DailyCheckinComponent } from '../daily-checkin/daily-checkin.component';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HomeComponent } from '../home/home.component';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [CommonModule,FormsModule,RouterOutlet,RouterModule,DailyCheckinComponent,HomeComponent],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent {
  constructor(private router:Router){}

  logout() {
    // Implement logout logic
  }
  navigateToCheckIn(){
    this.router.navigate(['/daily-check-in']);
  }
}
