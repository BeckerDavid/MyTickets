import {Injectable} from '@angular/core';
import {ActivatedRouteSnapshot, Resolve} from '@angular/router';
import {Observable} from 'rxjs';
import {PersonService} from '../service/Person.service';

@Injectable({
  providedIn: 'root'
})
export class PersonResolver implements Resolve<Observable<any>> {
  constructor(private personService: PersonService) {
  }

  resolve(route: ActivatedRouteSnapshot) {
    return this.personService.getPerson(route.paramMap.get('id'));
  }
}
