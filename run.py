from flask import Flask
from flask_cors import CORS
import logging

_logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)


####################################################################
# Main
####################################################################

@app.route("/")
def hello():
    return "The Horribly Fast Api with Extremely Efficient Endpoints by Lucas Ferreira"



if __name__ == "__main__":
    app_port = 8080
    app.run(debug=False, port=app_port, host='0.0.0.0', use_reloader=False)