from flask import Flask

app = Flask(__name__)

@app.route("/")
def Whats_up():
  return "What's up"

@app.route("/about")
def about():
  return "PAG ABOUT"

if __name__ == "__main__":
  app.run(debug=True)