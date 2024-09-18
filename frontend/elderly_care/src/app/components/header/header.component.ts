import { CommonModule, DatePipe } from '@angular/common';
import { Component, OnInit, OnDestroy, ChangeDetectorRef, NgZone, ChangeDetectionStrategy } from '@angular/core';
import { HealthriskComponent } from "../healthrisk/healthrisk.component";
import { Router } from '@angular/router';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [CommonModule, DatePipe, HealthriskComponent],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css',
  providers: [DatePipe],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class HeaderComponent implements OnInit, OnDestroy {
triggerEmergency() {
throw new Error('Method not implemented.');
}
  private audioContext: AudioContext;
  private oscillator: OscillatorNode | null = null;
  private clockTimer: any;

  userName: string = '';
  currentDateTime: string | null = '';

  constructor(
    private datePipe: DatePipe,
    private cdr: ChangeDetectorRef,
    private ngZone: NgZone,
    private router:Router
  ) {
    this.audioContext = new (window.AudioContext || (window as any).webkitAudioContext)();
  }

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
  navigateTohealthrisk(){
    this.router.navigate(['/healthrisk']);
  }
}