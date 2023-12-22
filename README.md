>Please use branch ```python-script``` for this task that already exist in your forked repository after you has been started task
- [ ] Create a program that prompts the user to input their age, and then prints out their age category
based on the following criteria:

  - If the user is less than 2 years old,the program should output "You are a baby".
  - If the user is between 2 and 12 years old, the program should output "You are a child.".
  - If the user is between 13 and 19 years old, the program should output "You are a teenager.".
  - If the user is 20 years old or older, the program should output "You are an adult.".

- [ ] In order to verify the script, run the following commands:

  - Install required packages (only once):

        pip install -r requirements.txt
  - Run script:

        python main.py
  - Run code checkers

        tox -r (run code checkers)
  - Submit your solution

- [ ] Fix all issues found during validation.

- [ ] Use termcolor library to highlight caption “Age category detector”:

  - Install library locally:

        pip install termcolor
  - Add termcolor to _requirements.txt_.
  - Import library in the main.py, e.g., _“from termcolor import colored”_
  - Highlight caption with any color or/and effect.
