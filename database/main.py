import sqlalchemy
from sqlalchemy import Table, Column, Integer, Text #, Model
import pandas as pd
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import UserDefinedType

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


db = sa.create_engine('postgresql+psycopg2://admin:admin@127.0.0.1:5432/db_stickers')
# ensure this is the correct path for the sqlite file.

base = declarative_base()


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)



from sqlalchemy.dialects.postgresql import TSVECTOR

class TSVector(sa.types.TypeDecorator):
    impl = TSVECTOR


class Stickers(base):
    __tablename__ = "stickers"
    sticker_id = sa.Column(sa.Integer(), primary_key=True)
    descr = sa.Column(sa.Text())
    file_id = sa.Column(sa.Text())
    sticker_set_name = sa.Column(sa.Text())
    file_unique_id = sa.Column(sa.Text())

    __ts_vector__ = sa.Column(TSVector(), sa.Computed(
        "to_tsvector('english', descr)",
         persisted=True))

    __table_args__ = (sa.Index('ix_stickers___ts_vector__',
          __ts_vector__, postgresql_using='gin'),)


def main():
    sts = session.query(Stickers)
    for st in sts:
        print(st.descr)

    results = session.query(Stickers).filter(Stickers.__ts_vector__.match('die')).all()
    for st in results:
        print(st.descr)



if __name__ == "__main__":
    main()
