from flask import Flask
from flask import request, render_template

 
app = Flask(__name__)
 
@app.route('/')

def index():
   name = 'Anya'
   surname = 'Kostyuchenko'
   left_menu = [{'name':'Overview','icon':'/static/assets/chart (14).png'}]
   return  render_template('index.html', name = name, surname = surname, left_menu = left_menu)

if __name__ == "__main__":
    app.run(debug = True)