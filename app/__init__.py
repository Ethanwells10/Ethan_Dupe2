from flask import Flask, g
from .app_factory import create_app
from .db_connect import close_db, get_db

app = create_app()
app.secret_key = 'your-secret'  # Replace with an environment

# Register Blueprints
from app.blueprints.examples import examples
from app.blueprints.jerseys import jerseys
from app.blueprints.hats import hats
from app.blueprints.payment import payment
from app.blueprints.contact import contact

app.register_blueprint(examples, url_prefix='/example')
app.register_blueprint(jerseys, url_prefix='/jerseys')
app.register_blueprint(hats, url_prefix='/hats')
app.register_blueprint(payment, url_prefix='/checkout')
app.register_blueprint(contact, url_prefix='/contact')

from . import routes

@app.before_request
def before_request():
    g.db = get_db()
    if g.db is None:
        print("Warning: Database connection unavailable. Some features may not work.")

# Setup database connection teardown
@app.teardown_appcontext
def teardown_db(exception=None):
    close_db(exception)