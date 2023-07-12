import { Component, OnInit } from '@angular/core';
@Component({
  selector: 'app-upload-form',
  templateUrl: './upload-form.component.html',
  styleUrls: ['./upload-form.component.css'],
})
export class UploadFormComponent {
  selectedFiles?: FileList;

  constructor() {}

  selectFile(event: any): void {
    this.selectedFiles = event.target.files;
  }

  upload(): void {
    if (this.selectedFiles) {
      const file: File | null = this.selectedFiles.item(0);
      this.selectedFiles = undefined;

      if (file) {
        const API_ENDPOINT = 'http://127.0.0.1:5000/api/getVisualization';
        const request = new XMLHttpRequest();
        const formData = new FormData();

        request.open('POST', API_ENDPOINT, true);
        formData.append('file', file);
        request.send(formData);
      }
    }
  }
}
