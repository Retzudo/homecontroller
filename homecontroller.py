#!/usr/bin/env python2

from flask import Flask, render_template, jsonify
import wol, json

app = Flask(__name__)
app.debug = True

computer_list = {
    'PC':     '48:5B:39:C9:67:A3',
    'Server': '6c:62:6d:8d:8b:dd',
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/computers')
def computers():
    return jsonify(computer_list)


@app.route('/boot/<computer>')
def boot(computer):
    if computer not in computer_list:
        abort(404)

    wol.send_magic_packet(computer_list[computer])
    return 'Booting...'


if __name__ == '__main__':
    app.run('0.0.0.0', 80)
