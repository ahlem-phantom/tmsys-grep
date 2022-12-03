import { Pipe, PipeTransform } from '@angular/core';
@Pipe({
  name: 'transform'
})
//removes "" and _
export class StringPipe implements PipeTransform {
    transform(word: any): string {
      return word[1].toUpperCase() + word.split('"').join('').split('_').join(' ').substring(1).toLowerCase();
    }
  }
