from flask import Flask
import datetime
  
x = datetime.datetime.now()
  
# Initializing flask app
app = Flask(__name__)
  
  
# Route for seeing a data
@app.route('/')
def sayshit():
  
    # Returning an api for showing in reactjs
    # interesting... shows in alphabetical order (not like it matters)
    return {
        'what happen':"AHH",
        "uhhhhhhh":"ooooooh",
        "Date":x,
        "programming":"actually JSON bruh"
        }

@app.route('/data')
def get_time():
  
    # Returning an api for showing in reactjs
    return {
        'Name':"AHH",
        "Age":"22",
        "Date":x,
        "programming":"python-flask"
        }
  
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)