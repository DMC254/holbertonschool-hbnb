Part 4 - Simple Web Client
This phase focuses on the front-end development of your application using HTML5, CSS3, and JavaScript ES6. You'll build an interactive user interface that communicates seamlessly with the back-end services developed in previous phases.

🌟 Objectives
Develop a user-friendly interface following the provided design specifications.

Implement client-side functionality to interact with the back-end API.

Ensure secure and efficient data handling using JavaScript.

Apply modern web development practices to create a dynamic, responsive web application.

🎯 Learning Goals
Apply HTML5, CSS3, and JavaScript ES6 in a real-world project.

Use AJAX or the Fetch API to interact with back-end services.

Implement authentication mechanisms and manage user sessions using JWT.

Enhance user experience with client-side scripting—no full-page reloads.

📋 Tasks Breakdown
🖌️ 1. Design
Complete provided HTML and CSS to match design specifications.

Create the following pages:

Login

List of Places

Place Details

Add Review

🔐 2. Login
Implement login functionality using the back-end API.

Store the JWT token returned by the API in a cookie for session management.

📍 3. List of Places
Build the main page to display a list of all places.

Fetch data from the API.

Implement client-side filtering based on country selection.

Redirect to the login page if the user is not authenticated.

🧭 4. Place Details
Create a detailed view page for individual places.

Fetch place details using the place's unique ID.

Display a review form only if the user is authenticated.

✍️ 5. Add Review
Implement a form that allows users to add reviews to a place.

Ensure only authenticated users can access this feature.

Redirect unauthenticated users to the index page.

⚠️ CORS Notice
When testing your front-end against your API, you may encounter Cross-Origin Resource Sharing (CORS) errors.
To resolve this, you'll need to update your Flask API to allow requests from your web client.

📖 Read this article for a deeper understanding of CORS and how to configure it in Flask.

✅ Tech Stack
Frontend: HTML5, CSS3, JavaScript (ES6)

Backend: Flask (from previous parts)

Authentication: JWT-based session management

Data Fetching: Fetch API / AJAX