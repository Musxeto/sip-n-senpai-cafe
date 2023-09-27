# python-flask-cafe-web
A Cafe website I created as a project named "Sip &amp; Senpai"
Getting Started
To get this project up and running on your local machine, follow these steps:

Clone the repository to your local machine using git clone.
bash
Copy code
git clone https://github.com/your-username/restaurant-contact-form.git
Install the required dependencies. You can create a virtual environment to keep your dependencies isolated.
bash
Copy code
cd restaurant-contact-form
pip install -r requirements.txt
Configure the application by creating a config.json file in the project directory. You should specify the following parameters in the JSON file:
json
Copy code
{
    "params": {
        "local_server": "True",
        "local_uri": "your_local_database_uri",
        "prod_uri": "your_production_database_uri",
        "gmail-user": "your_gmail_username",
        "gmail-password": "your_gmail_password"
    }
}
local_server: Set it to "True" if you are running the app locally, and "False" for production.
local_uri: Specify the local database URI.
prod_uri: Specify the production database URI.
gmail-user: Provide your Gmail email address for sending emails.
gmail-password: Provide your Gmail password (for application access).
Run the application.
bash
Copy code
python app.py
The application will be accessible at http://127.0.0.1:5000/.

Project Structure
The project structure is organized as follows:

app.py: The main Flask application script.
config.json: Configuration file for the application.
requirements.txt: List of required Python packages.
templates/: HTML templates for the web pages.
static/: Static files (e.g., CSS stylesheets, images).
README.md: This readme file.
Usage
Visit the website by going to http://127.0.0.1:5000/.

Explore the available pages:

Home: The main landing page.
Menu: View the restaurant's menu.
Contact: Submit a contact message using the contact form.
To submit a contact message:

Fill in your name, email, and message in the contact form.
Click the "Submit" button.
You will receive a confirmation message, and the restaurant will be notified of your message via email.
Contributing
Contributions to this project are welcome. Here are some ways you can contribute:

Report bugs or suggest improvements by opening an issue.
Fork the repository, make changes, and submit a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.
