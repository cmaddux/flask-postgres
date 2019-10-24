.PHONY: test
test:
	docker exec -t api pytest
