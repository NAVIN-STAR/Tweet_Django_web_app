# Tweetit

This is a Django-based web application that includes user authentication, tweet creation, and search functionality.

## Features

- User Registration and Login
- User Logout
- Tweet Creation
- Search Functionality

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```sh
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```sh
        source venv/bin/activate
        ```

4. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

5. **Apply migrations:**

    ```sh
    python manage.py migrate
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

## Usage

1. **Register a new user:**

    Navigate to `/register` and fill out the registration form.

2. **Login:**

    Navigate to `/login` and enter your credentials.

3. **Logout:**

    Click the "Logout" link in the navigation bar.

4. **Create a Tweet:**

    Navigate to the tweet creation page and submit your tweet.

5. **Search:**

    Use the search bar in the navigation to search for tweets.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
