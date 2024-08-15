import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { AuthService } from '../services/auth.service';
import { gsap } from 'gsap';
import { Power2 } from 'gsap/all';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule, ReactiveFormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
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

  ngOnInit() {
    this.animateForm();
  }

  animateForm() {
    gsap.from('.card', {
      duration: 0.8,
      y: 50,
      opacity: 0,
      ease: Power2.easeOut,
      delay: 0.2
    });

    gsap.from('.login-button', {
      duration: 0.8,
      y: 50,
      opacity: 0,
      ease: Power2.easeOut,
      delay: 0.4
    });
  }

  toggleMode() {
    this.isLoginMode = !this.isLoginMode;
    this.animateFormSwitch();
  }

  animateFormSwitch() {
    const currentForm = this.isLoginMode ? '.login-form' : '.registration-form';
    const otherForm = this.isLoginMode ? '.registration-form' : '.login-form';

    gsap.to(otherForm, {
      duration: 0.3,
      opacity: 0,
      y: 20,
      ease: Power2.easeIn,
      onComplete: () => {
        gsap.to(currentForm, {
          duration: 0.3,
          opacity: 1,
          y: 0,
          ease: Power2.easeOut
        });
      }
    });
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