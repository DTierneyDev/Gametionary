# Gametionary

This project is an online dictionary for Game related words, abbreviations and phrases.

Using this site, you will be able to read the entries that have been entered into the database.
Add you own entries into the database. Edit entries that are in the database, and delete entries from the database.

You can also upvote entries that you find helpful or accurate.

The goals of this site are to:
- Allow users to easily share information on game related jargon.
- Allow users to easily find information on game related jargon.
- Allow users to upvote information that they find helpful.

## Demo

A demo can be viewed on Heroku [here](https://gametionary.herokuapp.com/).

## UX

My goal with the design of this site was to make it simple to navigate and use.
I've done this using an introduction on the main page, and making the layout easy to understand. Such as the buttons (edit, delete, upvote) on entries being highlighted and easy to find.

#### User Stories

1. Allow users to add entries to the database
2. Allow users to edit entries that are in the database
3. Allow users to delete entries from the database
4. Allow users to search the database for entries
5. Allow users to upvote helpful/accurate entries
6. Allow users to see the most upvoted entries
7. Allow users to see random entries from the database

#### Wireframe Mockups

Here are the wireframe mockups that I made before starting the project.

- [Index - Desktop](wireframes/index-desktop.png).
- [Index - Desktop - Menu Open](wireframes/index-desktop-menuopen.png).
- [Index - Tablet](wireframes/index-tablet.png).
- [Index - Mobile](wireframes/index-mobile.png).
- [Search - Desktop](wireframes/search-desktop.png).
- [Search - Tablet](wireframes/search-tablet.png).
- [Search - Mobile](wireframes/search-mobile.png).
- [A-Z - Desktop](wireframes/a-z-desktop.png).
- [A-Z - Tablet](wireframes/a-z-tablet.png).
- [A-Z - Mobile](wireframes/a-z-mobile.png).
- [Top Rated - Desktop](wireframes/top-rated-desktop.png).
- [Top Rated - Tablet](wireframes/top-rated-tablet.png).
- [Top Rated - Mobile](wireframes/top-rated-mobile.png).
- [Random - Desktop](wireframes/random-desktop.png).
- [Random - Tablet](wireframes/random-tablet.png).
- [Random - Mobile](wireframes/random-mobile.png).
- [Add Entry - Desktop](wireframes/add-entry-desktop.png).
- [Add Entry - Tablet](wireframes/add-entry-tablet.png).
- [Add Entry - Mobile](wireframes/add-entry-mobile.png).
- [Edit Entry - Desktop](wireframes/edit-entry-desktop.png).
- [Edit Entry - Tablet](wireframes/edit-entry-tablet.png).
- [Edit Entry - Mobile](wireframes/edit-entry-mobile.png).

## Features

Each page features a navigation bar with a brand-logo for quick access to the home page, a search bar, and a button to toggle the sidebar.

#### Index

This page features introduction text and buttons to the various pages.
It also features 2 random entries to give users an idea of what to expect, and get them interested.

#### Search

This page features a search bar and will show the database entries that contain your search.
If you were redirected to this page via the navbar then your search will be pre-entered.

#### A-Z

This page features a full A-Z list of the entries currently in the database.

#### Top Rated

This page features the 20 database entries with the most upvotes.

#### Random

This page features a random entry from the database.
It also features a button to change that entry to a different random entry from the database.

#### Add Entry/Edit Entry

These pages feature a form to enter the Name/Description of an entry.
The add page will load with a blank form. Whereas the edit page will load with the details of whichever entry you clicked edit on.
Once you'ce completed the form the submit button will add or edit the entry.

### Existing Features

- Search Function - This allows users to search the database for a particular definition.
- Add Entry - This allows users to Create new definitions in the database.
- A-Z List - This allows users to Read all of the definitions that are currently in the database.
- Edit Entry - This allows users to Update definitions that are currently in the database.
- Delete Entry - This allows users to Delete definitions from the database.

## Technologies Used

1. HTML
2. CSS
3. Bootstrap (4.3)
4. JQuery
5. Javascript
6. MongoDB
7. Flask
8. Python
9. Heroku

## Testing

1. Navbar - Search Form:
    1. Went to the "Index" page
    2. Tried to submit the empty form and confirmed that an error message about the required field appears.
    3. Tried to submit the form with all inputs and verify it submits the search term to the search page correctly.

2. Search Page - Search Form:
    1. Went to the "Search" page
    2. Tried to submit the empty form and confirmed that an error message about the required field appears.
    3. Tried to submit the form with all inputs and verify it submits the search term to the search page correctly.

3. Add Entry Page - Entry Form:
    1. Went to the "Add Entry" page
    2. Tried to submit the empty form and confirmed that an error message appears.
    3. Tried to submit the form with empty name and confirmed that an error message about the required fields appears.
    4. Tried to submit the form with empty description and confirmed that an error message about the required fields appears.
    5. Tried to submit the form with all inputs valid and verify it is correctly added to mongo database.

4. Edit Entry Page - Entry Form:
    1. Went to the "Edit Entry" page
    2. Tried to submit the empty form and confirmed that an error message appears.
    3. Tried to submit the form with empty name and confirmed that an error message about the required fields appears.
    4. Tried to submit the form with empty description and confirmed that an error message about the required fields appears.
    5. Tried to submit the form with all inputs valid, and some data changed, and verify it is correctly edited on mongo database.

5. Delete Entry Button:
    1. Went to the "Index" page.
    2. Clicked the delete button on one of the entries shown.
    3. Confirmed that the entry had been deleted from the Mongo Database.

## Deployment

This site is hosted using Heroku, it is linked directly to this Github repositories' master branch. The deployment on Heroku is updated automatically everytime a new push is made to the Github repo.

In order for the deployed site to work correctly on Heroku, there must be a procfile, requirements.txt file and an app file.

While working on the project, an env.py file was used to store my MONGO_URI. This was put into the .gitignore file to keep my MONGO_URI/password from being uploaded to github.
On my Heroku deployment the MONGO_DBNAME and MONGO_URI values are input into the config vars directly. This keeps my database password out of the local files and stops anyone being able to access this.

A demo can be viewed on Heroku [here](https://gametionary.herokuapp.com/).

## Credits
### Content
- The text for most of the database entries was copied from [This Wikipedia Article](https://en.wikipedia.org/wiki/Glossary_of_video_game_terms)
- I used the following tutorial to give me a base toggleable sidebar to work with: [Sidebar Tutorial](https://www.w3schools.com/howto/howto_js_collapse_sidebar.asp)

### Acknowledgements

- I received inspiration for this project from [Urban Dictionary](https://www.urbandictionary.com/)

This is for educational use.