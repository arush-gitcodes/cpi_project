// src/app/services/auth.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { User,UserCreate } from '../model/user.model';
import { Token } from '../model/user.model'; 

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = 'http://localhost:8000';  // Replace with your FastAPI backend URL

  constructor(private http: HttpClient) { }

  register(user: UserCreate): Observable<User> {
    return this.http.post<User>(`${this.apiUrl}/register`, user);
  }

  login(username: string, password: string): Observable<Token> {
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    return this.http.post<Token>(`${this.apiUrl}/token`, formData);
  }

  setToken(token: string): void {
    localStorage.setItem('token', token);
  }

  getToken(): string | null {
    return localStorage.getItem('token');
  }

  isLoggedIn(): boolean {
    return !!this.getToken();
  }

  logout(): void {
    localStorage.removeItem('token');
  }
}