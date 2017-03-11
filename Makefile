ENV_DIR=cohash-venv

init:
	@( \
		pip install --upgrade pip setuptools twine; \
		pip install virtualenv; \
		virtualenv  $(ENV_DIR) ;\
	)

clean-env:
	rm -fr ./$(ENV_DIR)

.PHONY: exit init
