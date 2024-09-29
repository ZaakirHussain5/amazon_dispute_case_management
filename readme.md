# Amazon Seller Return Dispute Management App

## Overview

This application is designed to help Amazon sellers manage and dispute return charges efficiently. It allows users to input order and return data, create and track dispute cases linked to returns, and resolve disputes through a streamlined process. The app is built with Django, containerized using Docker, and integrated with PostgreSQL for data storage. Dynamic content loading is achieved through HTMX, allowing for a smooth user experience without full page reloads.

## Features

- **Order Data Input**: Sellers can input and manage Amazon order details, including order ID, item name, customer details, and order date.
- **Return Data Input**: Input Amazon return details such as order ID, return reason, and return tracking information.
- **Dispute Case Management**: Users can create and track dispute cases with links to return details, status updates, and resolution tracking. Dispute cases are created through a modal and updated dynamically using HTMX.
- **Dynamic Updates**: The application uses HTMX for asynchronous updates, making the user interface responsive and eliminating full page reloads.
  
## Project Architecture

The application is divided into several key components:
- **Backend**: Built with Django, handling orders, returns, and disputes data management.
- **Frontend**: Integrated with HTMX for smooth asynchronous content loading and Tailwind CSS for UI styling.
- **Database**: PostgreSQL is used to store orders, returns, and dispute data.
- **Containerization**: The entire application is containerized using Docker for easy deployment.

## Getting Started

### Prerequisites
Ensure you have the following installed on your system:
- Docker
- Docker Compose
- Python 3.10+
- PostgreSQL

### Installation

Follow these steps to get the app running locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/amazon-dispute-management.git
   cd amazon-dispute-management
   ```

2. Create an `.env` file with the following environment variables:
   ```bash
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=postgres://your_user:your_password@localhost:5432/your_db
   ```

3. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ```

4. Apply database migrations:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. Create a superuser to access the admin panel:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

6. Access the app at `http://localhost:8000`.

### Usage

- **Order Management**: Go to the "Orders" section to input and manage Amazon order details.
- **Return Management**: Navigate to the "Returns" section to input return details.
- **Dispute Case Management**: Use the "Dispute Cases" section to create, view, and track disputes. New cases are created through a modal, and the list updates dynamically using HTMX.

## Database Schema

The database schema is designed to maintain appropriate relationships between orders, returns, and disputes:

- **Order**: Stores details of Amazon orders (`order_id`, `item_name`, `customer_details`, `order_date`).
- **Return**: Stores return information linked to orders (`order_id`, `return_reason`, `return_tracking`).
- **Dispute**: Manages disputes linked to returns (`dispute_reason`, `status`, `resolution_date`).

PostgreSQL is used for efficient storage and retrieval of this data.

## Technical Details

- **Dynamic Content Loading**: HTMX is used to asynchronously load and update dispute data without requiring full page reloads.
- **Containerization**: The application is containerized using Docker for consistent development and deployment environments.
- **Tailwind CSS**: Tailwind CSS is integrated for fast, responsive UI development.

## Conclusion

This project provides a complete solution for Amazon sellers to manage and dispute return charges efficiently. The combination of Django, Docker, PostgreSQL, HTMX, and Tailwind CSS ensures a scalable, maintainable, and user-friendly application.