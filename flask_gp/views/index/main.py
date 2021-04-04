from flask import render_template, abort
from jinja2 import TemplateNotFound
from . import index_page


@index_page.route('/')
def main():
    try:
        return render_template('index/main.html')
    except TemplateNotFound:
        abort(404)
