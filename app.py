from flask import Flask
from flask import render_template
app = Flask(__name__)

# This is going to route index.html file to the root
@app.route("/")
def index():
    template = "index.html"
    return render_template(template)

if __name__ == "__main__":
    # fires up the flask test server
    app.run(debug=True, use_reloader=True)
