user = session.query(User).filter_by(name='John').first()
session.delete(user)
