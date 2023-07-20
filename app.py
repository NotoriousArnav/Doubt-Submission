from flask import (
    Flask, 
    render_template, 
    request, 
    redirect, 
    url_for, 
    jsonify
)
from flask_sqlalchemy import SQLAlchemy
import subprocess
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///doubts.db'
db = SQLAlchemy(app)

class Doubt(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()), unique=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    doubt = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"<Doubt {self.id}>"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        doubt = request.form['doubt']
        print(
            f"""
                {name}
                {email}
                {doubt}
            """
        )
        d = notify_send(doubt, f"New Doubt by {name}")
        new_doubt = Doubt(id=str(uuid.uuid4()),name=name, email=email, doubt=doubt)
        db.session.add(new_doubt)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('index.html')

def notify_send(message, title="New Doubt"):
    p = subprocess.Popen(['notify-send', title, message])
    return True, p

if __name__ == '__main__':
    with app.app_context():db.create_all()
    app.run(debug=True)

