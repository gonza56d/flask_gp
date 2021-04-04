# Python
# import pdb
# Flask
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
# Project
from flask_gp.services import RaceResults


raceresults_page = Blueprint('raceresults_page', __name__, template_folder='templates')

@raceresults_page.route('/race_results')
def main_view():
    try:
        template_data = RaceResults().get_race_results()
        return render_template('raceresults/main.html', **template_data)
    except TemplateNotFound:
        abort(404)
