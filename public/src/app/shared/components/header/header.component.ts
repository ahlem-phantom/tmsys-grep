import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  constructor(private router:Router) { }

  ngOnInit(): void {
  }

  characters = [
    'inbox',
    'Aquaman',
    'Asterix',
    'The Atom',
    'The Avengers',
    'Batgirl',
    'Batman',
    'Batwoman',
  ]

  getUserIdsFirstWay($event) {
    let i = (<HTMLInputElement>document.getElementById('search-field')).value;
    this.router.navigate(["/app/"+i+""]);

    console.log("test"+i)
  }  

}
