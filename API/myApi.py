import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def return_files_tut():
    try:
        return flask.send_file('/home/ubuntu/NetworkMeasurement/API/parker.jpg',
                               attachment_filename='test.txt')
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
