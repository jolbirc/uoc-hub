# UOCHUB
15-08-26

---

A web application to help university students navigate life at the University of Chester. Application includes study space bookings, wellbeing support, the campus directory, and an academic calendar, all in one hub. 

---
## Overview
Built as a coursework MVP (CO5992) exploring building a single hub for reducing the number of separate apps/portals for students to use. Focused on four core segments:
  - **Study spaces**. Search and book an available study room by date/time
  - **Wellbeing**. A simple contact form to reach support
  - **Campus Directory**. Browse UoC campus locations
  - **Academic Calendar**. MVP skeleton; view-only at this stage.

---
## Stack 
  - **Backend**: Python w/ Django
  - **DB**: SQLite
  - **Deploy**: Nginx + Gunicorn

---
## User Guide

### Home
Landing dashboard after login, with tiles linking to each feature area.

### Study Spaces
1. Navigate to study spaces from the nav.
2. Select a date/time from the drop downs
3. Click 'search' to see available rooms
4. Click 'book' on a listed room to "reserve" it

### Wellbeing
1. Enter a name and message
2. Click 'send' to submit a request for support (currently a stub for MVP)

### Campus Directory
Browse a list of campus locations, with each entry linking to the official page for that building, for further info.

### Academic Calendar
View the current months calendar **only** at the minute. MVP scope, semi-placeholder.

### Campus Map
Leaflet/OS Street Map map implemented to view the campus and all the relevant locations pinpointed. 

### Profile
View/manage account details - requires login.

### Authentication
Most pages require login. A test account has been set up for demo purposes:
  - Username: test_user
  - Password: testpass123

---

Josh Birch
