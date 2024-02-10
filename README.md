# Sip & Senpai - Cafe Website

## Getting Started

To get this project up and running on your local machine, follow these steps:

1. Clone the repository to your local machine using `git clone`.
    ```bash
    git clone https://github.com/Musxeto/sip-n-senpai-cafe
    ```

2. Install the required dependencies.
    ```bash
    cd sip-n-senpai-cafe
    ```

3. Configure the application by creating a `config.json` file in the project directory. Specify the following parameters in the JSON file:
    ```json
    {
        "params": {
            "local_server": "True",
            "local_uri": "your_local_database_uri",
            "prod_uri": "your_production_database_uri",
            "gmail-user": "your_gmail_username",
            "gmail-password": "your_gmail_password"
        }
    }
    ```
   - `local_server`: Set it to "True" if you are running the app locally, and "False" for production.
   - `local_uri`: Specify the local database URI.
   - `prod_uri`: Specify the production database URI.
   - `gmail-user`: Provide your Gmail email address for sending emails.
   - `gmail-password`: Provide your Gmail password (for application access).

4. Run the application.
    ```bash
    python main.py
    ```

   The application will be accessible at http://127.0.0.1:5000/.

## Project Structure

- `app.py`: The main Flask application script.
- `config.json`: Configuration file for the application.
- `requirements.txt`: List of required Python packages.
- `templates/`: HTML templates for the web pages.
- `static/`: Static files (e.g., CSS stylesheets, images).
- `README.md`: This readme file.

## Usage

Visit the website by going to http://127.0.0.1:5000/.

Explore the available pages:
- **Home**: The main landing page.
- **Menu**: View the restaurant's menu.
- **Contact**: Submit a contact message using the contact form.

To submit a contact message:

1. Fill in your name, email, and message in the contact form.
2. Click the "Submit" button.
3. You will receive a confirmation message, and the restaurant will be notified of your message via email.

## Contributing

Contributions to this project are welcome. Here are some ways you can contribute:

- Report bugs or suggest improvements by opening an issue.
- Fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
