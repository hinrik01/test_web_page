# Ship O'Cereal

Ship O'Cereal is a online store where you can shop various cereals. 

This is a project for the course Verklegt Námskeið 2 in Reykjavik University.
The creators of the website are Andrea Einarsdóttir, Atli Karl Sigurbjartsson, Hermann Guðmundsson and Hinrik Pétur Jóhannson.
The teacher of the course is Arnar Leifsson.

  * [Setting up environment](#setting-up-environment)
  * [Setting up virtual environment](#setting-up-virtual-environment)
  * [Installing dependencies](#installing-dependencies)
  * [Running the project](#running-the-project)

<a name="setting-up-environment"></a>
## Setting up environment 

The following instructions assume that are using the PyCharm interpreter.

Start by updating your current python to version 3.9.

When you open up PyCharm, select Get from version control 
![Screenshot 2021-05-12 at 10 25 42](https://user-images.githubusercontent.com/54948246/117960562-a12d1d80-b30c-11eb-826a-8e7a27c59d22.png)
Into the URL box, put the URL below and press clone.
>URL: https://github.com/andreaeinars/ship_o_cereal.git

<a name="setting-up-virtual-environment"></a>
##  Setting up virtual environment

First, make sure you don't already have a virtual environment folder in the project directory. 
Then go to settings -> project -> python interpreter. There you can choose the "python interpreter" dropdown and choose show all.
Then you click the + and choose virtual environment, and a new virtual environment gets created for the project.

<a name="installing-dependencies"></a>
##  Installing dependencies

Inside the virtual environment, make sure you have (venv) in front of your working path, run the following command:
> pip install -r requirements.txt 
![Screenshot 2021-05-12 at 10 23 04](https://user-images.githubusercontent.com/54948246/117960113-3380f180-b30c-11eb-9a95-a6274dc2f770.png)



This requirements.txt file includes Django and all the additional libraries, packages, db, etc. needed for the system to work (including versions).
Running this pip install command installs Django and sets everything up in your virtual environment.

<a name="running-the-project"></a>
## Running the project
To run the project, run this command in the home directory of the virtual environment you have created!
>python manage.py runserver

Finally, to go to the website, simply press the IP in the terminal.

![Screenshot 2021-05-12 at 10 26 41](https://user-images.githubusercontent.com/54948246/117960641-b86c0b00-b30c-11eb-95be-6ef12bedbd8d.png)
