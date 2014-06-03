=====================================
Please write a README for this app :)
=====================================

This is a django app template providing a setup.py script.

Create a new app
================

Note: all action would preferably be made in a python virtual env.

Clone this repository in a location of your choice.

In your virtualenv, in another location (eg. ``sources`` directory), enter the following command::

  django-admin.py startapp --template=<django-app-template-directory> awesome-app

Install your new app
====================

The best way to install and then work with your newly created app is to install it in "dev mode".
Go to your app directory and enter the following command::

  pip install -e .

Once installed in development mode, you don't need to install again when you change files.
Of course, Django runserver automatic reload will work.

Post install steps
==================

Your template based app should immediately work but you can adapt the following files:

- ``setup.py``: Add author, website, license, etc.
- ``<app>/version.py``: Your app version number
- ``MANIFEST.in``: Remove or change include directives

In this case you can run ``pip install -e`` again.
