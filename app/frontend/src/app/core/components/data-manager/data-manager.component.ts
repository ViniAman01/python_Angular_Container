import { Component, OnInit } from '@angular/core';
import * as FileSaver from 'file-saver';
import { SchoolService } from '../../services/school-service/school-service.service';
import { ShareDataService } from '../../services/share-data/share-data.service';
@Component({
  selector: 'app-data-manager',
  templateUrl: './data-manager.component.html',
  styleUrls: ['./data-manager.component.scss']
})
export class DataManagerComponent implements OnInit {
  receivedData : any
  constructor(
              private service_school : SchoolService,
              public service_data: ShareDataService,) {

              }
  ngOnInit(): void {
    this.getSharedData()

  }
  getSharedData(){
    this.service_data.data$.subscribe(data  => {
    this.receivedData = data;
      } )
  }
  downloadFile(): void {

		this.service_school.getSchoolFile().subscribe((data: Blob) => {
		const fileName = 'US_Schools.csv'
		FileSaver.saveAs(data, fileName)
		});
	}
}
