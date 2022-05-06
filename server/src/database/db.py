from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import delete

import database.table as Table


class BanHeimDB:
    """Easy way to manage DB"""

    def __init__(self, db_url):
        self.engine = create_engine(db_url, echo=False)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def get_engine(self):
        """Returning DB engine"""
        return self.engine

    def clear(self, table: Table):
        """Simple way to purge all entries from table"""
        self.execute(delete(table))
        self.session.commit()

    def execute(self, statement):
        """Execute any statement"""
        return self.session.execute(statement)
