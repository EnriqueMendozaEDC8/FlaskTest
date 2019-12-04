import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class FlaskserviceService {
  url = "http://165.227.25.5:5000/";
  constructor(protected http:HttpClient) {
   }  
  getUser() {
    return this.http.get(this.url+'getuser');
  }
  postUser(data) {
    return this.http.post(this.url+'postuser', data);
  }
  putUser(data) {
    return this.http.put(this.url+'putuser', data);
  }
  deleteUser(data) {
    const options = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
      }),
      body: data,
    };
    return this.http.delete(this.url+'deleteuser',options);
  }
}
