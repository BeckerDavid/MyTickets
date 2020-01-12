import { Component, OnInit } from '@angular/core';
import {AbstractControl, FormBuilder, ValidatorFn, Validators} from '@angular/forms';
import {HttpClient} from '@angular/common/http';
import {PersonService} from '../service/person.service';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-person-form',
  templateUrl: './person-form.component.html',
  styleUrls: ['./person-form.component.scss']
})
export class PersonFormComponent implements OnInit {

  personFormGroup;
  // countryOptions;
  companyOptions;
  constructor(private fb: FormBuilder, private http: HttpClient, private personService: PersonService,
              private route: ActivatedRoute) { }

  ngOnInit() {

    this.personFormGroup = this.fb.group({
      id: [null],
      first_name: ['', [Validators.required, this.numberValidator()]],
      last_name: ['', [Validators.required, this.numberValidator()]],
      birthday: ['', Validators.required],
      internal: [null, Validators.required],
      company: [null, Validators.required],
    });

    const data = this.route.snapshot.data;
    // this.countryOptions = data.countryOptions;
    this.companyOptions = data.companyOptions;

    if (data.person) {
      this.personFormGroup.patchValue(data.person);
    }
  }

  createPerson() {
    const person = this.personFormGroup.value;
    if (person.id) {
      this.personService.updatePerson(person)
      // this.http.put('/api/movie/' + movie.id + '/update', movie)
        .subscribe(() => {
          alert('updated successfully');
        });
    } else {
      this.personService.createPerson(person)
      // this.http.post('/api/movie/create', this.movieFormGroup.value)
        .subscribe(() => {
          alert('created successfully');
        });
    }
  }

  numberValidator(): ValidatorFn {
    return (control: AbstractControl): { [key: string]: any } | null => {
      const forbidden = /\d/.test(control.value);
      return forbidden ? {number: {value: control.value}} : null;
    };
  }
}
