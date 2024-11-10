<h1> Tech News Publication Website using Django, Tailwind CSS, and Flowbite </h1>


## Introduction

Welcome to the Django Blog project documentation. This project is a feature-rich Django-based blog website that allows users to create, manage, and interact with blog posts, with a focus on tech-related content. It provides a user-friendly interface with Flowbite for responsive and modern UI components for bloggers and readers alike. Whether you're a new Django developer or an end user, this documentation will help you get started with the project and explore its features.


## Getting Started

### Installation

Before you begin, make sure you have Python and Django installed on your system. To install Django, you can use pip:

```bash
pip install Django
```

### Project Setup

1. Clone the project repository from GitHub:

   ```bash
   git clone https://github.com/iamTANMOY7/Digital-Tech-Publication-Website.git
   ```

2. Navigate to the project directory:

   ```bash
   cd blog
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv env
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     .\env\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source env/bin/activate
     ```

5. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Create a new terminal and Install Tailwind/Flowbite
  
   ```bash
   npx tailwindcss init
   npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch
   ```
      
7. Run the development server:

   ```bash
   python manage.py runserver
   ``` 
   
8.  Open your web browser and visit [http://localhost:8000/demo](http://localhost:8000/demo) to access the modern UI Django Blog project.

<hr>

<h2>Project Overview</h2>

## Features 

- **Admin Panel** :- Built-in Django Admin for managing blog posts and users.
- **Manage Blog** :– In this feature includes the CRUD operation in a blog or content you create like adding, editing and deleting content of the blog.
- **Login System** :- In this feature the admin can login to the system and manage all the feature of the system.
- **Media** :- In this method which you can found all the media that you are upload in the system.
- **Template** :- In this method which is the design of the system that consist of HTML,CSS and JavaScript.

## Usage

### User Registration and Authentication

- To create an account, click the "Register" link in the navigation menu.
- To log in, click the "Login" link in the navigation menu.

![ ](https://github.com/user-attachments/assets/449d56a9-0952-4c99-81c9-3ccebf3dd67b)

### Blog Management

- On the home page, you can view the latest blog posts.
- Navigate through multiple pages of blog posts using pagination.

![ ](https://github.com/user-attachments/assets/36efba9c-31b7-41e5-91fb-4faf31322b98)

###  Responsive Design & Dark Mode Toggle

- Uses Flowbite and Tailwind CSS for a clean, responsive layout.
- User-friendly light/dark mode switch.

![ ](https://github.com/user-attachments/assets/44388287-06e4-4e73-a898-ae378494966f)

### Search

- Utilize the search form in the navigation menu to search for specific blog posts based on title, content.

![ ](https://github.com/user-attachments/assets/1bb20779-176e-43bd-9c59-5b7c3ba62358)


