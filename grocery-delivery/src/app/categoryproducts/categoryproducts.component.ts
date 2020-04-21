import { Component, OnInit } from '@angular/core';
import { CategoryService } from '../category.service';
import { ActivatedRoute } from '@angular/router';
import { Product } from '../models';

@Component({
  selector: 'app-categoryproducts',
  templateUrl: './categoryproducts.component.html',
  styleUrls: ['./categoryproducts.component.css']
})
export class CategoryproductsComponent implements OnInit {
  products: Product[] = [];

  constructor(public categoryService: CategoryService,
              private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.getProductsByCategory();
  }

  getProductsByCategory(){
    const id = +this.route.snapshot.paramMap.get('id');
    this.categoryService.getProductsByCategories(id).subscribe(products => {this.products = products; });
  }
}

