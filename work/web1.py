from flask import Flask

web1 = Flask(__name__)


@web1.route('/')
def home():
    return '''
    <p>
    Test Page
    </p>


    <p>
    __________________________________________________________________________
    </p>


    <p>
    Body of the page
    </p>


    <p>
    __________________________________________________________________________
    </p>


    <p>
    Ez pz!
    </p>
    '''



'''
In the Terminal:
================
> export FLASK_APP=web1
> flask run

'''