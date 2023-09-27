# 21 MID Event Organiser

![AM I Responsive images](assets/readme/example.PNG)

### [Live Website](https://bar-match-bookings-site-929e26b7b02a.herokuapp.com/)

A community wesite to organise gaming events/times.  
The objective of this is to provide a simple site to try to organise gaming events among friends. These days it's difficult to get my gaming group together to play something as we all have resposibilities this is an attempt to make getting together easier.


## Table of Contents

1. [User Experience (UX)](#user-experience-ux)
    1. [Strategy](#strategy)
        1. [Project Goals](#project-goals)
        2. [User Goals](#user-goals)
    2. [Structure](#structure)
        1. [Database Model](#database-model)
        2. [Wireframes](#wireframe)
2. [Features](#features)
    1. [Features Left to Implement](#features-left-to-implement)

***


## User Experience (UX)

### Strategy

#### Project Goals

* The website contains simple colors for a modern and clean design.

* Responsive design to make the website accessible on different screen sizes.

* Structure is easy to understand and navigates effortlessly.

* Site users are able to register an account in order to interact with the content.

* Site users are able to post events and indicate if they would like to attand.


#### User Goals
GitHub projects was used as my project management tool to track user stories. Using a Kanban board helped to focus on specific tasks and track the project progress. I used lables on the stories to priority of the feature.

[Features/Planning Board](https://github.com/users/EMarnus/projects/4/views/1) 


### Structure


#### Database Model

The database model has been designed using [drawsql](https://drawsql.app/). The type of database being used for the is relational database being managed using [PostgreSQL](https://www.postgresql.org/).

![Data Model](assets/readme/datamodel.png)  

#### Wireframes

Page | Desktop Version | Mobile Version
--- | --- | ---
Index / User Logged Out | ![Desktop index / user logged out wireframe image](assets/readme/outindex.png) | ![Mobile index / user logged out wireframe image](assets/readme/outindexm.png)
Index / User Logged In | ![Desktop sign up wireframe image](assets/readme/inindex.png) | ![Mobile sign up wireframe image](assets/readme/inindexm.png)
Sign Up | ![Desktop log in wireframe image](assets/readme/register.png) | 
Profile | ![Desktop index / user logged in wireframe image](assets/readme/profile.png) | 

### Features 

- __The Nav Bar__

  - Featured at the top of the page, bracketed by the site name and catchfrase we have the nav links
  - If you're not logged in you see, A Home link that show all the events with some detals, the register link - lets you register and the Login link which lets you log in if you are already registered.  
    ![Logged out Nav](assets/readme/outnav.PNG)
  - If you are logged in you see, A Home link that show all the events with some detals, Add Events which lets you add events, and a User dropdown which lets you logout and view your profile(To be expanded)  
  ![Logged in Nav](assets/readme/innav.PNG)

- __Home Page body__

  - This section is the main focus of the website(for now). Here you see all the Events that have been posted by users with some detail.
  - As a logged in user you can view more details on the Events or if you posted the Event you can access the Edit and Delete functions from here.  
  ![Logged in Index](assets/readme/inindexbody.PNG)  

  - As a logged out user you can only see the Event panels.
  ![Logged out Index](assets/readme/outindexbody.PNG)

- __Event Details Page__  

- In the first section you can see all the details for the events.
![Details secion one](assets/readme/detialsone.PNG)

### Features Left to Implement

- Fleshed out Profile for users
- Ability for Users to see others Profiles
- Ability to message others
- Features left on Stretch

## Testing 

Ongoing testing on Chrome as features were added. Additional Testing was done desktop Edge, Firefox & Mobile Chrome. Manual testing was done following this checklist [Checklist](https://docs.google.com/spreadsheets/d/1UXtTze1940aCpoY0gpDi4OD64AhHgHELo6on6-MYtAA/edit?usp=sharing).

[Incognito Lighthouse](#)

### Validator Testing 

- HTML
    - [W3C validator](#)
- CSS
    - [(Jigsaw) validator](#)


### Unfixed Bugs
- Updating Events broke after adding previously submitted dates as default.  
- The desctiption on booking-submit is not dynamic depending on type selected.
- 


### Fixed Bugs
- When not logged it, colums do not display correctly on homepage, fixed with [Commit](https://github.com/EMarnus/PP4-Redo/commit/8f04d5038b0b07338a8e9da65b9a83187e89506f?diff=split)
- Pagination doesn't work, just keeps flowing down. [Commit](https://github.com/EMarnus/PP4-Redo/commit/34cf80bb00148e4965a48b059a2a1252377f4600)
- 


## Deployment

- The site was deployed using Heroku: 
  - In heroku Create a new App
  - In your new App go to settings and reveal Config Vars, add your variables from env.py as well as PORT: 8000
  - Make sure your repo contains a Procfile
  - Go to Deply, select GitHub as the Deployment method, Deploy Branch from Main.


## Credits 
- Can Sucullu - Mentor at Code Institute
- Codemy.com - [Django Wednesdays Playlist](https://bit.ly/35Xo9jD)
- CI's I think Therefore I Blog - Used project as a base template for my site
- Comment system built using  
[djangocentral.com](https://djangocentral.com/creating-comments-system-with-django/#building-comment-model)
[CodingEntrepreneurs ](https://www.youtube.com/watch?v=rKXVuG4axTg)
And help from Sean, Code Institute Tutor.

### Content 


### Media

- 
- 