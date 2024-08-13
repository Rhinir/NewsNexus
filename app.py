from flask import Flask, render_template, request, send_file
import os
from flask import send_from_directory, redirect

from scraper3 import *

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug = True)