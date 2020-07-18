import json
import pandas as pd
import sqlite3
from sqlite3 import Error

from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def home():
    with open("data.json", "r") as read_file:
        data = json.load(read_file)
    data_frame = pd.DataFrame(data)
    return render_template('record.html',   tables=[data_frame.to_html(classes='data')], titles=data_frame.columns.values)

if __name__ == '__main__':
    app.run(debug=True)


