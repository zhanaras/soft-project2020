import { Component, OnInit } from '@angular/core';
import { Product } from '../models';
import { CategoryService } from '../category.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-brand-list',
  templateUrl: './brand-list.component.html',
  styleUrls: ['./brand-list.component.css']
})
export class BrandListComponent implements OnInit {
  products: Product[] = [];

  constructor(public categoryService: CategoryService,
              private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.getProductsByBrand();
  }

  getProductsByBrand(){
    const id = +this.route.snapshot.paramMap.get('id');
    this.categoryService.getProductsByBrand(id).subscribe(products => {this.products = products; });
  }

}
