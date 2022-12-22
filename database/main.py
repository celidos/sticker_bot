import sqlalchemy
from sqlalchemy import Table, Column, Integer, Text
import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import UserDefinedType

db_engine = sqlalchemy.create_engine('sqlite:////home/celidos/Documents/GIT/sticker_bot/database/db_stickers.sqlite')
# ensure this is the correct path for the sqlite file.

Session = sessionmaker(bind=db_engine)
session = Session()

meta = sqlalchemy.MetaData()

Stickers = sqlalchemy.Table(
    'stickers',
    meta,
    Column('sticker_id', Integer, primary_key=True),
    Column('descr', Text),
    Column('file_id', Text),
    Column('sticker_set_name', Text),
    Column('file_unique_id', Text)
)


def main():
    context = type('', (), {})()



    sts = Stickers.select()#.filter(Stickers.descr.like(u'%press%'))
    conn = db_engine.connect()
    result = conn.execute(sts)

    print('Hello!')
    for row in result:
        print(row)

    q_req = session.query(Stickers).filter(Stickers.c.descr.op("MATCH")("press")).all()
    q_res = conn.execute(q_req)
    print(q_res)



if __name__ == "__main__":
    main()
