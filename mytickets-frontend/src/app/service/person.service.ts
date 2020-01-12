import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class PersonService {

  constructor(private http: HttpClient) { }

  getPersons() {
    return this.http.get('api/person/list');
  }

  getPerson(personId: any) {
    return this.http.get('/api/person/' + personId + '/get');
  }

  createPerson(person: any) {
    return this.http.post('/api/person/create', person);
  }

  updatePerson(person: any) {
    return this.http.put('/api/person/' + person.id + '/update', person);
  }

  deletePerson(personId: any) {
    return this.http.delete('/api/person/' + personId + '/delete');
  }
}
