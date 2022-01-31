from flask import Flask, request, jsonify
import json, numpy
from flask_cors import CORS
from simbad_querying import get_view
from plotting_hemis import plot_polar

app = Flask(__name__)
CORS(app)

# Handling errors
@app.errorhandler(500)
def page_not_found(e):
    return {
        "error": "CONTEST ID OR THE LETTER OF THE QUESTION WAS NOT FOUND, MOST LIKELY BECAUSE THEY DON'T EXIST"
    }, 500

@app.route('/get_constellation', methods=['POST'])
def get_constellation():
    if request.method == "POST":
        req = request.data.decode("UTF-8")
        latLong = json.loads(req)
        fig = get_view(latLong["latitude"], latLong["longitude"], 1)
        return json.dumps(fig.tolist())


if __name__ == '__main__':
    app.run(threaded=True, port=3000)