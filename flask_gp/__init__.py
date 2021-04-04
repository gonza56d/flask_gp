# Flask
from flask import Flask
import flask_gp.views
# Project
from flask_gp.views import index_page, raceresults_page


app = Flask(__name__)
app.register_blueprint(index_page)
app.register_blueprint(raceresults_page)
