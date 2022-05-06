from datetime import datetime

from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class IPSetTable(Base):
    """Representation of IPSet Table"""

    __tablename__ = "ipset"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(255), unique=True, nullable=False)
    timestamp = Column(
        "timestamp", TIMESTAMP(timezone=False), nullable=False, default=datetime.now()
    )

    def __init__(self, name, timestamp=datetime.now()):
        self.name = name
        self.timestamp = timestamp


class IPTable(Base):
    """Representation of IP Table"""

    __tablename__ = "ip"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    ip = Column("ip", String(255), nullable=False)
    ipset_id = Column("ipset_id", Integer, ForeignKey("ipset.id"))
    network_range = Column("network_range", Boolean, nullable=False)
    hardstate = Column(
        "hardstate", Integer, ForeignKey("iphardstates.id"), nullable=True
    )
    date = Column(
        "date", TIMESTAMP(timezone=False), nullable=False, default=datetime.now()
    )

    def __init__(
        self, ip, ipset_id, network_range, date=datetime.now(), hardstate=None
    ):
        self.ip = ip
        self.ipset_id = ipset_id
        self.network_range = network_range
        self.date = date


class IPHardState(Base):
    """Representation of IPHardState Table"""

    __tablename__ = "iphardstates"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    hardstate = Column("hardstate", String(255), nullable=True)
    reason = Column("reason", String(255), nullable=True)

    def __init__(self, hardstate, reason):
        self.hardstate = hardstate
        self.reason = reason


class ReportedTable(Base):
    """Representation of Reported Table"""

    __tablename__ = "reported"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    ip = Column("ip", String(255), nullable=False)
    machine = Column("machine", String(255), nullable=False)
    timestamp = Column(
        "timestamp", TIMESTAMP(timezone=False), nullable=False, default=datetime.now()
    )
    reason = Column("reason", String(255), nullable=True)

    def __init__(self, ip, machine, timestamp=datetime.now(), reason=""):
        self.ip = ip
        self.machine = machine
        self.timestamp = timestamp
        self.reason = reason
