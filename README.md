Recipe Generator App
This is a full-stack web application that generates recipes based on a specified food item and calorie count. The backend is built with Python and Flask, while the frontend is built with React.
Backend
The backend is a Flask application that uses the OpenAI API and Replicate API to generate recipes and images, respectively. Here are the main features:
OpenAI API Integration: The application uses the OpenAI API to generate recipes based on the provided food item, calorie count, and language.
Replicate API Integration: The application uses the Replicate API to generate an image of the specified food item.
Environment Variables: The application uses environment variables to store API keys and other sensitive information. You'll need to create a .env file and populate it with the required variables (see .env.example for reference).
Installation
Clone the repository: git clone []
Navigate to the backend directory: cd []
Install the required dependencies: pip install -r requirements.txt
Create a .env file and populate it with your API keys (see .env.example for reference)
Run the Flask app: python app.py
Frontend
The frontend is a React application that communicates with the Flask backend to generate recipes and display the results. You can find the source code for the frontend on GitHub:
You can also access the live version of the application at: https://your-app-url.com
