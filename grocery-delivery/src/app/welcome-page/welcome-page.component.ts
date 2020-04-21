import { Component, OnInit } from '@angular/core';
import { Product, Category, Brand } from '../models';
import { ActivatedRoute } from '@angular/router';
import { ProductsService } from '../products.service';
import { CategoryService } from '../category.service';


@Component({
  selector: 'app-welcome-page',
  templateUrl: './welcome-page.component.html',
  styleUrls: ['./welcome-page.component.css']
})
export class WelcomePageComponent implements OnInit {
  categories: Category[] = [];
  brands: Brand[] = [];

  constructor(public categoryService: CategoryService,
              private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.getCategoryList();
  }

  getCategoryList(){
    this.categoryService.getCategoryList().subscribe(categories => {this.categories = categories; });
  }

  getBrandList(){
    this.categoryService.getBrandList().subscribe(brands => {this.brands = brands; });
  }

}
