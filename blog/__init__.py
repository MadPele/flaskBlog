from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '7c67b2b1be150808714c2e59b4208d6b'

import blog.views
