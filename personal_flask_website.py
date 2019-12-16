from flask import Flask

#Create an variable to store the Flask app object 
app = Flask(__name__)

#Create a decorator o view the webiste, # means homepage
@app.route('/')
#Create a function to define what they webpage does
def home():
    return "Website content goes here"

#Conditional statement to run the code 
if __name__ == "__main__":
    app.run(port=5000, debug=True)