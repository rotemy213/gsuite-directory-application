# Web application code

import config
import directory

from flask import Flask, render_template

# Create application object
app = Flask(__name__, template_folder='templates')

# Load configuration from config file
app.config.from_object(config)


@app.route("/")
def index():
	"""
	Default route for the application that returns the list of users
	:return: List view of all users
	"""
	users = directory.get_users()
	return render_template('list.html', users=users)


@app.route("/<id>")
def user(id):
	"""
	Route for a specific user object
	:param id: user's id in gsuite
	:return: User object as JSON
	"""
	user = directory.get_user(id=id)
	return user


@app.errorhandler(500)
def server_error(e):
	"""
	Error handler
	:param e: error
	:return: error string to be rendered
	"""
	return """
        An internal error occurred: <pre>{}</pre>
        See logs for full stacktrace.
        """.format(e), 500


if __name__ == '__app__':
	app.run()
