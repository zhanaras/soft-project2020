import { Component, OnInit } from '@angular/core';
import { Product } from '../models';
import { ProductsService } from '../products.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-top',
  templateUrl: './top.component.html',
  styleUrls: ['./top.component.css']
})
export class TopComponent implements OnInit {
  products: Product[] = [];

  constructor(private productService: ProductsService,
              private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.getTop();
  }

  getTop(){
    this.productService.getTop().subscribe(products => {this.products = products; });
  }

}
