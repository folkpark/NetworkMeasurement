import flask

app = flask.Flask(__name__,static_url_path='')
app.config["DEBUG"] = True


# @app.route('/', methods=['GET'])
# def home():
#     return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/uploads/<path:filename>')
def home(filename):
    return flask.send_from_directory('/home/ubuntu/NetworkMeasurement/API/test.txt',filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)