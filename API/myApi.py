import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# @app.route('/', methods=['GET'])
# def home():
#     return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# @app.route('/home/ubuntu/NetworkMeasurement/API/<path:filename>')
# def home(filename):
#     return flask.send_from_directory(app.config['/home/ubuntu/NetworkMeasurement/API/test.txt'],
#                                      filename,
#                                      as_attachment=True)

@app.route('/')
def return_files_tut():
    try:
        return flask.send_file('/home/ubuntu/NetworkMeasurement/API/test.txt',
                               attachment_filename='test.txt')
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
