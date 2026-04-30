# HW-5: SQLAlchemy + Alembic + PostgreSQL

## Setup

1. Start PostgreSQL in Docker:

```bash
docker run --name hw5-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

2. Create and activate virtualenv, then install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure DB URL (optional, default is already set):

```bash
set DATABASE_URL=postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/postgres
```

4. Run migrations:

```bash
alembic upgrade head
```

5. Seed database:

```bash
python seed.py
```

## Files

- `database.py` - engine/session configuration.
- `models.py` - SQLAlchemy models.
- `seed.py` - random data generator.
- `my_select.py` - 10 select queries as functions.
- `alembic/` - migration configuration and revisions.
