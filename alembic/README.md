# Alembic Tutorial

[](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

* Initial alembic environment
  * `venv/bin/alembic init sample/alembic`
  * `alembic.ini` created at local path
* Editing the .ini File
  * `sqlalchemy.url=sqlite:////tmp/portal.db`
  * <https://docs.sqlalchemy.org/en/14/dialects/sqlite.html#dialect-sqlite-pysqlite-connect>
* Create a migration script
  * `alembic revision -m "init tables"`
  * `code alembic/versions/9f250c8198bc_init_tables.py`
* Running our first migration
  * `alembic upgrade head`
* Getting Information
  * `alembic current`
  * `alembic history --verbose`
* Running our first migration
  * `alembic downgrade base`

## Generate ER Diagram

* Create `/tmp/portal.db`
  * `cd alembic`
  * `alembic upgrade head`
* Explore by command line
  * `sqlite3 /tmp/portal.db`
* Launch `DataGrip`
  * connect to /tmp/portal.db
  * portal.db -> schemas -> (select all tables) -> Diagrams -> show virualizations ...