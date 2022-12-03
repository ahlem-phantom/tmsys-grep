import { Component, ElementRef, OnInit, Pipe , PipeTransform} from '@angular/core';
import { TruckService } from 'src/app/core/services/truck/truck.service';
import { Truck } from 'src/app/core/models/truck';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Location } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-truck',
  templateUrl: './truck.component.html',
  styleUrls: ['./truck.component.css']
})


export class TruckComponent implements OnInit {
	trucks: Truck[] = [];
  editForm: FormGroup;
  addForm: FormGroup;
  truck: Truck;
  page: number = 1;
  count: number = 0;
  tableSize: number = 7;
  tableSizes: any = [3, 6, 9, 12];

  constructor(private router : Router ,private truckService: TruckService, private fb: FormBuilder,private elementRef: ElementRef) { }

  ngOnInit(): void {
    this.getTrucks();
     this.addForm = this.fb.group({
      plate_number : [''],
      truck_type : [''],
      truck_status : [''],
      truck_driver : [''],
      truck_capacity : ['']
     });
  }

  getTrucks(): void {
		this.truckService.getTrucks().subscribe(trucks=> { this.trucks = trucks['trucks']});
	}


  addClient(truck: Truck): void {
    console.log(this.trucks)
		this.truckService.addTruck(truck);	
	}

  editClient(t: Truck) {
   
    this.router.navigate(['/tms/truck-details',t.truck_id])

  }

  addSubmit() : void{
    console.log(this.addForm.getRawValue());
    this.truck = this.addForm.getRawValue();
    this.truckService.addTruck(this.truck).subscribe(success=> {this.success()});   
  }

  deleteTruck(t: Truck) {
    console.log(t);
    this.truckService.deleteTruck(t.truck_id).subscribe(success=> {this.getTrucks();this.elementRef.nativeElement.querySelector('#deleteTruck').close();});	
   
   }

   
	success(): void {
    
	}

  onTableDataChange(event: any) {
    this.page = event;
    this.getTrucks();
  }
  onTableSizeChange(event: any): void {
    this.tableSize = event.target.value;
    this.page = 1;
    this.getTrucks();
  }

  getIcon(status) : any{
    if(status = 'Available') {
     return 'fas fa-check'
    }
    else if (status = 'Assigned'){
      return 'fas fa-check-box'
    }
    else {
      return ''
    }

    
  }


  getButton(status) : any{
    if(status = 'Available') {
      return 'btn btn-outline-info waves-effect waves-themed'
    }
  
    else if (status = 'Assigned'){
     return 'btn btn-sm btn-outline-info waves-effect waves-themed'
    }
    else {
     return ''
    }
  }
}

@Pipe({name: 'transform'})
export class StringPipe implements PipeTransform {
  transform(word: string): string {
    return word.replace('"','');
  }
}