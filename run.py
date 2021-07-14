from flask import Flask
from flask_cors import CORS
import logging

from app.endpoints.status import blueprint as status_bp

_logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)


####################################################################
# Main
####################################################################

app.register_blueprint(status_bp)

@app.route("/")
def hello():
    return "The Horribly Fast Api with Extremely Efficient Endpoints by Lucas Ferreira"


if __name__ == "__main__":
    app.run(debug=False, port=8080, host='0.0.0.0', use_reloader=False)