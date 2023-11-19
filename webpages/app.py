from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/<path:filename>')
def download_file(filename):
    return send_from_directory('C:\\Users\\kithm\\OneDrive\\Desktop\\localbank\\webpages\\templates', filename)

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
