// auth.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { BehaviorSubject, Observable } from 'rxjs';

interface User {
  id: string;
  firstName: string;
  lastName: string;
  email: string;
  role: 'elderly' | 'caregiver';
  token: string;
}

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private currentUserSubject: BehaviorSubject<User | null>;
  public currentUser: Observable<User | null>;

  constructor(private http: HttpClient, private router: Router) {
    const storedUser = localStorage.getItem('currentUser');
    this.currentUserSubject = new BehaviorSubject<User | null>(
      storedUser ? JSON.parse(storedUser) : null
    );
    this.currentUser = this.currentUserSubject.asObservable();
  }

  public get currentUserValue(): User | null {
    return this.currentUserSubject.value;
  }

  login(email: string, password: string) {
    this.http.post<any>('/api/login', { email, password })
      .subscribe(
        (response) => {
          const user: User = {
            id: response.id,
            firstName: response.firstName,
            lastName: response.lastName,
            email: response.email,
            role: response.role,
            token: response.token
          };
          localStorage.setItem('currentUser', JSON.stringify(user));
          this.currentUserSubject.next(user);
          this.router.navigate(['/dashboard']);
        },
        (error) => {
          console.error('Login error:', error);
          // Handle login error
        }
      );
  }

  register(firstName: string, lastName: string, email: string, password: string, role: 'elderly' | 'caregiver') {
    this.http.post<any>('/api/register', { firstName, lastName, email, password, role })
      .subscribe(
        (response) => {
          const user: User = {
            id: response.id,
            firstName: response.firstName,
            lastName: response.lastName,
            email: response.email,
            role: response.role,
            token: response.token
          };
          localStorage.setItem('currentUser', JSON.stringify(user));
          this.currentUserSubject.next(user);
          this.router.navigate(['/dashboard']);
        },
        (error) => {
          console.error('Registration error:', error);
          // Handle registration error
        }
      );
  }

  logout() {
    // Remove user from local storage and update the currentUser subject
    localStorage.removeItem('currentUser');
    this.currentUserSubject.next(null);
    this.router.navigate(['/login']);
  }
}
