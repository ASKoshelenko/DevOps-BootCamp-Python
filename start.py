from flask import Flask, render_template, request, redirect, url_for
from handlers.pull_requests import get_pull_requests

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect(url_for('pull_requests'))

@app.route('/pull_requests')
def pull_requests():
    state = request.args.get("state", "open")
    pull_requests = get_pull_requests(state)
    return render_template("pull_requests.j2", pull_requests=pull_requests)

if __name__ == '__main__':
    app.run(debug=True)
