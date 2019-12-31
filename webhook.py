
from flask import Flask, request, abort
import subprocess

app = Flask(__name__)

def pull_and_restart():
    subprocess.run(['/opt/gitpull.sh'])
    return

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        github_json = request.get_json()
        print(github_json['ref'])
        if github_json['ref'] == 'refs/heads/staging' or github_json['ref'] == 'refs/heads/main' :
            pull_and_restart()
            return '', 200
    else:
        abort(400)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001)