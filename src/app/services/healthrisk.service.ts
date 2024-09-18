import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class HealthRiskService {
  private apiUrl = 'http://localhost:8000/predict';  // FastAPI endpoint

  constructor(private http: HttpClient) {}

  // Method to send health data and get risk prediction
  predictRisk(healthData: any): Observable<any> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    return this.http.post<any>(this.apiUrl, healthData, { headers });
  }
}
