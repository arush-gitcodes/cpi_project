import { Component } from '@angular/core';
import { ChatService } from '../../services/chat.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MatDialogTitle, MatDialogContent, MatDialogActions } from '@angular/material/dialog';
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';

@Component({
  selector: 'app-chat-bot',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    MatDialogTitle,
    MatDialogContent,
    MatDialogActions,
    MatButtonModule,
    MatInputModule,
    MatFormFieldModule
  ],
  template: `
    <h2 mat-dialog-title>Elderly Care Assistant</h2>
    <mat-dialog-content class="mat-typography">
      <div class="chat-messages">
        <div *ngFor="let message of messages" [ngClass]="{'user-message': message.sender === 'You', 'bot-message': message.sender === 'Assistant'}">
          <strong>{{ message.sender }}:</strong> {{ message.text }}
        </div>
      </div>
    </mat-dialog-content>
    <mat-dialog-actions align="end">
      <mat-form-field class="chat-input">
        <input matInput [(ngModel)]="userMessage" placeholder="Type your message..." (keyup.enter)="sendMessage()">
      </mat-form-field>
      <button mat-raised-button color="primary" (click)="sendMessage()">Send</button>
    </mat-dialog-actions>
  `,
  styles: [`
    .chat-messages {
      height: 300px;
      overflow-y: auto;
      margin-bottom: 20px;
    }
    .chat-input {
      width: 100%;
      margin-right: 10px;
    }
    .user-message {
      text-align: right;
      color: #1976d2;
    }
    .bot-message {
      text-align: left;
      color: #43a047;
    }
  `]
})
export class ChatBotComponent {
  messages: { sender: string, text: string }[] = [];
  userMessage = '';

  constructor(private chatService: ChatService) {}

  sendMessage() {
    if (this.userMessage.trim() === '') return;

    this.messages.push({ sender: 'You', text: this.userMessage });

    this.chatService.sendMessage(this.userMessage).subscribe(
      response => {
        this.messages.push({ sender: 'Assistant', text: response.response });
      },
      error => {
        console.error('Error:', error);
        this.messages.push({ sender: 'Assistant', text: 'Sorry, I encountered an error. Please try again.' });
      }
    );

    this.userMessage = '';
  }
}