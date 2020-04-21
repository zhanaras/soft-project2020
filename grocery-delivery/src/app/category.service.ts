import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { Category, Product, Brand, LoginResponse } from './models';

@Injectable({
  providedIn: 'root'
})
export class CategoryService {
  BASE_URL = 'http://localhost:8000';

  constructor(private http: HttpClient) { }

  getCategoryList(): Observable<Category[]> {
    return this.http.get<Category[]>(`${this.BASE_URL}/api/categories/`);
  }

  getBrandList(): Observable<Brand[]> {
    return this.http.get<Brand[]>(`${this.BASE_URL}/api/brands/`);
  }

  getProductsByCategories(id): Observable<Product[]>{
    return this.http.get<Product[]>(`${this.BASE_URL}/api/categories/${id}/products/`);
  }

  getProductsByBrand(id): Observable<Product[]>{
    return this.http.get<Product[]>(`${this.BASE_URL}/api/brands/${id}/products/`);
  }
}
