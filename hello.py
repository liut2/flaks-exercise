from flask import Flask, render_template, redirect, session, flash 
#from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired
app = Flask(__name__)
#Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'

class Course_review_form(Form):
	name = StringField("what is your name?", [DataRequired()])
	submit = SubmitField("submit it")

@app.route("/")
def about():
	return render_template("home.html")

@app.route("/success")
def success():
	name = session.get("name")
	return render_template("success.html", name = name)

@app.route("/contact/", methods=["GET", "POST"])
def contact():
	
	form = Course_review_form()
	if form.validate_on_submit():
		
		session["name"] = form.name().data
		form.name().data = ""
		return redirect("/success")

		

	return render_template("contact.html", form = form)

if __name__ == "__main__":
	app.run(debug = True)
