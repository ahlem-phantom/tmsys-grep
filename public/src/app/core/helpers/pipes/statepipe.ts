import { Pipe, PipeTransform } from '@angular/core';
@Pipe({
  name: 'transform'
})
export class StringPipe implements PipeTransform {
    transform(word: any): string {
      return word.split('"').join('')
    }
  }
