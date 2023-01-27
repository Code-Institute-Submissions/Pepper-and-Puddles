# Pepper and Puddles

- This is a restaurant reservation web application using Python with Django, and a Postgres relational database.
- The site has a model view controller to allow customers to make bookings following CRUD principles, and to give administrative access to the site owner only.

# Site Goals

- The purpose of this site is to allow customers to make bookings in a particular restaurant. 
- The booking system should employ strong logic and consider real world business needs in order to be an efficient replacement for a manual means of restaurant reservation management.
- The site should reflect the restaurant and offer a satisfying user experience.

# Agile Development

- This project follow Agile principles and methodologies through assessing the Clear Value Proposition of User Stories

- The User Stories are catalogued using github's issues and projects features. The project is linked to the repository for this project, and set to public, and it should be visible to the assessment panel.

## Epics and User Stories

### Restaurant Owner Epics
- The site should be able to supply all information the customers could need. It should be laid out clearly and rationally. It should be easy, and enticing, for customers to make bookings. Bookings should be made with sophistacted logic, taking into account the restaurants capacity, opening times/days, and to not double book a table, but to also host multiple sittings per table.

1. USER STORY: Restaurant owner needs to see what bookings have been made
2. USER STORY: Restaurant owner should be able to have full CRUD capability for all bookings
3. USER STORY: Double bookings should not occur
4. USER STORY: Customers contact details need to be given to the owner
5. USER STORY: Passwords, bookings, contact information should all be secure, and not visible to other customers

### Customer Epics
- The site should be clearly laid out, easy to navigate, on any device. I want to see the menu, contact details and location, nearby parking etc. I want to be able to make a booking for any number of people, and to be able to choose a suitable time.

6. USER STORY: The menu, contact details, and location of the restaurant should be present
7. USER STORY: The site should be easy to understand, navigate and use
8. USER STORY: Customers need CRUD capability
9. USER STORY: Customers should be able to find an available booking slot for their party size
10. USER STORY: Customers should be able to attach a message to their booking for the owner to see
11. USER STORY: Any of the customers data manipulations should be confirmed with relevant feedback


- Making the Reservation functionality
- I have created a function that requests date, time, name, phone, and, email from the user.
- On a successful submission, the user should be brought to a confirmation.html page.
- Missing positional argument of Table ID, perhaps Table ID not yet defined, could work later, removed for now temporarily.

- Additional page is necessary, booking confirmation page added.
- Additional page, view_bookings, created.


- Moved all html files to templates within the booking app. Expect that the site should work from index onwards through the templates.

- Classes successfuly appear in admin panel
- Two objects have been created in the admin panel for classes of bookings, and have been successfully rendered in a template view.

### Example Sites

- Calendar booking vs Email/Message request
Below are examples of different approaches to take bookings by real-life restaurants. The first uses a popular booking service provider and has their unifrom set-up. The second is a less sophisticated system that allows the user to supply the restaurant with a message and contact details. The system of booking must be performed by the restaurant owner instead of being managed by the site.

![calendar_booking](assets/readme_documentation/calendar_booking_example.jpg) ![message_booking](assets/readme_documentation/booking_page_example.jpg)


## Wireframes

- Homepage for mobile

![Homepage_example_mobile](assets/readme_documentation/homepage_wireframe.jpg)
- Dropdown menu for mobile

![Dropdown_example-mobile](assets/readme_documentation/dropdown_wireframe.jpg)

# Testing

- Created booking app, tested functionality by using command line "python3 manage.py runserver".
H1 html text showing in server. App set up successfully.

- Created Admin by usering createsuperuser command line, verified by signing in following url admin path on open server"

- Form will not create object for booking. Solution: Changed action in form to call on view function, imported redirect to views

# Deployment

Log into Heroku account. Click "NEW" on the Dashboard, select "Create new app" from the drop-down. Give the app a unique name, and click "Create app" to confirm.

Log into ElephantSQL. Click "Create New Instance" on the Dashboard. Give your new plan a Name, select the Tiny Turtle (free) plan, the Tags field can be left blank. Select Region: EU-West-1 (Ireland). Then click "Review", confirm details, and click "Create instance".

Return to the ElephantSQL Dashboard and click "database instance name" for this project, in the URL section, click the copy icon to copy the database URL.

In the project workspace create a env.py file, ensure this is listed in the .gitignore file. In the env.py file write import os. After a blank line type:  os.environ["DATABASE_URL"] = "<copiedURLfromElephanSQL>". This will need a secret key as Django application so beneath the url type:  os.environ["SECRET_KEY"] = "any_secret_key". And save the file.

In settings.py add the followng code to the Path import:  import os
 import dj_database_url
 if os.path.isfile('env.py'):
     import env
A little further down, remove the insecure secret key provided by Django. Instead, we will reference the variable in the env.py file, so change your SECRET_KEY variable to the following:  SECRET_KEY = os.environ.get('SECRET_KEY').
Next in settings.py, where you find the following:
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': BASE_DIR / 'db.sqlite3',
      }
  }
Replace with: 
  DATABASES = {
     'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
 }

 Save the settings file and run the terminal command "python3 manage.py migrate".
 Follow this up and add, commit, push the project to gihub.

Return to the Heroku Dashboard and select the Settings tab. Add some config vars:
DATABASE_URL with the value of the copied url from ElephantSQL,
SECRET_KEY with value of the secret create in env.py file.
PORT with value of 8000.

To connect Cloudinary to the Heroku project, set up a free account on Cloudinary.
On the Cloudinary dashboard select Copy To Clipboard next to API Environment Variables.

In the env.py file, add at the bottom, os.environ["CLOUDINARY_URL"] = "Value copied less the beginning part of CLOUDINARY_URL="
Copy this value again without the prefix and return to Heroku settings, Config Vars.

Add new Config Var:
CLOUDINARY_URL  with value of copied text.

In settings.py under INSTALLED_APPS: above 'django.contrib.staticfiles', add 'cloudinary_storage', below 'django.contrib.staticfiles', and 'cloudinary'.

Near the end of settings file below STATIC_URL = '/static/' add
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIR = [os.path.join(BASE_DIR,'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

At the top of settings.py, under BASE_DIR type
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

Scroll to half way down to TEMPLATES =, and in the 'DIRS': [] line, between the square brackets type TEMPLATES_DIR.

Scroll back up, and below DEBUG = True, skip a line and type: 
ALLOWED_HOSTS = ['*herokuappname*.herokuapp.com', 'localhost']

Create three directories in the top level, next to manage.py file: templates, media, and static. Additionally create a Procfile. Inside the Procfile add the line:
web: gunicorn appname.wsgi

Save, add, commit, and push the project.

In the Heroku Dashboard, click on the Deploy tab, click on the option to Deploy through Github, this may need to be set up if its your first time. Search your repositories for the project. Scroll to the bottom of the page and select Deploy Branch.
