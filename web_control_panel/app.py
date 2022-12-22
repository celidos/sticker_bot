from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import sqlalchemy as sa

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@localhost/db_stickers'

db = SQLAlchemy(app)


class Stickers(db.Model):
    __tablename__ = "stickers"
    sticker_id = sa.Column(sa.Integer(), primary_key=True)
    descr = sa.Column(sa.Text())
    file_id = sa.Column(sa.Text())
    sticker_set_name = sa.Column(sa.Text())
    file_unique_id = sa.Column(sa.Text())


@app.route('/stickers/<int:page_num>')
def sticker(page_num):
    sts = Stickers.query.paginate(per_page=5, page=page_num, error_out=True)
    return render_template('index.html', sticker=sts)


if __name__ == '__main__':
    app.run(debug=True)