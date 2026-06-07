from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Hello , Data Scientist!"

@app.route('/about')
def about():
    return "about , Data Scientist!"

@app.route('/contact')
def contact():
    return "contact , Data Scientist!"
    
# if __name__ == '__main__':
app.run(debug = True)