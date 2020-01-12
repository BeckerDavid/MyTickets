import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {LoginComponent} from './login/login.component';
import {TicketListComponent} from './ticket-list/ticket-list.component';
import {AuthGuard} from './auth.guard';
import {TicketFormComponent} from './ticket-form/ticket-form.component';
import {TicketResolver} from './resolver/ticket.resolver';
import {CompanyOptionsResolver} from './resolver/company-options.resolver';
import {PersonOptionsResolver} from './resolver/person-options.resolver';
import {PersonListComponent} from './person-list/person-list.component';
import {PersonFormComponent} from './person-form/person-form.component';
import {PersonResolver} from './resolver/person.resolver';

const routes: Routes = [
  {path: 'login', component: LoginComponent},
  {path: 'ticket-list', component: TicketListComponent, canActivate: [AuthGuard]},
  {
    path: 'ticket-form',
    component: TicketFormComponent,
    canActivate: [AuthGuard],
     resolve: {
      companyOptions: CompanyOptionsResolver,
      personOptions: PersonOptionsResolver,
     }
  },
  {
    path: 'ticket-form/:id',
    component: TicketFormComponent,
    canActivate: [AuthGuard],
    resolve: {
      companyOptions: CompanyOptionsResolver,
      personOptions: PersonOptionsResolver,
      ticket: TicketResolver,
    }
  },
  {path: 'person-list', component: PersonListComponent, canActivate: [AuthGuard]},
  {
    path: 'person-form',
    component: PersonFormComponent,
    canActivate: [AuthGuard],
    resolve: {
      companyOptions: CompanyOptionsResolver,
    }
  },
  {
    path: 'person-form/:id',
    component: PersonFormComponent,
    canActivate: [AuthGuard],
    resolve: {
      companyOptions: CompanyOptionsResolver,
      person: PersonResolver,
    }
  },
  {path: '', redirectTo: 'login', pathMatch: 'full'},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
