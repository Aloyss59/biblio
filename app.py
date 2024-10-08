from flask import Flask, render_template, request, jsonify, redirect, session, url_for, flash, abort
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from db import CreateTable
import os, uuid, base64, pytz, psutil, time, random, ssl, string, pyotp, logging

# Créez l'application Flask
app = Flask(__name__, template_folder='./flaskr/templates', static_folder='./flaskr/static')

@app.route('/')
def index():
    return render_template('principale.html')

def login():
    return render_template('auth/login.html')

@app.route('/register')
def register():
    return render_template('auth/register.html')

if __name__ == '__main__':
    CreateTable()
    app.run(debug=True, host='0.0.0.0', port=5000)