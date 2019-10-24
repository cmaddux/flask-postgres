.PHONY: test
test:
	docker exec -t api pytest

.PHONY: migrate
migrate:
	docker exec -t api alembic upgrade head

.PHONY: migrate-rollback
migrate-rollback:
	docker exec -t api alembic downgrade -1
