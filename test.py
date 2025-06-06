# In your app.py file (or whatever your app file is named)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"

if __name__ == "__main__":
  app.run(debug=True) # Optional: enable debug mode for development