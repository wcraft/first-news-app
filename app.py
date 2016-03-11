import csv
from flask import Flask
from flask import render_template
app = Flask(__name__)

def get_csv(csv_path):
    csv_file = open(csv_path, "rb")
    #DictReader returns a list of dictionaries
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

# This is going to route index.html file to the root
@app.route("/")
def index():
    template = "index.html"
    object_list = get_csv("./static/la-riots-deaths.csv")
    return render_template(template, object_list = object_list)

if __name__ == "__main__":
    # fires up the flask test server
    app.run(debug=True, use_reloader=True)
