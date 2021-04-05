# Python
import pdb
# Flask
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
# Project
from flask_gp.services import CalendarService


index_page = Blueprint('index_page', __name__, template_folder='templates')


@index_page.route('/')
def main_view():
    try:
        template_data = CalendarService().get_circuits()
        return render_template('raceresults/main.html', **template_data)
    except TemplateNotFound:
        abort(404)
