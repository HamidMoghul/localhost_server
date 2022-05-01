from flask import Flask, render_template
from .models import User, Tweet, DB


def create_app():
    web2 = Flask(__name__)
    web2_title = 'LocalHostServer'


    web2.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    web2.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    DB.init_app(web2)

    @web2.route('/')
    def root():

    # Grab user from the database we linked: 
        users= User.query.all()
        return render_template('base.html',title= 'Home', users=users)


    @web2.route('/test')
    def test():
        return f'<p> This is a page for {web2_title} </p>'

    @web2.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()

        return '''The database has been reset

        <a href='/'> Go to [homepage]</a>
        <a href='/reset'> Go to [reset]</a>
        <a href='/populate'> Go to [populate]</a>
        '''

    @web2.route('/populate')
    def populate():
    # I add here some hypothetical users and tweets: 
        user1 = User(id=1, username='Haji')
        DB.session.add(user1)
        user2 = User(id=2, username='Bob')
        DB.session.add(user2)
        user3 = User(id=3, username='John')
        DB.session.add(user3)
        user4 = User(id=4, username='Nancy')
        DB.session.add(user4)
        user5 = User(id=5, username='Kathy')
        DB.session.add(user5)
        tweet1 = Tweet(id=1,text='this is my first tweet', user=user1)
        DB.session.add(tweet1)
        tweet2 = Tweet(id=2,text='going to the moon!', user=user2)
        DB.session.add(tweet2)
        tweet3 = Tweet(id=3,text='What would be your favorite videogame if you were a cat', user=user3)
        DB.session.add(tweet3)
        tweet4 = Tweet(id=4,text='just hanging out', user=user4)
        DB.session.add(tweet4)
        tweet5 = Tweet(id=5,text='People love vacations!', user=user5)
        DB.session.add(tweet5)
        DB.session.commit()

        return '''The database has been reset

        <a href='/'> Go to [homepage]</a>
        <a href='/reset'> Go to [reset]</a>
        <a href='/populate'> Go to [populate]</a>
        '''
    

    return web2






'''
In the Terminal:
================
> export FLASK_APP=web2
> flask run

'''