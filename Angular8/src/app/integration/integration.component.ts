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
  key = '';
  user = 'enrique';
  constructor(protected FlaskserviceService:FlaskserviceService) { }

  async ngOnInit() {
    await this.FlaskserviceService.getkey()
    .subscribe(
      (data) =>{
        this.key = this.FlaskserviceService.createReturnedKey(data['key'],this.user);
        this.FlaskserviceService.getUser(this.key)
        .subscribe(
          (data) =>{
            this.users = [data['data']];
          },
          (error) => {
            console.error(error);
            alert("we have some error");
          }
        );
      },
      (error) => {
        console.error(error);
        alert("we have some error");
      }
    );
  }
  onClickDoPost(formData) {
    const data ={'id':formData.id};
    this.FlaskserviceService.postUser(data,this.key)
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
    this.FlaskserviceService.putUser(data,this.key)
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
    this.FlaskserviceService.deleteUser(data,this.key)
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
