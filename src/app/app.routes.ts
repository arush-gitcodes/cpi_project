import { Routes } from '@angular/router';
import { DailyCheckInComponent } from './components/daily-checkin/daily-checkin.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { HomeComponent } from './components/home/home.component';
import { AppointmentComponent } from './components/appointment/appointment.component';
import { UserProfileComponent } from './components/user-profile/user-profile.component';
import { TaskListComponent } from './components/task-list/task-list.component';
import { LoginComponent } from './login/login.component';
import { AuthComponent } from './auth/auth.component';
import { EventsComponent } from './components/events/events.component';
import { HealthriskComponent } from './components/healthrisk/healthrisk.component';

export const routes: Routes = [
  { path: '', redirectTo: '/auth', pathMatch: 'full' },
  {path:'auth',component:AuthComponent,data: { isAuth: true }},
  { path: 'home', component: HomeComponent },
  { path: 'dashboard', component: DashboardComponent },
  {path:'profile',component:UserProfileComponent},
  {path:'events',component:EventsComponent},
  {path:'healthrisk',component:HealthriskComponent},

  //{ path: 'profile', component: ProfileComponent },
 { path: 'medication-appointments', component: AppointmentComponent },
  { path: 'daily-check-in', component: DailyCheckInComponent },
 { path: 'tasks', component: TaskListComponent },
  //{ path: 'social', component: SocialComponent },
//  { path: 'health', component: HealthComponent },
  { path: '**', redirectTo: '/home' } // Redirect to dashboard for any unknown routes
];
