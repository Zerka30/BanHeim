from sqlalchemy import delete, select

import database.table as Table
from database.db import BanHeimDB


class QueryBuilder:
    """Easy way to build SQLAlchemy query"""

    def __init__(self, db: BanHeimDB):
        self.db = db

    # Select methods
    def select(
        self, *table: Table, join: Table = None, from_table: Table = None, **filters
    ):
        """
        Select specific row by filtering

        Usage : db.select(Table_to_select, filters)

        """
        if from_table is None:
            from_table = table[0]

        if join is None:
            return select(*table).filter_by(**filters)
        else:
            return select(*table).join(join).filter_by(**filters)

    # Insert methods
    def insert(self, *table: Table):
        self.db.session.add_all(table)
        self.db.session.commit()

    # Delete methods
    def delete(self, table: Table, *whereclause):
        self.db.session.execute(delete(table).where(*whereclause))
        self.db.session.commit()
