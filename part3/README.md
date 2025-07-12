🏠 HBnB Project - Part 3: Enhanced Backend with Authentication and Database Integration
Welcome to Part 3 of the HBnB Project!
In this phase, you’ll enhance the backend by introducing user authentication, authorization, and database integration. You’ll move from in-memory storage to SQLAlchemy + SQLite for development and prepare for MySQL in production, making your application secure, persistent, and production-ready.

📌 Project Objectives
Authentication & Authorization

Implement JWT-based authentication using Flask-JWT-Extended

Add role-based access control with an is_admin attribute to secure admin-specific endpoints

Database Integration

Replace in-memory storage with SQLite for development

Use SQLAlchemy as the ORM

Configure MySQL (or other RDBMS) for production

CRUD Operations with Persistence

Refactor all CRUD operations to interact with the database

Database Design & Visualization

Design the database schema and visualize it with mermaid.js

Ensure relationships between Users, Places, Reviews, and Amenities are well-defined

Data Consistency & Validation

Implement robust data validation and enforce constraints in your models

🎯 Learning Outcomes
By the end of Part 3, you will be able to:

✅ Secure your API with JWT authentication
✅ Manage user sessions and restrict access based on roles
✅ Replace in-memory storage with a persistent SQL database
✅ Map entities and relationships using SQLAlchemy ORM
✅ Design and visualize a real-world relational database schema
✅ Build a backend that is secure, scalable, and production-ready

🗂️ Project Context
In previous parts, you used in-memory storage for prototyping. In Part 3, you’ll switch to SQLite for local development and prepare your system for MySQL in production — giving you hands-on experience with real-world database systems.

You’ll also introduce JWT-based authentication to secure your API, so only authorized users can access or modify data. With role-based access control, you’ll enforce admin-only operations and protect critical endpoints.

🔗 Resources
JWT Authentication: Flask-JWT-Extended Docs

SQLAlchemy ORM: SQLAlchemy Docs

SQLite: SQLite Docs

Flask: Flask Docs

Mermaid.js for ER Diagrams: Mermaid.js Docs

🏗️ Project Structure
Here’s a breakdown of the tasks for Part 3:

Modify User Model

Store passwords securely with bcrypt

Update registration logic

Implement JWT Authentication

Protect endpoints with JWT tokens

Implement Role-Based Authorization

Restrict access for admin-only actions using is_admin

SQLite Database Integration

Transition from in-memory to SQLite for persistence

Map Entities with SQLAlchemy

Define and relate Users, Places, Reviews, and Amenities

Prepare for Production

Configure MySQL for deployment environments

Database Design & Visualization

Use mermaid.js to create ER diagrams for your schema

✅ Final Outcome
By the end of this phase, you’ll have:

A secure, authenticated backend with JWT and role-based access

A persistent database for reliable storage using SQLAlchemy and SQLite (and MySQL for production)

Well-structured, validated models ensuring data integrity

A clear ER diagram visualizing your entire database schema

You’ll be well on your way to deploying a robust, scalable web application that follows industry-standard practices! 🚀