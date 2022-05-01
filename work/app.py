from flask import Flask, render_template

app = Flask(__name__)
app_title = 'LocalHostServer'


@app.route('/')
def root():
    return render_template('base.html',title= 'Home')


@app.route('/test')
def test():
    return f'<p> This is a page for {app_title} </p>'


'''
In the Terminal:
================
> export FLASK_APP=app
> flask run

'''