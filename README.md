# Gametionary

This project is an online dictionary for Game related words, abbreviations and phrases.

Using this desktopsite, you will be able to read the entries that have been entered into the database.
Add you own entries into the database. Edit entries that are in the database, and delete entries from the database.

You can also upvote entries that you find helpful or accurate.

The goals of this desktopsite are to:
- Allow users to easily share information on game related jargon.
- Allow users to easily find information on game related jargon.
- Allow users to upvote information that they find helpful.

## Demo

A demo can be viewed on Heroku [here](hhttps://gametionary.herokuapp.com/).

## UX

My goal with the design of this desktopsite was to make it simple to navigate and use.
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

Each page features a navigation bar with a brand-logo for quick access to the home page, a search bar, and a button to open the sidebar.

#### Index

This page features introduction text and buttons to the various pages.
It also features 2 random entries to give users an idea of what to expect, and get them interested.

#### Search

This page features a search bar and will show the database entries that contain your search.
If you were redirected to this page via the navbar then your search will be pre-entered. Otherwise this page will load empty.

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
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

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

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)
- I used the following tutorial to give me a base toggleable sidebar to work with: [Sidebar Tutorial](https://www.w3schools.com/howto/howto_js_collapse_sidebar.asp)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from [Urban Dictionary](https://www.urbandictionary.com/)