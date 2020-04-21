import { Component, OnInit } from '@angular/core';
import { AuthorizationService } from '../authorization.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  logged = false;
  username = '';
  password = '';

  constructor(private authorizationService: AuthorizationService,
              private route: ActivatedRoute) { }

  ngOnInit(): void {
    const token = localStorage.getItem('token');
    if (token){
      this.logged = true;
  }
}

  login(){
    this.authorizationService.login(this.username, this.password).subscribe(res => {
      localStorage.setItem('token', res.token);
      this.logged = true;
      this.username = '';
      this.password = '';
    });
  }

  logout(){
    localStorage.clear();
    this.logged = false;
  }
}

