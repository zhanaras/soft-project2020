import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { WelcomePageComponent } from './welcome-page/welcome-page.component';
import { TopComponent } from './top/top.component';
import { LoginComponent } from './login/login.component';
import { CategoryComponent } from './category/category.component';
import { CategoryproductsComponent } from './categoryproducts/categoryproducts.component';
import { BrandListComponent } from './brand-list/brand-list.component';


const routes: Routes = [
  {path: '', component: WelcomePageComponent},
  {path: 'top', component: TopComponent},
  {path: 'login', component: LoginComponent},
  {path: 'categories', component: CategoryComponent},
  {path: 'categories/:id/products', component: CategoryproductsComponent},
  {path: 'brands/:id/products', component: BrandListComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
