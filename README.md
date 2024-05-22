# Traxion Project

The Traxion project aims to manage service orders and maintenance parts for vehicles.

## Introduction

Traxion is a Django-based project designed to facilitate the management of service orders and maintenance parts for vehicles. It provides a RESTful API for creating, retrieving, updating, and deleting service orders and maintenance parts.

## Features

- CRUD operations for service orders and maintenance parts.
- Integration with Django admin for easy management.
- API documentation using Swagger UI.

## Installation

1. Clone the repository and run container:

   ```bash
   git clone https://github.com/your/repository.git


   cd traxion-project

   docker-compose build

   docker-compose up

   ```

2. Run integration test and unit test:

   ```bash
   docker exec -it traxion sh
   python manage.py test

   ```
Access the application at http://localhost:8000.
Usage
Access the API documentation:
Swagger UI: http://localhost:8000/swagger/
OpenAPI JSON: http://localhost:8000/swagger.json
Use the provided endpoints to interact with the application data.
API Endpoints
Vehicles:
	GET /vehicles/
	POST /vehicles/
	GET /vehicles/{id}/
	PUT /vehicles/{id}/
	DELETE /vehicles/{id}/
Service Orders:
	GET /service-orders/
	POST /service-orders/
	GET /service-orders/{id}/
	PUT /service-orders/{id}/
	DELETE /service-orders/{id}/
Maintenance Parts:
	GET /maintenance-parts/
	POST /maintenance-parts/
	GET /maintenance-parts/{id}/
	PUT /maintenance-parts/{id}/
	DELETE /maintenance-parts/{id}/