# 🏙️ UrbanNestBasic — Real Estate Web Application (Flask)

UrbanNestBasic is a functionality-focused real estate web application built using Flask.
This repository represents the initial and foundational stage of the UrbanNest project, concentrating on backend development, data modeling, authentication, and real-world CRUD workflows.

⚠️ UI/UX in this project is intentionally basic.
The goal is to demonstrate Flask backend fundamentals, not frontend polish.

## 1️⃣ Project Objective

The primary objective of this project is to build a working real estate backend system that helps in understanding:

Flask application structure

SQLAlchemy ORM and relationships

Authentication & authorization

Role-based access control

Property CRUD workflows

Image uploads and file handling

Filtering and search logic

Admin moderation concepts

This project serves as a learning-first and backend-reference project.

## 2️⃣ Core Functional Features

User Registration & Login (Flask-Login)

User Profile Management

Role-Based Access (user / admin)

Property Listing (Rent / Sale)

Add / Edit / Delete Property (Owner & Admin)

Multiple Property Image Upload

Property Detail Page

Admin Property Verification Flow

Search & Filter:

City

Property Type

Rent / Sale

Price Range

SQLite database with SQLAlchemy ORM

## 3️⃣ Technology Stack

Backend: Python, Flask

Frontend: HTML, Jinja2 (Basic UI)

Database: SQLite

ORM: SQLAlchemy

Authentication: Flask-Login

Forms & Validation: Flask-WTF

Static Assets: CSS, JavaScript

File Uploads: Werkzeug

Deployment (Advanced Version): Render

## 4️⃣ Project Evolution (Important)

This repository (UrbanNestBasic) is the initial stage of a larger project.

## ✅ Purpose of This Repository

Learn Flask backend from scratch

Understand data flow and routing

Practice real-world CRUD logic

## 🚀 Advanced Version (Modern UI + Live Deployment)

I later evolved this project into a fully redesigned, modern UI/UX real estate platform, deployed live using Render.

### 👉 Advanced GitHub Repository (Modern Version):
🔗 https://github.com/sunilprajapati832/UrbanNest_Flask

### 👉 Live Website (Render Deployment):
🌐 https://urbannest-m1ix.onrender.com/

If you are interested in modern UI, better UX, production-ready structure, and live deployment, please refer to the advanced repository above.

## 5️⃣ Project Folder Structure (Professional & Actual)

```text
UrbanNestBasic/
│
├── app/
│   ├── __init__.py          # App factory & extensions
│   ├── models.py            # Database models
│   ├── forms.py             # Flask-WTF forms
│   │
│   ├── routes/
│   │   ├── auth.py          # Authentication routes
│   │   ├── main.py          # Home & public routes
│   │   ├── profile.py       # User profile management
│   │   └── property.py      # Property CRUD & filters
│   │
│   ├── templates/           # Jinja2 HTML templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── profile.html
│   │   ├── edit_profile.html
│   │   ├── property_list.html
│   │   ├── property_detail.html
│   │   ├── add_property.html
│   │   ├── update_property.html
│   │   ├── view_property.html
│   │   └── unverified_properties.html
│   │
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── location.js
│   │   ├── images/
│   │   │   └── logo.png
│   │   ├── profile_pics/
│   │   │   └── default.png
│   │   └── uploads/         # Property images
│   │
│   └── __pycache__/
│
├── instance/
│   └── urbannest.db         # SQLite database
│
├── config.py                # App configuration
├── run.py                   # Application entry point
├── requirements.txt         # Dependencies
└── README.md                # Documentation
```

## ✅ Who Should Use This Project?

Flask beginners learning backend fundamentals

Developers understanding real-world CRUD systems

Students practicing SQLAlchemy relationships

Backend-focused portfolio projects

Reference for building scalable Flask apps

## 📌 Final Note

This repository is not abandoned — it is the foundation of the advanced UrbanNest project.

For:

## ✅ Clean backend logic → Use this repo

## 🚀 Modern UI & live product → Visit the advanced repo

Use as a reference for backend structure

Ideal for beginners and intermediate learners
