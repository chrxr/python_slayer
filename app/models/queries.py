from models import User, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

session = Session()

results = session.query(User).first()

print(results.name)

for instance in session.query(User):
    print(instance.name, instance.fullname)
