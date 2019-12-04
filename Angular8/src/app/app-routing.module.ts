import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { IntegrationComponent } from './integration/integration.component';
import { IndexComponent } from './index/index.component';

const routes: Routes = [
  {path:'', component:IndexComponent},
  {path:'implement', component:IntegrationComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
