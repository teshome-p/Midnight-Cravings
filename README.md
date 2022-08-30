# Midnight Cravings

## A fake restaurant's online menu created using HTML, CSS, Javascript, Python, and Flask.

## Register
The user starts at the register page. They can enter a username, email, and password to create an account on the site. If the user tries to register with a username/email that has already been taken, they will be redirected to the login page so they can log in to that account, and also be allowed to try creating an account again. If they successfully create a new account, they're automatically logged in are redirected straight to the home page of the site.

## Login
The user can choose to go to the login page if they already have an account made. There, they can enter their password along with either their username or email. If the password is incorrect, they can try again, and if the username or email doesn't exist, they will be directed to the register page. If they successfully login, they are redirected to the home page of the site.

## Home 
Once the user is at the home page, there will be a navigation bar at the top that allows the user to sign out and login again, to view the menu, and to view their cart. There also is a rotating carousel of images of the food thats on the menu. This page also contains the logo of the restaurant and information about the restaurant.

## Menu
From the home page, the user can go to the menu page to see the options available on the menu. The menu is split into different sections for each category of food. Each menu item has an image, a listed price, and an "Add to Cart" button. Once the user adds everything they want to buy to the cart, they can click a button at the bottom to take them to the cart page so they can confirm what they selected.

## Cart
After being redirected from the menu page to the cart page, a list of the user's selected items is displayed to the user, along with the total price. There is a button there for the user to confirm their order, which completes the whole order process.

## How to Run
In order to run the program, run the account.py file. You start at the register page, so you can either use Flask to start the application, or manually open the register.html file from the templates folder.
