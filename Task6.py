import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from Task6_models import create_tables, Publisher, Book, Shop, Stock, Sale


login = 'postgres'
password = 'Maxim0055!!!'
db_name = 'Task6'

DSN = f'postgresql://{login}:{password}@localhost:5432/{db_name}'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind = engine)
session = Session()

with open('tests_data.json', 'r', encoding = 'UTF-8') as file:
    data = json.load(file)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
session.commit()

print('Введите номер издателя для отчета:')
for pb in session.query(Publisher).all():
    print(pb)

choice = int(input())

subq1 = session.query(Publisher).filter(Publisher.id == choice).subquery()
subq2 = session.query(Book).join(subq1, Book.id_publisher == subq1.c.id).subquery()
subq3 = session.query(Stock).join(subq2, Stock.id_book == subq2.c.id).subquery()
for result in session.query(Sale).join(subq3, Sale.id_stock == subq3.c.id).all():
    print(result)

session.close()
