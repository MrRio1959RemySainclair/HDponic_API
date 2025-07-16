# API

from flask import render_template
import config
from models import Datas


app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

@app.app.route("/")
def home():
    data = Datas.query.all()
    return render_template("home.html", data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, log_level="info")
