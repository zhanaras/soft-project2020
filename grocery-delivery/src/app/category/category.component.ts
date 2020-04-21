import { Component, OnInit } from '@angular/core';
import { Category, Product } from '../models';
import { CategoryService } from '../category.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.css']
})
export class CategoryComponent implements OnInit {
  categories: Category[] = [];
  products: Product[] = [];

  constructor(public categoryService: CategoryService,
              private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.getCategoryList();
  }

  getCategoryList(){
    const id = +this.route.snapshot.paramMap.get('id');
    this.categoryService.getCategoryList().subscribe(categories => {this.categories = categories; });
    this.categoryService.getProductsByCategories(id).subscribe(products => {this.products = products; });
  }
}
