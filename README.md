#Local Quick Start
##Before You Start
First create a virtual environment
```
mkvirtualenv -p python2.7 dev
```

If you have created the virtual environment, then use this commend to enter it
```
virtualenv dev && source dev/bin/activate
```

Here is the command to install the requirements
```
pip install -r requirements.txt
```
Here is the command to set up and run the program
```
python views.py -h 134.197.20.79 -p 5000 --threaded
```
134.197.20.79 should be replaced with your machine ip address. The command is to set up a server with your machine
