import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { FooterComponent } from "../footer/footer.component";
import { HeaderComponent } from "../header/header.component";
import { NavbarComponent } from "../navbar/navbar.component";

@Component({
  selector: 'app-events',
  standalone: true,
  imports: [CommonModule, FormsModule, FooterComponent, HeaderComponent, NavbarComponent,
    HeaderComponent,NavbarComponent,FooterComponent
  ],
  templateUrl: './events.component.html',
  styleUrl: './events.component.css'
})
export class EventsComponent {

  events = [
    {
      title: 'Group Reading',
      date: 'Wed, Jul 21, 10:00 AM',
      location: 'Alzheimer\'s Association, 123 Main St.',
      imageUrl: 'https://cdn.usegalileo.ai/stability/bd118542-ce7a-46b8-b641-5a04a4e0aa5b.png'
    },
    {
      title: ' Exercise classes',
      date: 'Wed, Jul 21, 10:00 AM',
      location: 'Alzheimer\'s Association, 123 Main St.',
      imageUrl: 'https://cdn.usegalileo.ai/stability/e72ec3d7-7364-46f2-a377-7c09ef3c0c55.png'
    },
    {
      title: 'Yoga',
      date: 'Wed, Jul 21, 10:00 AM',
      location: 'Alzheimer\'s Association, 123 Main St.',
      imageUrl: 'https://cdn.usegalileo.ai/stability/b0040266-fcea-4b9d-82b5-2691531e1cbb.png'
    },
    {
      title: 'Nursery Visits',
      date: 'Wed, Jul 21, 10:00 AM',
      location: 'Alzheimer\'s Association, 123 Main St.',
      imageUrl: 'https://cdn.usegalileo.ai/stability/16f44b94-ffe6-4279-966b-0ee90e91b326.png'
    },
    {
      title: 'Dementia support group',
      date: 'Wed, Jul 21, 10:00 AM',
      location: 'Alzheimer\'s Association, 123 Main St.',
      imageUrl: 'https://cdn.usegalileo.ai/stability/b0a30521-938b-4d48-ab9c-285e6063ebbf.png'
    }
  ];
}


