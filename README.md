>Please use branch ```flask-app-tests``` for this task that already exist in your forked repository after you has been started task
# flask-app-tests

Create unit tests for Flask project from the previous task.  

Put your tests into _tests_ folder. 

Implement tests for scripts from  **handlers** folder.

Code coverage has to be equal or more than 80%. 

Use tox to run unit tests localy: 

    $ pip install -r requirements.txt
    $ tox -r

or pytest:

    $ pytest --cov=handlers --cov-fail-under=80

See also https://pytest-cov.readthedocs.io/en/latest/reporting.html
