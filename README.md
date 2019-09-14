Installing
**********

Please start by cloning the repo into your working directory.

    $ git clone git@github.com:chrislombaard/pears.git
    $ cd pears/

Creating a Python Virtual Environment
=====================================

To get started with Lasso install Python 3.6 and pip. Then do:

    $ virtualenv ve -p python3.7
    $ source ve/bin/activate
    $ pip install pip-tools
    $ make up
    $ make deps

If you don't have virtualenv installed first run:

    $ pip install virtualenv
    $ sudo /usr/bin/easy_install virtualenv


Install Step 1 - Getting the backend up and running.
====================================================
Once you've gotten your virtualenv installed and have activated it, then its time to install the dependencies required to run the django backend, the server will default to `0.0.0.0:8010`:

    $ python manage.py migrate
    $ make su
    $ make run
