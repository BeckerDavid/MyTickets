import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class TicketService {

  constructor(private http: HttpClient) { }

  getTickets() {
    return this.http.get('api/ticket/list');
  }

  getTicket(ticketId: any) {
    return this.http.get('/api/ticket/' + ticketId + '/get');
  }

  createTicket(ticket: any) {
    return this.http.post('/api/ticket/create', ticket);
  }

  updateTicket(ticket: any) {
    return this.http.put('/api/ticket/' + ticket.id + '/update', ticket);
  }

  deleteTicket(ticketId: any) {
    return this.http.delete('/api/ticket/' + ticketId + '/delete');
  }
}
