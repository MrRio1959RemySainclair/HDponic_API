# app.py

from flask import render_template 
import config
from models import DATA

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

@app.app.route("/")
def home():
    data_home = DATA.query.all()
    return render_template("home.html", data=data_home)

if __name__ == "__main__":
    app.run("app:app", host="0.0.0.0", port=8000, reload=True)