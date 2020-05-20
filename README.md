
<img src="static\images\Annotation 2020-05-20 231446.png"/>
<img src="static\images\Annotation 2020-05-20 231601.png"/>
# 12Run - A community-driven running event web application

This web application serves as a database index of community local running events contributed and hosted by users of the public themselves.

The website aims to act as a platform that encourages the running community to grow, thrive and actively encourage one another to meet up and train together. This keeps them motivated and builds a sense of belonging within the running community. Each event contains various key information - ``` Title, Location, Date/Time, experience level, category and description ```

## Project Purpose
> Social Facilitation Theory refers to the tendency of people to perform better when they are being watched or when they are competing with others doing the same task.

Social facilitation is coined as the top leading factor to not only helping people find new breakthroughs and personal bests in running, but also to keep them motivated for a lifelong journey in staying fit and healthy. 

However, unless an individual was a once part of a fitness club or was fortunate enough to have found like-minded friends with the same objectives, it isn't easy to find people to gather and train together with. Given the unknown difference in levels of fitness, goals or interests between people, these factors play a huge part to the invisible walls beign built around us, preventing the likelyhood of an impromptu meet up for exercising between strangers or even friends. 

My motivation for this project is to break down these walls by providing the local running community to have a platform to host their training sessions for the public, join nearby community events or even just to intermingle with one another. 


## Demo

A live demo can be found [here](https://kc12run.herokuapp.com/).

## UX

My goal is to allow users to easily search for events/sessions by entering keywords, or search by category/level of experience. Starting with a search engine placed at the hero image section, this allows users to understand that they have direct access to type in a certain exercise plan that they have in mind to see if there are any available on the server. Site users can also contribute and create events or leave a comment to enquire more on each event. 

- Users can either directly search from the home page and be redirected to show events page, or alternatively they can click on the [Nav] search icon to be brought to the see all events page.
- On the show programmes page, users can create a new event by clicking on the [+] button next to the search button. 
- Users can also filter their search by clicking on key categories or level of difficulty.

I opted to choosing pictures which showcases people training together of all different levels of fitness, to eliminate the underlying concern that one has to be extremely fit to be part of the running community. I segregated the information into seperate cards, giving each a generous amount of space between one another for ease of reading. To prevent overloading of information in database, i used pagination to split excess data into seperate pages to keep the page neat and tidy.

## Technologies
1.	HTML
2.	CSS
3.	[Bootstrap version 4.4](https://getbootstrap.com/)
4.	Python (3.6)
5.	Jinja2 (2.10.3)
6.	Flask (1.1.1)
7.	MongoDB
8.	Font Awesome (4.7.0)
9.	Google Fonts API
10. Flask 
11. Javascript
12. MongoDB noSQL
13. Heroku Deployment

## Features
The web application achieves these four basic functions of a database, namely CRUD –  an acronym for the four basic types of SQL commands: Create , Read , Update , Delete.

These functions allows users to perform the following features:
#### 1.	Create
a)	Add a new event with the following detail: 

- Event image
- Title
- Host Name
- Date/Time of event
- Estimated Duration of event
- Location
- Difficulty
- Category
- Description

b) Create a comment on each individual event

#### 2.	Read
Find events that matches the queries such as having a searchbox for event titles, alternatively clicking on keyword tags that allows the user to filter their searches via categories or level of difficulty.
Clicking on event card opens up more information which allows users to read comments left by the public.

#### 3.	Update
Edit the event details in the database

#### 4.	Delete
Delete the event

### Features Left to Implement
- Introduce functionality of likes/im going so that will have a +1 increment each time a user clicks on it.
- Allow users to upload image files to the website, instead of having to upload the image URL or convert their image to a URL
- Validate search query by preventing users to type in "[]" in search bar.

## Testing
#### 1. Create:
**•	Add a new event archive to the database**

All the form input boxes are able to fetch data to the database when the user fills up the form and press the submit button. There is also a javascript validator in date/time, event name, duration, location to prevent the user from submitting an empty field.

Selecting the category is optional if host is not sure. Image is also optional and a default image will be added.

**•	Create a comment on each individual event**

The comment form is successful in fetching input data to the database with both the commenter’s name and comment. Every single comment entry made on each individual artwork is added to the database as an object in an array called ‘reviews’, under the specific object ID given for each event. Once the user has submitted the comment, the comments will show up after the page has automatically refreshed.

#### 2. Read:
**•	Searchbox for event titles**

The search function is able to perform its function by filtering out the results according to the search query input using the regular expression, which would ignore any case sensitivity and parse in the search query as a string.

However, there is a limitation I found during testing that adding in "[]" would cause an error. This will be looked into. 

**•	Keywords to filter the queries**

In addition to the search function, the user has the ability to narrow down their searches by filtering out the results based on the each category/difficulty that the event has been assigned to. 

#### 3. Update:
**•	Edit the details of the existing event**

The default details of the existing events from the database will reflect in the input form. This is to ensure that the user is aware of the changes they are making to the artwork archive. Once the form is submitted, the data of the event archive will be updated to the database.

## Mobile Responsiveness and testing
To ensure compatibility and responsiveness, the site was tested across multiple browsers such as Chrome, Safari and Internet Explorer and on iOS devices - iPhone Xs Max, iPad and iPad Pro.

All links have been tested to ensure correct re-direction to desired destination.

- logo -> index.template.html
- Search Events, join now -> show_programmes.template.html
- event card -> programme_details.template.html
- create -> create_programme.template.html 
- edit icon -> edit_programme.template.html

## Deployment
This site is hosted using Heroku, deployed directly from the master branch and Github. The deployed site will update automatically upon new commits to the master branch.

To run locally, you can clone this repository directly into the editor of your choice by pasting `git clone https://github.com/kwokcheong/Project3_12Run.git` into your terminal.

## Credits
### Media
I do not own any of the photos used for the website and they were taken from various websites.

Icons are from the [Font Awesome CDN](https://fontawesome.com/v4.7.0/icons/)

### Acknowledgements
Template and tutorial of MongoDB, Flask and Jinja provided by the [lecturer]
w3School for tutorial on javascript validator.
