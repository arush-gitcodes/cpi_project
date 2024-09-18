import { Component } from '@angular/core';

@Component({
  selector: 'app-daily-quotes',
  standalone: true,
  imports: [],
  templateUrl: './daily-quotes.component.html',
  styleUrl: './daily-quotes.component.css'
})
export class DailyQuotesComponent {

  quote: string = '';
  author: string = '';

  private quotes = [
    { quote: "Age is an issue of mind over matter. If you don't mind, it doesn't matter.", author: "Mark Twain" },
    { quote: "The longer I live, the more beautiful life becomes.", author: "Frank Lloyd Wright" },
    { quote: "None are so old as those who have outlived enthusiasm.", author: "Henry David Thoreau" },
    { quote: "You are never too old to set another goal or to dream a new dream.", author: "C.S. Lewis" },
    { quote: "Today is the oldest you've ever been, and the youngest you'll ever be again.", author: "Eleanor Roosevelt" },
    { quote: "The great thing about getting older is that you don't lose all the other ages you've been.", author: "Madeleine L'Engle" },
    { quote: "Wrinkles should merely indicate where smiles have been.", author: "Mark Twain" },
    { quote: "With age comes wisdom. You don't learn it, you age into it.", author: "Elizabeth Clephane" },
    { quote: "Do not grow old, no matter how long you live. Never cease to stand like curious children before the great mystery into which we were born.", author: "Albert Einstein" },
    { quote: "The longer I live, the more I realize the impact of attitude on life.", author: "Charles Swindoll" }
  ];

  ngOnInit() {
    this.setDailyQuote();
  }

  private setDailyQuote() {
    // Use the current date to seed the random number generator
    const today = new Date();
    const seed = today.getFullYear() * 10000 + (today.getMonth() + 1) * 100 + today.getDate();
    const randomIndex = this.seededRandom(seed, 0, this.quotes.length - 1);
    
    const selectedQuote = this.quotes[randomIndex];
    this.quote = selectedQuote.quote;
    this.author = selectedQuote.author;
  }

  private seededRandom(seed: number, min: number, max: number): number {
    const x = Math.sin(seed++) * 10000;
    const rand = x - Math.floor(x);
    return Math.floor(rand * (max - min + 1)) + min;
  }
}

