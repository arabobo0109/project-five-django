Fifth and final project for the Code Institute: Full Stack Frameworks with Django.



Real world need - informative blog. When live, would generate an income. 

Bootstrap theme, customised.


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
25. Fixed image bug, upvotes bug, login bug, implemented messages.
26. Fixed messages bug. Customised 'cart.html'.
27. Implemented 'remaining' functionality to 'cart' app. Added 'about' page, and more content to apps and customised layouts. 
28. Added background image to page header. Edited 'index.html' to include navigational links.
29. Added comments to code. Finishing touches to CSS, including password reset forms. 
30. 

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

When customising any of my CSS, I would load the page in developer tools and write the code this way.





To ensure my colour scheme did not clash, I loaded my header image into MS Paint, and picked a colour that I liked, and used the colour picker to find the RGB code. I then translated this into the HEX code, and used it where I wanted in my project. I then input the HEX code into https://coolors.co/ to find my colour scheme.


Travis - 
[![Build Status](https://travis-ci.org/sarahcrosby/project-five-django.svg?branch=master)](https://travis-ci.org/sarahcrosby/project-five-django)



Credits 

background image
https://coolors.co/ colour scheme