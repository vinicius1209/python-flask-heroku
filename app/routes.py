from flask import render_template, redirect, request, flash, jsonify
from app import dashboard

@dashboard.route('/', methods=['GET'])
@dashboard.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html', title='Dashboard')