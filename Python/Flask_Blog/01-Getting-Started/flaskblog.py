from flask import Flask
app = Flask(__name__)

#decorators are ways to add additional functionality to existing function 
#we can have multiple routes handle by the same function 
@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"


@app.route("/about")
def about():
    return "<h1>About Page</h1>"


if __name__ == '__main__':
    # help us to see changes each time we save the filenin real time 
    app.run(debug=True)
