import ipaddress
from datetime import datetime

from database.QueryBuilder import QueryBuilder
from database.db import BanHeimDB
from database.table import ReportedTable


class IP:
    """Represent IP¨(as IPv4 and IPv6)"""

    def __init__(self, ip):
        ipo = ipaddress.ip_address(ip)
        self.ip = ipo.compressed
        self.ipset = []

    @staticmethod
    def is_address(ip):
        try:
            if "/" in ip:
                ip = ip.split("/")[0]
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_network(ip):
        try:
            ipo = ipaddress.ip_network(ip, True)
            if ipo.prefixlen == "/32" or ipo.prefixlen == "/128":
                return False
            return True
        except ValueError:
            return False

    def add_report(self, reporter, reason, timestamp=datetime.now()):
        db = BanHeimDB("sqlite:///test.db")
        qb = QueryBuilder(db)

        qb.insert(ReportedTable(self.ip, reporter, timestamp, reason))
