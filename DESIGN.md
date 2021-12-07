How you implemented project and why made design decisions

Tour underneath hood

# Foodie Design
Foodie is created with the Django web framework. We felt that Django was very similar to Flask but provided more scalability and functionality at the end of the day. We use vanilla Javascript for a portion of the project, including the asynchronous calls made when saving dishes. Bootstrap 5 is used for a clean, dynamic, and mobile friendly user interface. We first created various Django apps to organize the different functions of our project (account, core, dish, and resturant). We designed the databased schema in the models.py file under each respective app.

## Database
We used a sqlite3 database. Django provides a very easy way to implement this database into the project. By using this, we can easily share all of the data when demoing for people to download our project as it is all stored in a file located on the top of the project root.

## Settings
All settings are configured under the foodie/settings.py file. Coupled with environ we are able to pass enviornment variables to our project securely. 

## Static
We seperated the static by css, images, and js. Doing so allows us to keep a clean design where we can import specific items only when necessary on different pages.

## Templates
We have a base.html file that serves as the layout for other files. Every other html templates extends this through Django's jinja template language. We were also able to include other html blocks for a clean design, such as navbar, footer, and messages. We have an includes folder to reuse html elements like a dish card for rendering the dishes out uniformly.

## Account
Each user has a username, password, date joined, and a few permission booleans. We designed the various views and urls for the user.

