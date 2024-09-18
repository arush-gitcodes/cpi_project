// app.module.ts
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule, HTTP_INTERCEPTORS, provideHttpClient, withFetch } from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';
import {IonicModule} from '@ionic/angular';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { AuthService } from './services/auth.service';
import { AppRoutingModule } from './app-routing.module';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { DailyCheckInComponent } from './components/daily-checkin/daily-checkin.component';
import { DatePipe } from '@angular/common';
import { UserProfileComponent } from './components/user-profile/user-profile.component';
import { HomeComponent } from './components/home/home.component';
import { MatDialogModule } from '@angular/material/dialog';
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { HealthriskComponent } from './components/healthrisk/healthrisk.component';


@NgModule({
  declarations: [],
  imports: [
    BrowserModule,
    HttpClientModule,
    ReactiveFormsModule,LoginComponent,AppComponent,AppRoutingModule,HomeComponent,
    DailyCheckInComponent,DashboardComponent,UserProfileComponent,IonicModule.forRoot(),MatDialogModule,MatButtonModule,
    MatInputModule,MatFormFieldModule,HealthriskComponent
  ],
  providers: [
    AuthService,provideHttpClient(withFetch()),DatePipe,
   
  ],
  bootstrap: []
})
export class AppModule { }