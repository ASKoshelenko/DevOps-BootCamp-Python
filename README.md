>Please use branch ```flask-app``` for this task that already exist in your forked repository after you has been started task
# flask-app

Create a Flask web application that retrieves the information about the pull requests of https://github.com/boto/boto3 repository. 


Use GitHub REST API: https://docs.github.com/en/rest/pulls/pulls#list-pull-requests


Flask application template is provided.

![](https://gitlab.com/epam-devops-lab/epm-practice-lab-python-tasks/-/raw/flask-app/app.png)

Execute the following commands to run application, e:

    $ pip install -r requirements.txt
    $ python start.py

Then, open a browser and enter URL: 

    http://127.0.0.1:5000/pull_requests

The following columns have to be filled in _handlers/pull\_requests.py_:
- Number of pull request
- Title of pull request
- Link to pull request
 
Press buttons to change request parameters:
- ?state=open (PR state is open)
- ?state=closed  (PR state is closed)

Use **per_page=100** parameter (default value is 30) to fetch pull requests records from the repository. 

Avoid using any query parameters for GitHub API requests, except for `state` and `per_page`.

Use Access token to reach repository  https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token. Set it as environment variable: 
        
    $ export TOKEN=<your token>

