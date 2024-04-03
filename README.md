# django_task_app


This is a Django web application designed to manage a simple task list. Users can register, log in, and log out to manage their tasks effectively. The application provides features such as adding, editing, and deleting tasks, along with the ability to filter tasks based on their completion status.

## Features
1. **Task Model**: The application includes a Django model for tasks with attributes such as title, description, due date, and completion status.

2. **Views and Templates**: Implementations for views and templates are provided to list all tasks, view the details of a specific task, and add/edit tasks.

3. **User Authentication**: User authentication is integrated, ensuring that only authenticated users can access the task management functionalities. Users can register, log in, and log out securely.

4. **Task Filtering**: A feature is implemented to filter tasks based on their completion status, providing users with better organization and management options.

## Installation


*** create a separate directory for your Django project,
*** create a Python virtual environment, activate it, 
*** and then install Django inside that virtual environment, you can follow these steps:

1. **Create a Directory for Your Project**: 
    ```
    mkdir my_django_project
    cd my_django_project
    ```

2. **Create a Python Virtual Environment**: Inside your project directory, create a Python virtual environment using `venv` or `virtualenv`. For example, using `venv`:

    ```
    python -m venv env
    ```

3. **Activate the Virtual Environment**: Activate the virtual environment. The method for activating varies depending on your operating system. For example, on macOS/Linux:

    ```
    source env/bin/activate
    ```

   On Windows:

    ```
    .\env\Scripts\activate
    ```

   After activating the virtual environment, you should see `(env)` appear at the beginning of your terminal prompt, indicating that the virtual environment is active.

4. **Install Django**: With the virtual environment activated, you can now install Django using pip:

    ```
    pip install django
    ```

   This command will install the latest version of Django inside your virtual environment.

5. **Verify Installation**: You can verify that Django was installed correctly by running:

    ```
    python -m django --version
    ```

   If Django was installed successfully, you'll see the version number displayed in the terminal.


2. Clone the repository:
   ```
   git clone https://github.com/assiaatt/django_task_app.git
   ```

   

3. Apply migrations:
   ```
   cd django_task_app/skaalab/task_manager
   python manage.py migrate
   ```

4. Run the development server:
   ```
   python manage.py runserver
   ```

5. Access the application at `http://localhost:8000/` in your web browser.

## Usage
1. Register an account or log in if you already have one.
2. Once logged in, you can view your tasks, add new tasks, edit existing tasks, and mark tasks as completed.(only yours)
3. Use the task filtering feature to organize your tasks based on their completion status.

