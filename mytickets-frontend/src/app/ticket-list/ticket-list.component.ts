import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {TicketService} from '../service/ticket.service';

@Component({
  selector: 'app-ticket-list',
  templateUrl: './ticket-list.component.html',
  styleUrls: ['./ticket-list.component.scss']
})
export class TicketListComponent implements OnInit {

  tickets: any[];
  displayedColumns = ['id', 'customer_name', 'title', 'content', 'actions'];
  constructor(private http: HttpClient, private ticketService: TicketService ) { }

  ngOnInit() {
    this.ticketService.getTickets()
    // this.http.get('./api/ticket/list')
      .subscribe((response: any[]) => {
        this.tickets = response;
      });
  }

  deleteTicket(ticket: any) {
    this.ticketService.deleteTicket(ticket.id)
    // this.http.delete('/api/movie/' + movie.id + '/delete')
      .subscribe(() => {
        this.ngOnInit();
      });
  }

}
