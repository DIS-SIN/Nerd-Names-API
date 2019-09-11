import os
from flask import Blueprint, jsonify
from nerd_names_api.db import query_mysql

main = Blueprint('main', __name__)


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
