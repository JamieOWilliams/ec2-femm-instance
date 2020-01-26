import copy
import os

from flask import Flask, request, send_from_directory
from femm import Interface

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './fem'


@app.route('/solve', methods=['POST'])
def solve():
    """Accept a POST request, mesh and solve the problem."""
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    interface = Interface(filename=os.path.splitext(filename)[0])
    interface.mesh()
    ans_filename = interface.solve()
    return send_from_directory(app.config['UPLOAD_FOLDER'], ans_filename, mimetype='application/octet-stream')


if __name__ == '__main__':
    app.run(host='0.0.0.0:80', port=80)
