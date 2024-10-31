# Askify : An  Automatic Question Answer Generator

Askify is a web application that generates questions and answers from a given paragraph using natural language processing techniques. This project leverages Flask for the backend and provides a user-friendly interface for generating questions based on user input.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Input a Paragraph**: Users can enter a paragraph from which questions will be generated.
- **Customizable Question Count**: Users can specify the number of questions to generate (up to 5).
- **Dark Mode**: Users can toggle between light and dark mode for a better user experience.
- **Responsive Design**: The application is designed to be responsive and works well on various devices.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **HTML/CSS**: For the frontend interface.
- **JavaScript**: For dynamic interactions on the client side.
- **AJAX**: For asynchronous communication between the client and server.

## Installation

Follow these steps to set up and run the project on your local machine:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/askify.git
   cd askify

2. **Set Up a Virtual Environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Required Packages: Install the required Python packages using pip**:
   ```bash
   pip install Flask

## Usage

1. **Run the Application: Start the Flask development server by executing the following command**:
   ```bash
   python app.py

2. **Access the Application: Open your web browser and go to http://127.0.0.1:5000 (may differ after run the app.py) to view the application**.

3. Generate Questions:
  - Enter a paragraph in the provided text area.
  - Specify the number of questions to generate (1-5).
  - Click the "Generate Questions and Answers" button to receive your generated questions and answers.

## Project Structure
```graphql
askify/
│
├── app.py                   # Main Flask application file
├── templates/               # Directory for HTML templates
│   ├── index.html           # Main page of the application
│   ├── privacy_policy.html   # Privacy Policy page
│   └── terms.html           # Terms of Service page
│
├── static/                  # Directory for static files
│   ├── css/                 # Directory for CSS files
│   │   └── style.css        # Main stylesheet
│   └── js/                  # Directory for JavaScript files
│       └── script.js        # Main JavaScript file
│
└── README.md                # Project documentation
```

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request.
  - Fork the repository.
  - Create a new branch (git checkout -b feature/YourFeature).
  - Make your changes and commit them (git commit -m 'Add new feature').
  - Push to the branch (git push origin feature/YourFeature).
  - Open a pull request.
    
## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Here’s a video demonstration of the project:

![Demo GIF](assets/Demo.gif)
