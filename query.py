# Query all users
all_users = session.query(User).all()
for user in all_users:
    print(user.id, user.name, user.age)

# Query a specific user
user = session.query(User).filter_by(name='John').first()
print(user.id, user.name, user.age)

