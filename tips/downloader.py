from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

    
@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        print('File not found')
        return 'File not found'

    file = request.files['file']

    if file.filename == '':
        print('File not selected')
        return 'File not selected'
        
    file.save(file.filename)
    print('Success')
    return 'Success'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9002, debug=False)