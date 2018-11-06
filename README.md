Fifth and final project for the Code Institute: Full Stack Frameworks with Django.


Commits:
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
25. Fixed image bug, upvotes bug, login bug.

Technologies uses:
Django - 
Pillow - used to open images in python
Djang-Forms-Bootstrap - to allow easy rendering of forms
DJ-Database-url - allows access to postgreSQL instead of standard database driver used in Django
Psycopg2 - allows adaption to postgreSQL for python
Whitenoise - hosts static files on Heroku
Gunicorn - WSGI HTTP server for python
Stripe - allows us to take bank card payments

Testing:
Travis - 
[![Build Status](https://travis-ci.org/sarahcrosby/project-five-django.svg?branch=master)](https://travis-ci.org/sarahcrosby/project-five-django)