"""
A file for automating the execution of manage.py tasks in Django.
"""
from os import chdir
from subprocess import run


# Store the user's choices in a dictionary
choices = {
    1: 'Boot the dev server',
    2: 'Makemigrations & migrate',
    3: 'Add another app to your project.',
    4: 'Create a superuser.',
    5: 'Collect static files.',
    6: 'Run unit tests.',
    7: 'Update requirements.txt',
    8: 'Create virtualenv.',
    9: 'Initialize git repo, add + commit files'
}


# Add another app to your Django project
def add_app():

    app_name = input('Enter the name of the app that you want to add to your project: ')

    if not app_name:

        input('App name cannot be null! Press enter to exit.')

    run(['py', 'manage.py', 'startapp', app_name])

# Initialize a git repo, add, and commit files
def git():

    git_init = run(['git', 'init'])
    git_init.check_returncode()

    git_add = run(['git', 'add', '-A'])
    git_add.check_returncode()

    git_commit = run(['git', 'commit', '-m', 'initial commit'])
    git_commit.check_returncode()

    # Ask the user if they want to do a 'git remote' configuration
    git_remote_choice = input('Would you also like to do a git remote configuration(y/n)?: ')

    if git_remote_choice == "y":
        remote_url = input('Enter the URL of your remote repository: ')
        git_remote = run(['git', 'remote', 'add', 'origin', remote_url])
        git_remote.check_returncode()
    elif git_remote_choice == "n":
        pass
    else:
        input("Invalid value entered. Press enter to exit.")


if __name__ == "__main__":

    # Blank line for readability
    print()

    # Show the user their choices
    for key, val in choices.items():

        print(key, val)

    print()

    # Prompt the user to make a choice
    u_choice = int(input('Execute a process, based on the above options: '))

    if u_choice == 1:
        run(['py', 'manage.py', 'runserver'])
    elif u_choice == 2:
        app_name = input('Enter the name of the app that you want to do migrations for: ')
        run(['py', 'manage.py', 'makemigrations', app_name])
        run(['py', 'manage.py', 'migrate'])
    elif u_choice == 3:
        add_app()
    elif u_choice == 4:
        run(['py', 'manage.py', 'createsuperuser'])
    elif u_choice == 5:
        run(['py', 'manage.py', 'collectstatic'])
    elif u_choice == 6:
        run(['py', 'manage.py', 'test', 'postings.tests'])
    elif u_choice == 7:
        run(['pip', 'freeze', '>', 'requirements.txt'])
    elif u_choice == 8:
        venv_name = input('Enter a name for your virutalenv: ')
        run(['py', '-m', 'venv', venv_name], check=True)
    elif u_choice == 9:
        git()
    else:
        input('Invalid option. Press enter to exit')