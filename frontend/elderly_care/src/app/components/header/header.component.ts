import { Component } from '@angular/core';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent {
  


  userName: string='';
  currentDateTime: Date | undefined;

  ngOnInit() {
    // Initialize user name and current date time
    this.currentDateTime=new Date();
  }

  triggerEmergency() {
    // Implement emergency alert logic
  }
}

