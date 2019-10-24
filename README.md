# Falcon - Postgres Base

A base template for a simple Falcon API and Postgres stack using Alembic for migrations.

## Usage

1. Clone repo
2. Run `docker-compose up`
3. Run `make test`

## Migrations

To migrate forward, run `make migrate`.

To rollback most recent migrations, run `make migrate-rollback`.

To create a new migration:

1. Run `docker exec -it api alembic revision -m "{{NAME OF REVISION}}"`
2. Locate revision in alembic/revisions directory
3. Run `sudo chown ${USER}:${USER} {{REVISION FILE}}`
4. Run `chmod 664 {{REVISION FILE}}`
