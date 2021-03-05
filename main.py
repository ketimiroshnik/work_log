from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    param = {}
    mas = []
    sess = db_session.create_session()
    for job in sess.query(Jobs).all():
        d = {}
        d["title"] = job.job
        user = sess.query(User).filter(User.id == job.team_leader)[0]
        d["team_leader"] = f'{user.surname} {user.name}'
        d["work_size"] = job.work_size
        d["collaborators"] = job.collaborators
        d["finished"] = job.is_finished
        mas.append(d)
    param["mas"] = mas
    return render_template('jobs_view.html', **param)



if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")
    app.run(0)

