import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-task-list',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './task-list.component.html',
  styleUrls: ['./task-list.component.css']
})
export class TaskListComponent implements OnInit {
  taskTitle: string = '';
  taskDescription: string = '';
  taskName: string = '';
  taskInstructions: string = '';
  selectedCategory: string = '';
  selectedDueDate: string = '';
  selectedRepeat: string = '';
  currentMonth: string = '';
  selectedDate: number | null = null;
  calendarDays: number[][] = [];

  categories: string[] = ['Work', 'Personal', 'Shopping', 'Health'];
  dueDates: string[] = ['Today', 'Tomorrow', 'Next Week', 'Custom'];
  repeats: string[] = ['Never', 'Daily', 'Weekly', 'Monthly'];

  constructor() {}

  ngOnInit() {
    this.initializeCalendar();
  }

  initializeCalendar() {
    const today = new Date();
    this.currentMonth = today.toLocaleString('default', { month: 'long', year: 'numeric' });
    this.generateCalendarDays(today.getFullYear(), today.getMonth());
  }

  generateCalendarDays(year: number, month: number) {
    const firstDay = new Date(year, month, 1).getDay();
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    
    this.calendarDays = [];
    let week: number[] = Array(firstDay).fill(0);
    
    for (let day = 1; day <= daysInMonth; day++) {
      week.push(day);
      if (week.length === 7) {
        this.calendarDays.push(week);
        week = [];
      }
    }
    
    if (week.length > 0) {
      this.calendarDays.push(week);
    }
  }

  saveTask() {
    console.log('Saving task:', {
      title: this.taskTitle,
      description: this.taskDescription,
      category: this.selectedCategory,
      dueDate: this.selectedDueDate
    });
    // Implement actual save logic here
  }

  setDueDate() {
    if (this.selectedDate) {
      this.selectedDueDate = `${this.currentMonth} ${this.selectedDate}`;
      console.log('Due date set:', this.selectedDueDate);
    }
  }

  removeDate() {
    this.selectedDate = null;
    this.selectedDueDate = '';
    console.log('Due date removed');
  }

  changeMonth(direction: 'prev' | 'next') {
    const [month, year] = this.currentMonth.split(' ');
    const date = new Date(`${month} 1, ${year}`);
    
    if (direction === 'prev') {
      date.setMonth(date.getMonth() - 1);
    } else {
      date.setMonth(date.getMonth() + 1);
    }
    
    this.currentMonth = date.toLocaleString('default', { month: 'long', year: 'numeric' });
    this.generateCalendarDays(date.getFullYear(), date.getMonth());
  }

  selectDate(date: number) {
    this.selectedDate = date;
  }
}