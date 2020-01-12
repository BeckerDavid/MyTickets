import {Injectable} from '@angular/core';
import {Resolve} from '@angular/router';
import {Observable} from 'rxjs';
import {CompanyService} from '../service/company.service';

@Injectable({
  providedIn: 'root'
})
export class CompanyOptionsResolver implements Resolve<Observable<any>> {
  constructor(private companyService: CompanyService) {
  }

  resolve() {
    return this.companyService.getCompanies();
  }
}
