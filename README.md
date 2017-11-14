# User Profile with Django -- Treehouse Tech Degree Python Project #7
## Adam Cameron, 2017
---

## Project Description

"For this project, you’ll build a form that takes in details about a registered user and displays those details on a profile page. The profile page should only be visible once the user has logged in. The profile page should include first name, last name, email, date of birth, confirm email, short bio, and the option to upload an avatar.

You’ll also set up validation for email, date of birth and the biography. The Date of Birth validation should accept three date formats: YYYY-MM-DD, MM/DD/YYYY, or MM/DD/YY. The Email validation should check if the email addresses match and are in a valid format. The bio validation should check that the bio is 10 characters or longer and properly escapes HTML formatting.

You’ll also create a 'change password page' that updates the user’s password. This page will ask for current password, new password and confirm password. Set up validation which checks that the current password is valid, that the new password and confirm password fields match, and that the new password follows the following policy:

- must not be the same as the current password
- minimum password length of 14 characters.
- must use of both uppercase and lowercase letters
- must include of one or more numerical digits
- must include of special characters, such as @, #, $
- cannot contain the username or parts of the user’s full name, such as his first name."

## How to run the app

First you'll need to set up a virtual environment with the packages from requirements.txt.
After that, make and run your migrations to create the sqlite3 database.
You should then be able to run `python manage.py runserver` to start the server and use the app.

## Project Instructions

* Create a Django model for the user profile.
* Add routes to display a profile, edit a profile, and change the password.
* Create a "profile" view to display a user profile with the following fields: First Name, Last Name, Email, Date of Birth, Bio, and Avatar. Include a link to edit the profile.
* Create an "edit" view with the route "/profile/edit" that allows the user to edit the user profile with the following fields: First Name, Last Name, Email, Date of Birth, Confirm Email, Bio, and Avatar.
* Validate user input "Date of Birth" field: check for a proper date format (YYYY-MM-DD, MM/DD/YYYY, or MM/DD/YY)
* Validate user input "Email" field: check that the email addresses match and are in a valid format.
* Validate user input "Bio" field: check that the bio is 10 characters or longer and properly escapes HTML formatting.
* Add the ability to upload and save a user's avatar image.
* Create "change-password" view with the route "/profile/change_password" that allows the user to update their password using `User.set_password()` and then `User.save()`. Form fields will be: current password, new password, confirm password.
* Validate user input "Password" fields: check that the old password is correct using `User.check_password()` and the new password matches the confirm password field and follows the password policy detailed in the description above.
* Use CSS to style headings, font, and form.
* Make sure your coding style complies with PEP 8