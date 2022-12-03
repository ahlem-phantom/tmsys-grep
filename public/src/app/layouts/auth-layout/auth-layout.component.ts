import { Component, OnInit } from '@angular/core';
import {Form, FormBuilder, FormControl, FormGroup, Validators} from "@angular/forms";
import {ActivatedRoute, Router} from "@angular/router";
import { AuthenticationService } from 'src/app/core/services/authentication/authentication.service';
import { first } from 'rxjs/operators';
import { User } from 'src/app/core/models/user';

@Component({
  selector: 'app-auth-layout',
  templateUrl: './auth-layout.component.html',
  styleUrls: ['./auth-layout.component.css']
})
export class AuthLayoutComponent implements OnInit {
  form : FormGroup;
  submittedLogin=false;
  loading = false;
  returnUrl: string;
  error = '';


  constructor(
    private router:Router,
    private authenticationService: AuthenticationService
    ) { }

  ngOnInit(): void {
    this.form = new FormGroup({
      'username': new FormControl('',Validators.required),
     'password': new FormControl('',Validators.required),
    })

  }


  onSubmit() {
    this.submittedLogin = true;

    // stop here if form is invalid
    if (this.form.invalid) {
        return;
    }

    this.loading = true;
    this.authenticationService.login(this.form.value.username, this.form.value.password)
        .pipe(first())
        .subscribe(
            next => this.router.navigate(["/entity"]),
            error => {
                this.error = error;
                this.loading = false;
            });
}

}

