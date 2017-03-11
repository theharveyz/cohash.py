ENV_DIR=cohash-venv

init:
	@( \
		pip install --upgrade pip setuptools; \
		pip install virtualenv; \
		virtualenv  $(ENV_DIR) ;\
	)

clean-env:
	rm -fr ./$(ENV_DIR)

.PHONY: exit init
