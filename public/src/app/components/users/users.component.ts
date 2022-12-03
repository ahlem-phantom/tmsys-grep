import { Component, OnInit } from '@angular/core';
import {UserService} from "../../core/services/user/user.service";
import {ActivatedRoute, Router} from "@angular/router";
import { User } from "../../core/models/user";

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.css']
})
export class UsersComponent implements OnInit {
  users: User[];
  usersList: any;


  constructor(private route:ActivatedRoute,private router: Router,private userService: UserService) { }

  ngOnInit(): void {
    this.listUsers();
  }

  listUsers() {
    this.userService.getAllUsers().subscribe(data => {
      this.users = data;
    });
  }

}
