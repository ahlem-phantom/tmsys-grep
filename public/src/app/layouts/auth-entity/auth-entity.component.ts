import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormControl, FormGroup, Validators} from "@angular/forms";
import {Router} from "@angular/router";

@Component({
  selector: 'app-auth-entity',
  templateUrl: './auth-entity.component.html',
  styleUrls: ['./auth-entity.component.css']
})
export class AuthEntityComponent implements OnInit {
  myFormLogin: FormGroup;
  submittedLogin=false;

  constructor(private formBuilder: FormBuilder, private router:Router) { }

  ngOnInit(): void {
    this.myFormLogin=  this.formBuilder.group(
      {
        

      });
  }

  login(myForm:FormGroup){
    this.submittedLogin = true;
    localStorage.setItem("currentUser","1");
    this.router.navigate(["/app/inbox"]);
  }

}

