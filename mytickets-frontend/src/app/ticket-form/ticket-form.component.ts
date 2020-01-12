import { Component, OnInit } from '@angular/core';
import {AbstractControl, FormBuilder, ValidatorFn, Validators} from '@angular/forms';
import {HttpClient, HttpClientModule} from '@angular/common/http';
import {TicketService} from '../service/ticket.service';
import {ActivatedRoute} from '@angular/router';
import {StateService} from '../service/state.service';
import {InputTextareaModule} from 'primeng/inputtextarea';

@Component({
  selector: 'app-ticket-form',
  templateUrl: './ticket-form.component.html',
  styleUrls: ['./ticket-form.component.scss']
})
export class TicketFormComponent implements OnInit {

  ticketFormGroup;
  // countryOptions;
  companyOptions;
  personOptions;
  constructor(private fb: FormBuilder, private http: HttpClient, private ticketService: TicketService,
              private route: ActivatedRoute, public stateService: StateService) { }

  ngOnInit() {

    this.ticketFormGroup = this.fb.group({
      id: [null],
      customer: [null, Validators.required],
      title: ['', Validators.required],
      content: ['', [Validators.required, this.lineFeedValidator()]],
      state: [null, Validators.required],
      contributor: [[]],
      // creation_date: ['', Validators.required],
    });

    // this.ticketFormGroup.controls.creation_date.valueChanges.subscribe(() => {
    //   const releaseDate = this.ticketFormGroup.controls.release_date.value;
    //   this.age = undefined;
    //   if (releaseDate) {
    //     this.age = this.calculateAge(new Date(releaseDate));
    //   }
    // });

    const data = this.route.snapshot.data;
    // this.countryOptions = data.countryOptions;
    this.companyOptions = data.companyOptions;
    this.personOptions = data.personOptions;

    if (data.ticket) {
      this.ticketFormGroup.patchValue(data.ticket);
    }
  }

  createTicket() {
    const ticket = this.ticketFormGroup.value;
    if (ticket.id) {
      this.ticketService.updateTicket(ticket)
      // this.http.put('/api/movie/' + movie.id + '/update', movie)
        .subscribe(() => {
          alert('updated successfully');
        });
    } else {
      this.ticketService.createTicket(ticket)
      // this.http.post('/api/movie/create', this.movieFormGroup.value)
        .subscribe(() => {
          alert('created successfully');
        });
    }
  }

  lineFeedValidator(): ValidatorFn {
    return (control: AbstractControl): { [key: string]: any } | null => {
      const forbidden = /\n/.test(control.value);
      return forbidden ? {lineFeed: {value: control.value}} : null;
    };
  }
}
