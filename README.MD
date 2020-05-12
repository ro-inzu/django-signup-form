# Django-form
Uses Django to create a simple POST form with sessions and a form field class.
The web app will display the first name entered on the form using sessions to display the value on the confirmation page.

![PyPI - Python Version](https://img.shields.io/badge/python-3.7-blue)
![PyPI - Django Version](https://img.shields.io/badge/Django-3.0.6-green)
![PyPI - Requests Version](https://img.shields.io/badge/Requests-2.23.0-yellowgreen)

![Screenshot](/screenshots/index.png)
![Screenshot](/screenshots/confirmation.png)

### Setup
- (Recommended) create your virtual environment
  - python3.7 -m venv env
    - source env/bin/activate
- install requests
  - python3.7 -m pip install requests, Django


## Form Design
 - [Form Design Style 7](https://www.sanwebe.com/2014/08/css-html-forms-designs)


## Templates
- base.html
- signupform.html
- confirmation.html

## Views
  - index: renders the signupform.html template
  - after submitting the form it renders confirmation.html template
