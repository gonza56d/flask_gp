# Python
import pdb
# Flask
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


index_page = Blueprint('index_page', __name__, template_folder='templates')

@index_page.route('/')
def main_view():
    try:
        return render_template('index/main.html')
    except TemplateNotFound:
        abort(404)
