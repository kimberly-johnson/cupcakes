"""Flask app for Cupcakes"""
from flask import Flask, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"
# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/api/cupcakes')
def get_cupcakes():
    """display all cupcakes, create cupcake"""
    
    
@app.route('/api/cupcakes', methods=["POST"])
def create_cupcakes():
    """create a new cupcakes"""


@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake():
    """display single cupcake"""
    

