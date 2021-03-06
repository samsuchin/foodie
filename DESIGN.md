# Foodie Design
Foodie is created with the Django web framework. Django is very similar to Flask but provides more scalability and functionality. We use vanilla Javascript on the frontend, such as for asynchronous calls made when saving dishes. Bootstrap 5 is used for a clean, dynamic, and mobile friendly user interface. We first created various Django apps to organize the different functions of our project (account, core, dish, explore, and resturant). We designed the database schema in the models.py file under each respective app.

## Database
We used a sqlite3 database. Django provides a very easy way to implement this database into the project. By using this, we can easily share all of the data when demoing for people to download our project as it is all stored in a file located on the top of the project root.

### Account
Each account stores information used to login (username, password) and basic permissions (is_staff, is_active) as well as when a user was created.

### Resturant
Each resturant has a name, cuisine type, and city location. These are used to essentailly categorize the dishes.

### Dish
Dishes are the core of the website. They store the most information. Each dish has an image, name, rating, and optional information like the price and a written review. Each dish is foriegn keyed to a resturant.

### Save
By creating a save table we can record what user saved a dish and what dish through two foriegn keys. We also store when this was created by ordering by purposes.

## Settings
All settings are configured under the foodie/settings.py file. We configured a custom User model and a static, media, and templates folder.

## Static
We seperated the static by css, images, and js. Doing so allows us to keep a clean design where we can import specific items only when necessary on different pages.

## Templates
We have a base.html file that serves as the layout for other files. Every other html templates extends this through Django's jinja template language. We were also able to include other html blocks for a clean design, such as navbar, footer, and messages. We have an includes folder to reuse html elements like a dish card for rendering the dishes out uniformly.

## Save
The save is an important more complex feature. It uses vanilla JS fetch calls to make a POST to the backend and return a JsonResponse to the frontend asyncronously. Based off if a like was created or not we render out different looks for the save button by updating its class and innerHTML. 