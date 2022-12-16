Project Description
==============================

A sample pytest project https://www.saucedemo.com/ to trigger automated
tests, generate Allure Report and publish to GitHub Pages via GitHub
Actions workflow

|selenium_test| |Allure Report|

How to work with the Repo:
--------------------------

1. Create a folder locally
2. Clone the repo using 'git clone' command
3. Open the Project in PyCharm
4. Install dependencies using 'poetry install' command
5. Create a branch and start working

Notes:
------

-  AB - an example of a branch name
-  test_TC_001_05_add_into_cart.py - an example of a test name

Regular commands:
-----------------

-  Run all tests 'poetry run pytest'
-  Run only specific test 'poetry run pytest tests/<test_filename>'
-  Run only specific function from the test 'poetry run pytest -k'<part_of_test_fn_name>'

.. |selenium_test| image:: https://github.com/ivanovajulika/Sauce/actions/workflows/action.yml/badge.svg
   :target: https://github.com/Natalia-Tsy/SauceDemoProject/actions/workflows/action.yml
.. |Allure Report| image:: https://img.shields.io/badge/Allure%20Report-deployed-yellowgreen
   :target: https://natalia-tsy.github.io/SauceDemoProject/
