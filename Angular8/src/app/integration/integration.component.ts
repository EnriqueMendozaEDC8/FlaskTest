import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { FlaskserviceService } from '../flaskservice.service';

@Component({
  selector: 'app-integration',
  templateUrl: './integration.component.html',
  styleUrls: ['./integration.component.css']
})
export class IntegrationComponent implements OnInit {
  users: any[] = [];
  postUsers: any[] = [];
  constructor(protected FlaskserviceService:FlaskserviceService) { }

  ngOnInit() {
    this.FlaskserviceService.getUser()
    .subscribe(
      (data) =>{
        this.users = [data['data']];
      },
      (error) => {
        console.error(error);
        alert("we have some error");
      }
    );
  }
  onClickDoPost(formData) {
    const data ={'id':formData.id};
    this.FlaskserviceService.postUser(data)
    .subscribe(
      (data) =>{
        this.postUsers = [data['data']];
      }, (error) => {
        console.error(error);
        alert("we have some error");
      }
    );
  }
  onClickDoPut(formData) {
    const data ={
      'name':formData.name,
      'birthdate':formData.date,
      'job':formData.job,
    };
    this.FlaskserviceService.putUser(data)
    .subscribe(
      (data) =>{
        this.ngOnInit();
      }, (error) => {
        console.error(error);
        alert("we have some error");
      }
    );
  }
  onClickDoDelete(formData) {
    const data ={'id':formData.id};
    this.FlaskserviceService.deleteUser(data)
    .subscribe(
      (data) =>{
        this.ngOnInit();
      }, (error) => {
        console.error(error);
        alert("we have some error");
      }
    );
  }
}
