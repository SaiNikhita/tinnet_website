import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SearchOrUploadComponent } from './components/search-or-upload/search-or-upload.component';
import { TableComponent } from './components/table/table.component';
import { StructureComponent } from './components/structure/structure.component';
import { AnalysisComponent } from './components/analysis/analysis.component';

@NgModule({
  declarations: [
    AppComponent,
    SearchOrUploadComponent,
    TableComponent,
    StructureComponent,
    AnalysisComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
