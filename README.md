Requirements
---

    Python 2.7
    Virtualenv + Pip
    Pyramid
    SQLAlchemy
    SQlite

Steps to run the Server
---

```sh
git clone <repo_url>
cd <repo>
virtualenv .
source bin/activate
pip install Pyramid sqlalchemy pysqlite pyramid_chameleon
python server.py
# Navigate to http://localhost:8008/ or http://localhost:8008/bus/
```
