import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { LoginResponse } from './models';

@Injectable({
  providedIn: 'root'
})
export class AuthorizationService {
  BASE_URL = 'http://localhost:8000';

  constructor(private http: HttpClient) { }

  login(username, password): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(`${this.BASE_URL}/api/login/`, {
      username,
      password
    });
  }
}
