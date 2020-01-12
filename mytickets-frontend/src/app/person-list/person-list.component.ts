import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {PersonService} from '../service/person.service';

@Component({
  selector: 'app-person-list',
  templateUrl: './person-list.component.html',
  styleUrls: ['./person-list.component.scss']
})
export class PersonListComponent implements OnInit {

  persons: any[];
  displayedColumns = ['fullname', 'format_birthday', 'internal', 'company_name', 'actions'];
  constructor(private http: HttpClient, private personService: PersonService ) { }

  ngOnInit() {
    this.personService.getPersons()
    // this.http.get('./api/ticket/list')
      .subscribe((response: any[]) => {
        this.persons = response;
      });
  }

  deletePerson(person: any) {
    this.personService.deletePerson(person.id)
    // this.http.delete('/api/movie/' + movie.id + '/delete')
      .subscribe(() => {
        this.ngOnInit();
      });
  }

}
