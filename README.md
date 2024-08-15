# Django Todo List Project

![To-Do List Page](Screenshot%202024-08-15%20131324.png)
*Description: The main page showing all to-do items with options to create, view, edit, or delete tasks.*

## Description

The **Django Todo List Project** is a web application built using Django, designed to help users manage their daily tasks. It offers functionalities to create, view, update, and delete to-do items, providing a clean and user-friendly interface for task management.

## Features

- **Task Management**: Create, view, update, and delete todo items.
- **Admin Interface**: Manage tasks through Django’s built-in admin panel.
- **User Interface**: Simple and intuitive design for managing tasks.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS
- **Database**: SQLite (default), configurable to other databases like MySQL

### 1. Install Python and Django

Ensure you have Python and Django installed on your system. If not, follow these steps:

- **Python**: Install Python from [python.org](https://www.python.org/downloads/).
- **Django**: Install Django using pip:
  
## Setup Instructions

To run this project locally:

1. **Clone the repository**:

   ```bash
   git clone <repository_url>
   cd library_management

2. **Install dependencies (assuming you have Python and Django installed):**

   ```bash
   pip install -r requirements.txt

3. **Apply migrations to set up the database:**

   ```bash
   python manage.py migrate

4. **Run the development server:**

   ```bash
   python manage.py runserver

5. **Access the application:**

   Open a web browser and go to [http://localhost:8000](http://localhost:8000) to view the Library Management System.

# My Django Project
## Directory Structure

- `todoproject/`                 <- Django project root
  - `settings.py`                <- Django settings file
  - `urls.py`                    <- Django root URL configuration
  - `wsgi.py`                    <- WSGI configuration for deployment

- `todo/`                        <- Django app directory
  - `models.py`                  <- Django models for database
  - `views.py`                   <- Django views for handling requests
  - `urls.py`                    <- URL routing for the todo app
  - `templates/`                 <- Directory for HTML templates
    - `todo_list.html`           <- Template for the to-do list page
    - `todo_detail.html`         <- Template for viewing individual to-do items
    - `todo_form.html`           <- Template for creating and editing to-do items
    - `todo_confirm_delete.html` <- Template for confirming to-do item deletion
  - `static/`                    <- Directory for static files
    - `styles.css`               <- CSS stylesheet

- `manage.py`                    <- Django's command-line utility for management tasks

## Usage

### Managing Tasks

1. **Navigate to the Home Page**: Visit [http://127.0.0.1:8000](http://127.0.0.1:8000).

2. **View Task List**: The home page displays a list of all todo items. Click on an item to view its details.

3. **Create a New Task**: Click on "Add New To-Do" to create a new task.

4. **Edit Existing Task**: Click on an item and then click "Edit" to modify its details.

5. **Delete a Task**: Click on an item and then click "Delete" to remove it.

### Example

- **Create a New Task**: Enter the title and description, then click "Save".
- **Edit Task**: Change the details and click "Save".
- **Delete Task**: Confirm deletion by clicking "Yes, delete".

## Project Screenshots

![To-Do List Page](Screenshot%202024-08-15%20131324.png)
*Description: The main page showing all to-do items with options to create, view, edit, or delete tasks.*

![To-Do Detail Page](Screenshot%202024-08-15%20131426.png)
*Description: The detail view of a selected to-do item including its title, description, and completion status.*

![To-Do Create/Edit Form](Screenshot%202024-08-15%20131435.png)
*Description: The form used to create or edit to-do items.*

![To-Do Delete Confirmation](Screenshot%202024-08-15%20131454.png)
*Description: The confirmation page for deleting a to-do item.*

![Additional View](Screenshot%202024-08-15%20131507.png)
*Description: An additional view or feature of the application.*

## Key Files

- **todo/models.py**: Defines the TodoItem model.
- **todo/views.py**: Contains view functions for handling to-do item logic.
- **todo/urls.py**: Maps URLs to view functions in the todo app.
- **todo/templates/todo/todo_list.html**: Template for listing all to-do items.
- **todo/templates/todo/todo_detail.html**: Template for showing details of a to-do item.
- **todo/templates/todo/todo_form.html**: Template for creating and editing to-do items.
- **todo/templates/todo/todo_confirm_delete.html**: Template for confirming deletion of a to-do item.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

1. **Fork the repository**.
2. **Create a new branch** (`git checkout -b feature-branch`).
3. **Make your changes**.
4. **Commit your changes** (`git commit -m 'Add new feature'`).
5. **Push to the branch** (`git push origin feature-branch`).
6. **Open a pull request**.

## Credits

- **Developed by**: rajendraprasath and Open AI
- **Email**: [rajendraprasath307@gmail.com](mailto:rajendraprasath307@gmail.com)


### Dependencies

To install dependencies, use:

