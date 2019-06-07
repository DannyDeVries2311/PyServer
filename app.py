from flask import Flask, request, abort, jsonify
import logging


app = Flask(__name__)



@app.route("/")
def hello():
    return "Hello World!"

@app.route("/temp", methods=['GET','POST'])
def temp():
    #""" Test to send value and receive value """
    if request.method == 'POST':
        average_time = request.form.get('average_time')
        logging.warning("Test post")
        #return "Hello World Post!"
     
    # request.method == 'GET'
    return "Hello World Get!"

@app.route('/foo', methods=['POST']) 
def foo():
    if not request.json:
        abort(400)
    print(request.json)
    #json_data = json.loads(request.json)
    #json_string = json.dumps(request.json)
    return json.dumps(request.json)


if __name__ == '__main__':
    app.run(debug=True)

