
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from Task6_models import create_tables


login = 'postgres'
password = 'Maxim0055!!!'
db_name = 'Task6'

DSN = f'postgresql://{login}:{password}@localhost:5432/{db_name}'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind = engine)
session = Session()

session.close()
