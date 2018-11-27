# Do Life Yourself - A Lifestyle Blog For People Who Do Things Their Own Way

## Project Five: Full Stack Frameworks with Django [![Build Status](https://travis-ci.org/sarahcrosby/project-five-django.svg?branch=master)](https://travis-ci.org/sarahcrosby/project-five-django)

This is my fifth project, a web application that willdraw on the skills and knowledge I have acquired across the whole course. 

The blog capitalizes on the 'do it yourself' attitude, which is increasing in popularity. When live, it will feature tutorials from the author, which document projects from inception to completion. These range from typical home DIY projects, to more ambitious ideas such as launching a business and a DIY wedding.

The real-world need is for an informative blog, that will generate an income for the owner.

The project will consist of multiple apps, which include user registration and authentication mechanisms, which will provide access to a member's only area. Within this area, members can fund premium projects, which would be undertaken when funding is complete. Members can also submit their own projects, which they would like to see attempted. 

### Demo

A live demo can be found here: https://project-five-django.herokuapp.com/

### Technologies and Languages

* [Bootstrap (4.1.3)](https://getbootstrap.com/) - for the template, and to build a responsive and visually appealing site.
* [Javascript (1.8.5)](https://en.wikipedia.org/wiki/JavaScript) - the language and logic of the interactive elements on the page
* [jQuery(3.3)](https://jquery.com/) - a JavaScript library to enhance the user's experience
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - the language used to customise and present the web app, including CSS3 media queries.
* [HTML5](https://en.wikipedia.org/wiki/HTML) - the language used to write and create the web app.
* [Python (3.0)](https://www.python.org/) - for backend code and site functionality.
* [Django (1.11.15)](https://www.djangoproject.com/) - for templates, forms, data and authentication mechanisms.
* [UnitTest](https://docs.python.org/3/library/unittest.html) - the Python framework for testing code
* [Postgres](https://www.postgresql.org/) - the database used to store data.
* [Stripe (2.10.1)](https://stripe.com/) - for processing payments.
* [Google Fonts](https://fonts.google.com/) - for fonts used throughout the project.
* [Font Awesome](https://fontawesome.com/) - for icons used in the project.
* [Dj Database Url(0.5.0)](https://github.com/kennethreitz/dj-database-url) - allows access to postgreSQL instead of standard database driver used in Django.
* [Django Forms Bootstrap (3.1.0)](https://github.com/pinax/django-forms-bootstrap) - to easily generate bootstrap forms.
* [Gunicorn (19.9.0)](https://gunicorn.org/) - Python server.
* [Pillow (5.3.0)](https://pillow.readthedocs.io/en/5.3.x/) - for images in Python.
* [Psycopg2 (2.7.5)](http://initd.org/psycopg/) - PostgreSQL adaptor for Python.
* [Travis CI](https://travis-ci.org/) - for continuous testing of my code.
* [Whitenoise (4.1)](http://whitenoise.evans.io/en/stable/) - to host static files on Heroku.
* [Heroku](https://dashboard.heroku.com/) - to host the project.
* [GitHub](https://github.com/) - for version control, and to host the project.
* [Amazon Web Services](https://aws.amazon.com/) - for hosting purposes.
* [Cloud 9](https://c9.io/) - the cloud-based integrated development environment used to write the code.

### UX

I used a Bootstrap template to ensure my web application was visually appealing. To keep a clear division between my code and the Bootstrap code, I have created a 'library' folder which contains the original code. The template was called 'Clean Blog' and can be found [here](https://startbootstrap.com/template-overviews/clean-blog/).

I customised the code to suit my needs, and also added a 'custom.css' file. When editing CSS, I used the developer tools to edit my code before saving it. I also used the emulator in the developer tools to confirm that my app worked on different screen sizes, and I also loaded my app on my mobile, iPad and laptop.

To ensure my colour scheme did not clash, I loaded my header image into MS Paint, and picked a colour that I liked, and used the colour picker to find the RGB code. I then translated this into the HEX code, and used it where I wanted in my project. I then input the HEX code into https://coolors.co/ to find my colour scheme.

When designing the different aspects of my page, I decided that each feature should have an introduction, so the user could choose what they would like to see in more detail. For example, I listed a summary of the blog posts, and the user could click on a specific one to load the entire blog post. This was to save time loading the page and to stop the user feeling overloaded with information.

I also wanted to incorporate the following user stories: 

* As a user, I wanted to feel part of a community, by having a registration function and separate member's only page and content.
* As a registered user, I wanted to make contributions to the blog, by being able to make contributions, either financially or by voting and submitting ideas.
* As the site's author, I wanted to make an income from the website, by having a working eCommerce app.
* As a user, I wanted to understand what the website was about, by having an 'about' page.
* As a user, I wanted to be able to view the website on different devices, by having a responsive design.
* As a user, I didn't want to be confused or overloaded by information, by having a simple page with no pop-ups.
* As a user, I want to be able to re-set my password if I forget it, by receiving a password re-set email to my registered email address.

### Features

* Database functionality - to store and persist data, such as the blog posts.
* User registration and authentication - to allow members to interact with the site, and to persist the user's shopping cart between visits.
* About page - introduces and explains the meaning of the web appplication.
* Log in - allows the user to log into the member's only part of the website.
* Log out - allows users to log out of the site, to enhance security, ie. if they are using a shared computer.
* Shopping cart - allows users to see what they have added to their shopping cart, adjust the amounts, remove items they don't want, and proceed to to the check out.
* Checkout - uses Stripe to allow users to pay for items in their cart. 
* Blog - retrieves the author's blog posts from the database. This is the main content of the web application, as the users vot and pay for the blog posts they'd like to read next.
* eCommerce - allows users to browse which projects they would like to fund.
* Posts - allows registered and signed-in users to post their ideas for what they'd like to see next on the blog, and also read and vote for other people's ideas.
* Search - allows users to search through the eCommerce app, and find products they may be searching for.
* Password re-set - allows users to retrieve forgotten websites, so they can access their account if they have forgotten their website. This includes physically sending an email out to the user.
* Messages - adds a message to the page the user is on, if they perform certain functions, such as register, log in or log out.
* Progress updates - I added status messages to each project to explain to the user where the project was up to, ie. if it was waiting to be funded, or whether it was in progress. I also added progress bars, which would be functional when the site went live, to show how much funding a project had received.

In the future, I would extend the Django User model, to improve the 'upvote' functonality. This would ensure the user could only vote for a blog post once.

### Deployment

My code is deployed to GitHub, at: https://github.com/sarahcrosby/project-five-django/

I have also deployed my code to Heroku, at: https://project-five-django.herokuapp.com/

To run the app locally, first of all set up a virtual environment, and then download the files from GitHub and upload. 

Alternatively, you could clone the repository, by typing the following command into the terminal:

> $ git clone https://github.com/sarahcrosby/project-five-django/

Then, ensure you follow the requirements.txt and install everything indicated in this.

Due to sensitive information such as the secret keys being hidden in my code, you will need to address this with your own before the web app will function properly. You will also need to connect to your own database. This includes the Stripe and AWS keys.

### Testing

I used Travis CI for continuous testing throughout development - [![Build Status](https://travis-ci.org/sarahcrosby/project-five-django.svg?branch=master)](https://travis-ci.org/sarahcrosby/project-five-django)

I have also included automated Unit Tests across my project - please see the separate test files within each app.

I manually tested my project throughout construction. This included running through every link and trying to 'break' my code. I also asked my friends to do the same, to ensure I hadn't missed anything. I tried deleting, adding and editing posts as a registered user, and ensured posts were added to the website when they were submitted. I tried the password re-set function and changed the password on my account. I checked all of the blog posts, both on my code and on the deployed code, to ensure the image hosting was working. I upvoted submitted posts, and ensured the log in and log out functions worked. I created new users, and ensured the provided information was correct by loggin into the admin panel, and comparing the data. I checked the 'search' app by searching for words that I knew would return results, and also for words that I knew would not return results. I ensured the cart persisted between visits, by logging in, adding items, logging out, then logging in on another device, to ensure the number of items I added to my cart was the same. 

During my manual testing, I discovered a bug with Stripe. I was not able to process payments, despite using the card number '4242424242424242' which allows test payments with Stripe. The issue was caused due to my placement of the JavaScript, as I had not placed it before the jQuery, and also that my '{% block head_js %}' was not correctly placed. After resolving this, I also noticed that I had not updated the 'views.py' for the checkout app, to reflect changes I made to the 'Product' model, as I had changed the 'price' attribute to a 'tribute', to reflect the dynamic of the website's eCommerce. Once I had changed these, I was able to make test purchases with Stripe, to ensure the page was functioning as required.

I encountered a bug when I was updating the models for my database. After writing the original models, I decided that I wanted to change them, but this caused errors when migrating because I had already uploaded content to the database, so the existing models did not match the new models. To resolve this, I had to delete every migration from the separate apps, and start again. In the process, I deleted all of the content from my database, which included the blog posts which I had written. I did not have time to re-write the posts before the submission date, which is why I included the 'Lorem Ipsum' text, as a placeholder for the full blog, which would appear when the blog went live. I learned the hard way that I should back-up my code and website data! - but it is a mistake I will not make again. 

I also experienced a bug when manually testing my site, and I was able to 'break' the cart app when I input an order for 0 items. To fix this, I added:

> min="1"

to the input on the form for adding items to the cart. This resolved the bug, and meant that users had to add at least one item to the cart, before proceeding to the checout.

### Version Control

1. Initial commit. 
2. Created superuser. Added accounts templates and log in functionality.
3. Added template inheritance from base.html, and authorisation.
4. Added registration and profile functionality.
5. Added password re-set functionality.
6. Added backends.py, edited to allow users to log in using username or email.
7. Created virtualenvironment, added requirements.txt and created blog, .gitignore.
8. Added env.py and updated .gitignore.
9. Integrated Travis testing.
10. Addressed Travis bug.
11. Started posts app. Installed pillow. 
12. Added library for Bootstrap code, addded posts templates, installed Djang-Forms-Bootstrap.
13. Updated requirements.txt.
14. Removed author bug.
15. Deployed to Heroku, after installing requirements.
16. Created ecommerce, cart and search apps.
17. Installed Stripe and checkout app.
18. Added member's home page, content app, worked on layout and search page.
19. Implemented Bootstrap template.
20. Customised product pages.
21. Created progress page.
22. Customised 'posts' app, to allow user to submit their own projects.
23. Fixed bug with search app and implemented for ecommerce.
24. Improved functionality to blog app.
25. Fixed image bug, upvotes bug, login bug, implemented messages.
26. Fixed messages bug. Customised 'cart.html'.
27. Implemented 'remaining' functionality to 'cart' app. Added 'about' page, and more content to apps and customised layouts. 
28. Added background image to page header. Edited 'index.html' to include navigational links.
29. Added comments to code. Finishing touches to CSS, including password reset forms. 
30. Started testing.
31. Completed testing.
32. Updated README.
33. README additions. Fixed cart bug. Edited CSS on 'checkout.html' and 'cart.html'. Addressed 'Stripe' bug.
34. Added more automated tests. Addressed console error messages.