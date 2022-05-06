<h3 align="center">BanHeim</h3>

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 

</div>

## 📝 Table of Contents

- [About](#about)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>
A server that hosts an API that allows the client to remount malicious IPs.

The idea is that the clients will send the IPs banned by fail2ban to the server, and if the same IP is received several times the server will take the decision to ban the IP on all clients.

It will send a message on a SSE stream, and the clients will do the action according to what is received.

Having a restricted pool of client machines, we will also report the IPs globally to [AbuseIPDB](https://www.abuseipdb.com/), and we will retrieve the blacklist from the latter to protect all our machines.

## ℹ Informations <a name = "informations"></a>

We use [gitmoji](https://gitmoji.dev/) for our commit messages

### Technologies we use
- [Python](https://www.python.org/) - Programming Language
- [MariaDB](https://mariadb.org/documentation/) - To store every data
- [Redis](https://redis.io/) - To enqueue jobs and use worker
- [Docker](https://www.docker.com/) - To deploy this server

### Python Librairies
- [ipaddress](https://docs.python.org/3/library/ipaddress.html) - To add some check on string
- [Flask](https://flask.palletsprojects.com/en/2.1.x/) - To create the web server
- [SQLAlchemy](https://www.sqlalchemy.org/) - To manage database using python
- [RQ](https://python-rq.org/docs/jobs/) - To create workers

## ✍️ Authors <a name = "authors"></a>
- [@Zerka30](https://github.com/Zerka30) - creator and developer