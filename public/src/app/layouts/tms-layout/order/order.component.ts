import { Component, ElementRef, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Order } from 'src/app/core/models/order';
import { OrderService } from 'src/app/core/services/order/order.service';

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.css']
})
export class OrderComponent implements OnInit {

  orders : Order[] = [];
  editForm: FormGroup;
  addForm: FormGroup;
  order: Order;
  page: number = 1;
  count: number = 0;
  tableSize: number = 7;
  tableSizes: any = [3, 6, 9, 12];

  constructor(private orderService: OrderService, private fb: FormBuilder, private elementRef: ElementRef) { }

  ngOnInit(): void {
    this.getOrders();
    this.editForm = this.fb.group({
      order_address : [''],
      order_reference : [''],
      order_date : [''],
      order_code : [''],
      order_ht : [''],
      order_tva : [''],
      order_ttc : [''],
      order_lng : [''],
      order_lat : ['']
     });
     this.addForm = this.fb.group({
      order_address : [''],
      order_reference : [''],
      order_date : [''],
      order_code : [''],
      order_ht : [''],
      order_tva : [''],
      order_ttc : [''],
      order_lng : [''],
      order_lat : ['']
     });

  }

  getOrders(): void {
		this.orderService.getOrders().subscribe(orders => { this.orders = orders['orders']});
    

	}


  addOrder(order: Order): void {
    console.log(this.orders)
		this.orderService.addOrder(order);	
	}

  editOrder(o: Order) {
    console.log(o);
    this.editForm.patchValue({
      order_address : o.order_address,
      order_reference : o.order_reference,
      order_date : this.formatDate(o.order_date),
      order_code : o.order_code,
      order_ht : o.order_ht,
      order_tva : o.order_tva,
      order_ttc : o.order_ttc,
      order_lng : o.order_lng,
      order_lat : o.order_lat
     });
    
  }

   formatDate(date) {
    const d = new Date(date);
    let month = '' + (d.getMonth() + 1);
    let day = '' + d.getDate();
    const year = d.getFullYear();
    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;
    return [year, month, day].join('-');
  }

  addSubmit() : void{
    console.log(this.addForm.getRawValue());
    this.order = this.addForm.getRawValue();
    this.orderService.addOrder(this.order).subscribe(success=> {this.success()});   
  }

  deleteOrder(o: Order) {
    console.log(o);
    this.orderService.deleteOrder(o.client_id).subscribe(success=> {this.getOrders();this.elementRef.nativeElement.querySelector('#deleteOrder').close();});	
   
   }

   editSubmit(o: Order) {
    console.log("res:", this.editForm.getRawValue());
    this.orderService.updateOrder(o.client_id,this.editForm.getRawValue()).subscribe(success=> {this.success()});   
   }
   
	success(): void {
    
	}

  onTableDataChange(event: any) {
    this.page = event;
    this.getOrders();
  }
  onTableSizeChange(event: any): void {
    this.tableSize = event.target.value;
    this.page = 1;
    this.getOrders();
  }

}

