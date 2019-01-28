import flask

app = flask.Flask(__name__,static_url_path='')
app.config["DEBUG"] = True


# @app.route('/', methods=['GET'])
# def home():
#     return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/',  methods=['GET'])
def home():
    return app.send_static_file('/NetworkMeasurement/API/homePage.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)