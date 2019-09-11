import os
from flask import Blueprint, jsonify, render_template
from nerd_names_api.db import query_mysql

main = Blueprint('main', __name__)


@main.route('/')
def index():
	return render_template('index.html')


@main.route('/names')
def get_names():
	query = """
		SELECT *
		FROM nerd_names;
	"""
	results = query_mysql(query)
	results_json = {
		"results": results,
		"status": "OK"
	}
	return jsonify(results_json), 200
