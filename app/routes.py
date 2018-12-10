from flask import flash, redirect, render_template, request, url_for
from app import dashboard, db
from app.models import Task


@dashboard.route('/', methods=['GET', 'POST'])
@dashboard.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        name = request.form['name']
        if not name:
            flash('Task name is required.')
        else:
            db.session.add(Task(name=name))
            db.session.commit()

    tasks = Task.query.all()
    return render_template('dashboard.html', title='Dashboard', tasks=tasks)

@dashboard.route('/dashboard/<int:id>/delete', methods=['POST'])
def delete():
    task = Task.query.get(id)
    if task != None:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('dashboard'))

