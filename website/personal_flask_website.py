# Import Flask library
# Import HTML template from flask: render_template
from flask import Flask, render_template

#Create an variable to store the Flask app object 
app = Flask(__name__)

#Create a decorator o view the webiste, # means homepage
@app.route('/')
#Create a function to define what they webpage does
#Render the home.html file on this url
def home():
    return render_template("home.html")

#Render the return string on this url
#Render the about.html file on this url
@app.route('/about/')
def about():
    # return "Website content goes here"
    return render_template("about.html")

#Conditional statement to run the code 
if __name__ == "__main__":
    app.run(port=5000, debug=True)