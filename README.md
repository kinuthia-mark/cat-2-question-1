# E-Commerce Django Project

This project is a simple e-commerce system built with Django. It includes models for `Customer` and `Order`, demonstrating a one-to-many relationship where a customer can place multiple orders.


## Features

1. **Customer Management**
   - Add and manage customer records.
   - Each customer is identified by their name and email address.

2. **Order Management**
   - Record and view orders placed by customers.
   - Each order includes the customer, order date, and total amount.

3. **Admin Panel**
   - A user-friendly admin interface for managing customers and orders.


## Superuser Credentials

To access the admin panel, use the following credentials:

- **Username**: `strathmore`
- **Email**: `kinuthia.mark@strathmore.edu`
- **Password**: `5trathm0re`



### Setting up the Environment and Running the Project

Follow these steps to set up the project environment and run the application locally:


#### 1. **Install Python**
- Make sure you have installed on your machine.
- Check the Python version:
  python --version

#### 2. **Clone the Repository**
- Clone the project repository from GitHub to your local machine:
  git clone <repository-url>
  cd ecommerce
  ```


#### 3. **Set Up a Virtual Environment**
- Create a virtual environment to manage dependencies for the project:
  python -m venv venv

- Activate the virtual environment:

    venv\Scripts\activate


#### 4. **Install Required Dependencies**
- Install Django and any other dependencies:
  pip install django

#### 5. **Set Up the Database**
- Apply the database migrations to set up the database schema:
  python manage.py makemigrations
  python manage.py migrate



#### 6. **Run the Development Server**
- Start the Django development server:

  python manage.py runserver
 
- Open your browser and navigate to:

  http://127.0.0.1:8000/

  This will display the default Django welcome page.


#### 7. **Access the Admin Panel**
- Create a superuser if you haven’t already:
 
  python manage.py createsuperuser

  - Use the following details if required:
    - Username: `strathmore`
    - Email: `kinuthia.mark@strathmore.edu`
    - Password: `5trathm0re`

- Open the admin panel in your browser:
  
  http://127.0.0.1:8000/admin
  
- Log in using the superuser credentials.


### Notes:
- If you encounter any issues with dependencies, ensure your virtual environment is active and try re-installing the required packages.
- To stop the development server, press Ctrl+C in the terminal.
