# """ The flask app that handles lambda functions for all Spectrum accounts """
# #!/usr/local/bin/python
# # -*- coding: utf-8 -*-

from flask import Flask, request

app = Flask(__name__)

@app.route("/todos", methods=["GET"])
def kick_off_login():

  return "Success", 200