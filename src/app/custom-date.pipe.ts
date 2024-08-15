// custom-date.pipe.ts
import { Pipe, PipeTransform } from '@angular/core';
import { DatePipe } from '@angular/common';

@Pipe({
  name: 'customDate'
})
export class CustomDatePipe implements PipeTransform {

  constructor(private datePipe: DatePipe) {}

  transform(value: Date | string | null, format: string = 'medium'): string | null {
    if (!value) return null;
    return this.datePipe.transform(value, format);
  }

}
