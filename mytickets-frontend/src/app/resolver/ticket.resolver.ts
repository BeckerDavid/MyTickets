import {Injectable} from '@angular/core';
import {ActivatedRouteSnapshot, Resolve} from '@angular/router';
import {Observable} from 'rxjs';
import {TicketService} from '../service/ticket.service';

@Injectable({
  providedIn: 'root'
})
export class TicketResolver implements Resolve<Observable<any>> {
  constructor(private ticketService: TicketService) {
  }

  resolve(route: ActivatedRouteSnapshot) {
    return this.ticketService.getTicket(route.paramMap.get('id'));
  }
}
