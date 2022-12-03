import { Component, ElementRef, OnInit} from '@angular/core';
import { ClientService } from 'src/app/core/services/client/client.service';
import { Client } from 'src/app/core/models/client';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Location } from '@angular/common';

@Component({
  selector: 'app-client',
  templateUrl: './client.component.html',
  styleUrls: ['./client.component.css']
})
export class ClientComponent implements OnInit {
	clients: Client[] = [];
  editForm: FormGroup;
  addForm: FormGroup;
  client: Client;
  page: number = 1;
  count: number = 0;
  tableSize: number = 7;
  tableSizes: any = [3, 6, 9, 12];

  constructor(private clientService: ClientService, private fb: FormBuilder,private elementRef: ElementRef) { }

  ngOnInit(): void {
    this.getClients();
    this.editForm = this.fb.group({
      company_address : [''],
      company_name : [''],
      company_phone : [''],
      company_email : ['']
     });
     this.addForm = this.fb.group({
      company_address : [''],
      company_name : [''],
      company_phone : [''],
      company_email : ['']
     });

  }

  getClients(): void {
		this.clientService.getClients().subscribe(clients => { this.clients = clients['clients']});
    

	}


  addClient(client: Client): void {
    console.log(this.clients)
		this.clientService.addClient(client);	
	}

  editClient(c: Client) {
    console.log(c);
    this.editForm.patchValue({
      company_address : c.company_address,
      company_name : c.company_name,
      company_phone : c.company_phone,
      company_email : c.company_email
     });
    
  }

  addSubmit() : void{
    console.log(this.addForm.getRawValue());
    this.client = this.addForm.getRawValue();
    this.clientService.addClient(this.client).subscribe(success=> {this.success()});   
  }

  deleteClient(c: Client) {
    console.log(c);
    this.clientService.deleteClient(c.client_id).subscribe(success=> {this.getClients();this.elementRef.nativeElement.querySelector('#deleteClient').close();});	
   
   }

   editSubmit(c: Client) {
    console.log("res:", this.editForm.getRawValue());
    this.clientService.updateClient(c.client_id,this.editForm.getRawValue()).subscribe(success=> {this.success()});   
   }
   
	success(): void {
    
	}

  onTableDataChange(event: any) {
    this.page = event;
    this.getClients();
  }
  onTableSizeChange(event: any): void {
    this.tableSize = event.target.value;
    this.page = 1;
    this.getClients();
  }

}

