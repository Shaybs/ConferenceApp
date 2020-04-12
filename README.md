# Conference Call Application

### Application Setup

To set up this application on an instance. Clone down the repository. Install git and docker. Deploy the application by running docker. Ensure that the VM's firewall allow access to port 80. The SQLALCHEMY_DATABASE_URI, USERNAME, PASSWORD, MYSQL_URL, MYSQL_DB, SECRET_KEY environment variables will have be added to your .bashrc and sourced. Also a database on your SQL instance will have to added manually. After which the tables can be added utilising the models.

### Challenge Overview

In this challenge I had to create an app that could create a Conference and then add attendees to it.

### How to use the Application

To use this application. Register as a user, log in and go to the conference page, add, edit or delete conferences. Go to the Attendees page to add, edit or delete attendees.

### Further Improvements and Future

There are many improvements that can be made to this application. For example, there could be more stringent policies for who can open or generate an account. The application could be further developed to have a microservices architecture. Further, AWS Lambda or Azure Functions could be used instead of flask applications to add, edit or delete entries in the SQL directory. Testing could be added. Jenkins integration along with an ansible playbook could be added. The application could be further developed to utilise Kubernetes allowing for automated scaling. Security could also be enhanced through the addition of dummy data to passwords before hashing and through the randomisation of the dummy data to ensure there are no patterns for the dummy data.