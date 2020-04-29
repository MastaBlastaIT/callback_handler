# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
import os, git

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello from Flaskers!"


@app.route("/deploy_changes", methods=["POST"])
def deploy_changes():
    if request.method == "POST":
        repo = git.Repo("/home/mastaGateline/callback_handler")
        origin = repo.remotes.origin
        origin.pull()
        # origin.fetch()
        # repo.merge_base(repo.heads.master, origin.refs.master)
        return "Updated PythonAnywhere successfully", 200
    else:
        return "Wrong event type", 400
