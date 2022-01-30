from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Handling errors
@app.errorhandler(500)
def page_not_found(e):
    return {
        "error": "CONTEST ID OR THE LETTER OF THE QUESTION WAS NOT FOUND, MOST LIKELY BECAUSE THEY DON'T EXIST"
    }, 500

@app.route('/get_constellation', methods=['POST'])
def get_constellation():
    if request.method == "POST":
        print(123)
        req = request.data.decode("UTF-8")
        print(type(json.loads(req)))
        return req


if __name__ == '__main__':
    app.run(threaded=True, port=3000)