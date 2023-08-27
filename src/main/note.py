from flask import Blueprint, request, render_template, url_for, redirect

from main.db import get_db

bp = Blueprint('note', __name__, url_prefix='/note')


@bp.route("/", methods=('GET', 'POST'))
def index():
    if request.method == "POST":
        print(request.form)
        title = request.form['title']
        db = get_db()
        db.execute(
            'INSERT INTO note (title) VALUES (?)',
            (title, )
        )
        db.commit()
        return redirect(url_for('note.index'))

    db = get_db()
    notes = db.execute(
        'SELECT * FROM note'
    ).fetchall()
    return render_template('note/index.html', notes=notes)
