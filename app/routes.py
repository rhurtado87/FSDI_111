from flask import Flask         #from the flask module import the Flask class

app = Flask(__name__)           # Create an instance of the Flask classs   

@app.get("/about")
@app.et("/")                   #Flask decorator that maps view functions to routes
def index():                    #view function
    me = {                      #python dictionary 
        "first_name": "Ricardo",
        "last_name": "Hurtado",
        "hobbies": "TCG",
        "is_online": True
    }
    return me         #when you return a dict from a view fanction, it becomes JSON

