# Foodie

[OUR VIDEO](https://www.youtube.com/watch?v=JjaYeO0H4Sk)

## Install and Configure
Download the repository manually or through git

`git clone https://github.com/samsuchin/foodie.git`

Move into the repository folder

`cd foodie`

Make sure python3 is installed on your computer. This can be installed [Here](https://www.python.org/downloads/).

It is advised to create a virtual environment and then install the requirements.txt libraries

`pip install -r requirements.txt`

Once everything is installed, run the following commands.

`python manage.py runserver`

The website is now live. An account can be created under signup.

## Documentation

Our website is a social media platform for restaurant food and can be used to find dishes, reviews, and restaurants in Harvard Square. The website currently includes 20 of our favorite restaurants, but it could be expanded in the future to include more restaurants in Cambridge and in other cities as well. The website features a home page, an explore page, a signup page, a login page, an account page, and a post page. 

On the home page, each user can browse different dishes that have been posted by other users. The user will always be taken to the homepage upon opening the website, logging in, or clicking the “Foodie” logo. Each dish features an image, an emoji rating, a title, a restaurant, a review, and a save feature. A user can toggle between dishes by clicking the left and right arrows on either side of the dish image. A user can click on the restaurant name to view the restaurant page or the username to view the user’s page. Although you can browse through the dishes on the home page without being logged in, you must be logged in in order to save dishes. 

On the explore page, each user can search for restaurants by the name, cuisine, or dish. Results of the filtered restaurants will show and users will be able to see a preview and quick emoji review of the last three dishes posted under this restaurant. By clicking “learn more,” the user can access the restaurant’s page that contains its address and all of its dishes.

On the sign up page, each user is prompted to enter a username, a password, and a password confirmation. The sign up page is designed to ensure that the user enters a unique username, the password is not too similar to the username, the password is not too common, the password contains at least 8 characters, and the two password fields match. On the login page, each user is prompted to enter their username and password. The login page is designed to ensure that the username exists, and the password is correct.

Once the user is logged in, they can post, save dishes, view their account, and logout. On the post page, a user can post a dish by adding an image file, a restaurant name, a dish name, a review, a five-scale rating, and a price. A user can save a dish by clicking the “save” button which will run an asynchronous call to the site and automatically update the frontend’s html without reloading the page. A user can delete a post they own by clicking the “delete” button. On the account page, a user can view all of the dishes they've posted as well as the dishes they’ve saved. A user can log out by clicking “logout” on the right side of the nav bar.
