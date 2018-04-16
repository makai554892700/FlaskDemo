from . import user
from app.models import User
from .. import db


@user.route('/<user_id>', methods=['GET', 'POST'])
def index(user_id):
    user = User(user_id=user_id, username='test', age=18, phone='18621111111')
    db.session.add(user)
    db.session.commit()
    return 'hello world main.'
