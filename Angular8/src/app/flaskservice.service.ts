import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class FlaskserviceService {
  url = "http://127.0.0.1:5000/";
  constructor(protected http:HttpClient) {
   }  
  getUser(key) {
    const options = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'key':key
      }),
      body: {},
    };
    return this.http.get(this.url+'getuser',options);
  }
  postUser(data,key) {
    const headers = new HttpHeaders({'Content-Type':'application/json; charset=utf-8','key':key});
    return this.http.post(this.url+'postuser', data,{headers:headers});
  }
  putUser(data,key) {
    const headers = new HttpHeaders({'Content-Type':'application/json; charset=utf-8','key':key});
    return this.http.put(this.url+'putuser', data,{headers:headers});
  }
  deleteUser(data,key) {
    const options = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'key':key
      }),
      body: data,
    };
    return this.http.delete(this.url+'deleteuser',options);
  }
  getkey(){
    const options = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
      }),
      body: {},
    };
    return this.http.post(this.url+'getsecretkey',options);
  }
  createReturnedKey(key,user){
    return btoa(key+'USER:'+user);
  }
}
