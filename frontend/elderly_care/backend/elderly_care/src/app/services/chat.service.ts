import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ChatService {
  private apiUrl = 'http://localhost:8000'; // adjust this to your API URL

  constructor(private http: HttpClient) { }

  sendMessage(message: string): Observable<{ response: string }> {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json'
    });

    return this.http.post<{ response: string }>(`${this.apiUrl}/chat`, { message }, { headers })
      .pipe(
        catchError(error => {
          console.error('Error in chat service:', error);
          throw error;
        })
      );
  }
}