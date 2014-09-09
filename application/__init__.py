###############################################################################
##           Created by the Pitt Python Linguistics Group                     #
##           https://github.com/PittPythonLinguisticsGroup                    #
###############################################################################
# Import from standard library here:


# Import packages here:
from flask import Flask, render_template

# Create Flask app object:
app = Flask(__name__)

# Create new views here:
@app.route('/')
def index():
    "This should return whatever we have decided the main page will be."
    return render_template('index.html')

