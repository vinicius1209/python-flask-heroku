from app import db
from flask import flash, redirect, render_template, request, url_for, Blueprint
from app.models import Task

bp = Blueprint('app', __name__)

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/dashboard', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        if not name:
            flash('Task name is required.')
        else:
            db.session.add(Task(name=name))
            db.session.commit()

    tasks = Task.query.all()
    return render_template('dashboard.html', title='Dashboard', tasks=tasks)


@bp.route('/dashboard/<int:id>/delete', methods=['POST'])
def delete(id):
    task = Task.query.get(id)
    if task != None:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('index'))
