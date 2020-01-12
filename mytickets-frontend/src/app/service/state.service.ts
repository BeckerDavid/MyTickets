import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class StateService {

  stateNames = {
    n: 'new',
    i: 'in progress',
    p: 'pending',
    c: 'cancel',
    d: 'done'
  };

  constructor() { }
}
