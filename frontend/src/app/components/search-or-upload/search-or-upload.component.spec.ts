import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchOrUploadComponent } from './search-or-upload.component';

describe('SearchOrUploadComponent', () => {
  let component: SearchOrUploadComponent;
  let fixture: ComponentFixture<SearchOrUploadComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SearchOrUploadComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SearchOrUploadComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
