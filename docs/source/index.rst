Flask-Mux's documentation!
=====================================

**Flask-Mux** is a lightweight Flask extension that provides a routing 
system similar to that of Express.js_. It basically wraps Flask's 
url route registrations API to add more flexibility.

Get started with :ref:`Installation` and then get an overview with 
the :doc:`quickstart`. There is also a more detailed :doc:`tutorial/index` 
that shows how to create a small but complete application with Flask. 
The rest of the docs describe each component of Flask in detail, 
with a full reference in the :doc:`api` section.

.. _Express.js: https://www.expressjs.com/
.. role:: raw-html(raw)
    :format: html

.. toctree::
   :maxdepth: 3
      quickstart <quickstart.rst>
      api <api.rst>
   :caption: Contents:


Installation
==================

Install Flask-Mux using pip:

.. code:: Bash

   $ pip3 install flask-mux

User's Guide
==================

* :doc:`quickstart`
* Tutorial 
   - Pure Flask example
   - Flask-Mux example
* :doc:`api`
   - Mux
   - Router


Tests
==================
Tests are all kept in ``tests/``, to run them, install ``tox`` and simply
invoke ``tox`` in your command line.

Contributions
==================
Contributions are very welcome. Please feel free to clone the project's repository
and make a PR with your improved version. :raw-html:`<br />`
If you have a question or would like to request a feature, please create an issue
on Github, tweet me @DMehdi19 or reach to me by email.


License
==================