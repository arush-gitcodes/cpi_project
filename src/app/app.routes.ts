import { Routes } from '@angular/router';
import { DailyCheckinComponent } from './components/daily-checkin/daily-checkin.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { HomeComponent } from './components/home/home.component';
import { AppointmentComponent } from './components/appointment/appointment.component';
import { UserProfileComponent } from './components/user-profile/user-profile.component';
import { TaskListComponent } from './components/task-list/task-list.component';
import { LoginComponent } from './login/login.component';
import { AuthComponent } from './auth/auth.component';

export const routes: Routes = [
  { path: '', redirectTo: '/auth', pathMatch: 'full' },
  {path:'auth',component:AuthComponent,data: { isAuth: true }},
  { path: 'home', component: HomeComponent },
  { path: 'dashboard', component: DashboardComponent },
  {path:'profile',component:UserProfileComponent},
  //{ path: 'profile', component: ProfileComponent },
 { path: 'medication-appointments', component: AppointmentComponent },
  { path: 'daily-check-in', component: DailyCheckinComponent },
 { path: 'tasks', component: TaskListComponent },
  //{ path: 'social', component: SocialComponent },
//  { path: 'health', component: HealthComponent },
  { path: '**', redirectTo: '/home' } // Redirect to dashboard for any unknown routes
];
