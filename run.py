import os
from flask import Flask, render_template

# create an instance of the above and store it in a var called app.
# The first argument of the Flask class, is the name of
# the application's module - our package.
# Since we're just using a single module, we can use __name__
# which is a built-in Python variable.
# Flask needs this so that it knows where to look for templates
# and static files.
app = Flask(__name__)


# using app.route decorator.When we try to browse to the root directory,
# as indicated by the "/",
# then Flask triggers the index function underneath and returns
# the "Hello, World" text.
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html", page_title="About")


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact" )


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


# The word 'main' wrapped in double-underscores (__main__) is the name of
# the default module in Python.
# This is the first one that we run, so if this has not been imported,
# which it won't be, then it's going to be run directly.
# Then we want to run our app using the arguments
# that we've passing inside of this statement.
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True) 
# we should never have "debug=True" in a production application, or when
# we submit our projects for assessment.
# This is very important, because having debug=True can allow
# arbitrary code to be run, and obviously this is a security flaw.
# You should only have debug=True while testing your application in development
# mode, but change it to debug=False before you submit your project.
