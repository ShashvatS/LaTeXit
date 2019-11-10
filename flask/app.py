from flask import Flask, jsonify, request

app = Flask(__name__, static_url_path='', static_folder='../public')

@app.route('/')
def hello_world():
    return "hello_world"

counter = 0


@app.route('/send', methods=['POST'])
def yo():
    global counter
    
    print(request.data)
    print(request.files)
    file = request.files['file']
    file.save("upload/{}.png".format(counter))
    counter += 1
    print(file)
    print("yo")
    return "yo"


### curl -X POST localhost:5000/testtest

