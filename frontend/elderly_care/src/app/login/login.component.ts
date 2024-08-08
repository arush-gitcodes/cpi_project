// login-register.component.ts
import { Component } from '@angular/core';
import { FormBuilder, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-login',
  standalone:true,
  imports:[CommonModule,FormsModule,ReactiveFormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})


export class LoginComponent {
  loginForm: FormGroup;
  registrationForm: FormGroup;
  isLoginMode = true;

  constructor(
    private formBuilder: FormBuilder,
    private authService: AuthService
  ) {
    this.loginForm = this.formBuilder.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required]
    });

    this.registrationForm = this.formBuilder.group({
      firstName: ['', Validators.required],
      lastName: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(8)]],
      confirmPassword: ['', Validators.required],
      role: ['', Validators.required]
    }, {
      validator: this.passwordMatchValidator
    });
  }

  toggleMode() {
    this.isLoginMode = !this.isLoginMode;
  }

  onLogin() {
    if (this.loginForm.valid) {
      this.authService.login(
        this.loginForm.get('email')?.value,
        this.loginForm.get('password')?.value
      );
    }
  }

  onRegister() {
    if (this.registrationForm.valid) {
      this.authService.register(
        this.registrationForm.get('firstName')?.value,
        this.registrationForm.get('lastName')?.value,
        this.registrationForm.get('email')?.value,
        this.registrationForm.get('password')?.value,
        this.registrationForm.get('role')?.value
      );
    }
  }

  passwordMatchValidator(form: FormGroup) {
    const password = form.get('password')?.value;
    const confirmPassword = form.get('confirmPassword')?.value;
    return password === confirmPassword ? null : { passwordMismatch: true };
  }
}