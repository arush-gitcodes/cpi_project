import { Component } from '@angular/core';
import { NavigationEnd, Router, RouterOutlet } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { HeaderComponent } from './components/header/header.component';
import { FooterComponent } from './components/footer/footer.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { HomeComponent } from "./components/home/home.component";
import { DailyCheckInComponent } from './components/daily-checkin/daily-checkin.component';
import { UserProfileComponent } from './components/user-profile/user-profile.component';
import { filter } from 'rxjs';
import { EventsComponent } from './components/events/events.component';
import { HealthriskComponent } from './components/healthrisk/healthrisk.component';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, LoginComponent, HeaderComponent, FooterComponent,
     NavbarComponent, HomeComponent,DailyCheckInComponent,UserProfileComponent,EventsComponent,HealthriskComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'elderly_care';
  isAuthPage = false;

  constructor(private router: Router) {}

  ngOnInit() {
    this.router.events.pipe(
      filter(event => event instanceof NavigationEnd)
    ).subscribe((event: NavigationEnd) => {
      this.isAuthPage = event.urlAfterRedirects.startsWith('/auth');
    });
  }
}
