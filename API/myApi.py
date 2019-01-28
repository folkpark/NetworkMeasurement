import flask

app = flask.Flask(__name__,static_url_path='/NetworkMeasurement/API/')
app.config["DEBUG"] = True


# @app.route('/', methods=['GET'])
# def home():
#     return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/NetworkMeasurement/API/<path:path>',  methods=['GET'])
def send_js(path):
    return flask.send_from_directory('homePage.html', path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)