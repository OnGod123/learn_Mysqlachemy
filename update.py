user = session.query(User).filter_by(name='John').first()
user.age = 35
session.commit()
