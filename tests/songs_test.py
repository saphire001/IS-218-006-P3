import os

from flask_login import current_user

from app import db
from app.db.models import User, Song

def test_csv_upload(application):
    with application.app_context():
        db.session.query(User).count() == 0
        db.session.query(Song).count() == 0

        user = User('keith@webizly.com', 'testtest')
        db.session.add(user)

        user.songs = [Song("T","jgk","2134","jfk"), Song("T2","djf","2342","sdj")]
        db.session.commit()
        assert db.session.query(Song).count() == 2

        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0



