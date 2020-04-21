import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { Product } from './models';

@Injectable({
  providedIn: 'root'
})
export class ProductsService {
  BASE_URL = 'http://localhost:8000';

  constructor(private http: HttpClient) { }

  getTop(): Observable<Product[]> {
    return this.http.get<Product[]>(`${this.BASE_URL}/api/top`);
  }
}
