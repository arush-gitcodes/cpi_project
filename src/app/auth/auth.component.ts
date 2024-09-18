// src/app/components/auth/auth.component.ts
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { AuthService } from '../services/auth.service';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-auth',
  standalone:true,
  imports:[CommonModule,FormsModule,ReactiveFormsModule],
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css']
})

export class AuthComponent implements OnInit {
  authForm: FormGroup;
  isLoginMode = true;
  isLoading = false;
  errorMessage: string | null = null;
  successMessage: string | null = null;

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private router: Router
  ) {
    this.authForm = this.fb.group({
      username: ['', [Validators.required, Validators.minLength(3)]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]]
    });
  }

  ngOnInit() {
    this.updateFormValidation();
  }

  toggleMode(): void {
    this.isLoginMode = !this.isLoginMode;
    this.updateFormValidation();
    this.authForm.reset();
    this.errorMessage = null;
    this.successMessage = null;
  }

  updateFormValidation(): void {
    const emailControl = this.authForm.get('email');
    if (this.isLoginMode) {
      emailControl?.clearValidators();
      emailControl?.updateValueAndValidity();
    } else {
      emailControl?.setValidators([Validators.required, Validators.email]);
      emailControl?.updateValueAndValidity();
    }
  }

  onSubmit(): void {
    if (this.authForm.valid) {
      this.isLoading = true;
      this.errorMessage = null;
      this.successMessage = null;

      if (this.isLoginMode) {
        this.login();
      } else {
        this.register();
      }
    } else {
      this.errorMessage = 'Please fill out all required fields correctly.';
    }
  }

  private login(): void {
    const { username, password } = this.authForm.value;
    this.authService.login(username, password).subscribe({
      next: (response) => {
        this.authService.setToken(response.access_token);
        this.successMessage = 'Login successful. Redirecting...';
        setTimeout(() => this.router.navigate(['/home']), 2000);
      },
      error: (error) => {
        console.error('Login failed', error);
        this.errorMessage = 'Login failed. Please check your credentials and try again.';
        this.isLoading = false;
      }
    });
  }

  private register(): void {
    this.authService.register(this.authForm.value).subscribe({
      next: () => {
        this.successMessage = 'Registration successful! You can now log in.';
        this.isLoginMode = true;
        this.authForm.reset();
        this.updateFormValidation();
      },
      error: (error) => {
        console.error('Registration failed', error);
        this.errorMessage = 'Registration failed. Please try again.';
      },
      complete: () => {
        this.isLoading = false;
      }
    });
  }

  onGoogleLogin(): void {
    // Implement Google login logic
    console.log('Google login clicked');
  }

  onFacebookLogin(): void {
    // Implement Facebook login logic
    console.log('Facebook login clicked');
  }
}
