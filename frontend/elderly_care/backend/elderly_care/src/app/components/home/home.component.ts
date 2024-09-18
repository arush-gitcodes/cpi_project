import { CommonModule, DatePipe } from '@angular/common';
import { ChangeDetectorRef, Component, NgZone } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router, RouterModule, RouterOutlet } from '@angular/router';
import { HeaderComponent } from '../header/header.component';
import { NavbarComponent } from '../navbar/navbar.component';
import { FooterComponent } from '../footer/footer.component';
import { MatDialog } from '@angular/material/dialog';
import { ChatBotComponent } from '../chatbot/chatbot.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule,FormsModule,RouterOutlet,RouterModule,HeaderComponent,NavbarComponent,FooterComponent],
  providers:[DatePipe],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  constructor(public dialog: MatDialog,
    private datePipe: DatePipe,
    private cdr: ChangeDetectorRef,
    private ngZone: NgZone,
    private router: Router
  ) {    this.audioContext = new (window.AudioContext || (window as any).webkitAudioContext)();
  }

  openChatBot(): void {
    const dialogRef = this.dialog.open(ChatBotComponent, {
      width: '400px',
      height: '500px'
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
    });
  }
  private audioContext: AudioContext;
  private oscillator: OscillatorNode | null = null;
  private clockTimer: any;

  userName: string = '';
  currentDateTime: string | null = '';



  ngOnInit() {
    this.updateClock();
    this.ngZone.runOutsideAngular(() => {
      this.clockTimer = setInterval(() => {
        this.ngZone.run(() => {
          this.updateClock();
        });
      }, 1000);
    });
  }

  ngOnDestroy() {
    if (this.clockTimer) {
      clearInterval(this.clockTimer);
    }
  }

  private updateClock() {
    const now = new Date();
    this.currentDateTime = this.datePipe.transform(now, 'medium');
    this.cdr.markForCheck();
  }

  playAlarm() {
    this.oscillator = this.audioContext.createOscillator();
    this.oscillator.type = 'square';
    this.oscillator.frequency.setValueAtTime(440, this.audioContext.currentTime);
    this.oscillator.connect(this.audioContext.destination);
    this.oscillator.start();

    // Stop the alarm after 5 seconds
    setTimeout(() => {
      if (this.oscillator) {
        this.oscillator.stop();
      }
    }, 5000);
  }
  navigateToCheckIn(){
    this.router.navigate(['/daily-check-in']);
  }

}