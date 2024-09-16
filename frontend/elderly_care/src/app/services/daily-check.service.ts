import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DailyCheckService {
  private apiUrl = 'http://localhost:8000/api/daily-check'; // Adjust based on your FastAPI endpoint

  constructor(private http: HttpClient) {}

  submitDailyCheck(data: any): Observable<any> {
    return this.http.post(this.apiUrl, data);
  }

}
