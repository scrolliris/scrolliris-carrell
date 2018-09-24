ifeq (, $(ENV))
	ENV := development
	env := development
else ifeq (test, $(ENV))
	env := testing
else
	env := $(ENV)
endif

ifeq (, $(NODE_ENV))
	NODE_ENV := development
endif

app := rapperswil_jona

.DEFAULT_GOAL = test\:coverage
default: test\:coverage


# -- setup

setup:  ## Install Python packages
	pip install -e '.[${env}]' -c constraints.txt
.PHONY: setup

setup\:force:  ## Install Python packages with `--force-reinstall`
	pip install --upgrade --force-reinstall -e '.[${env}]' -c constraints.txt
.PHONY: setup\:force

setup\:update:  ## Update Python packages
	pip install --upgrade -e '.[${env}]' -c constraints.txt
.PHONY: setup\:update


# -- serve

serve:  ## Run server process (development)
	./bin/serve --env development --config config/development.ini --reload
.PHONY: serve

serve\:production:  ## Run {server,worker} process both in production mode (see Procfile)
	honcho start
.PHONY: serve\:production


# -- test

test:  ## Run unit tests and functional tests both
	ENV=test py.test -c 'config/testing.ini' -s -q \
	  test/unit test/func test/route_test.py
.PHONY: test

test\:unit:  ## Run unit tests
	ENV=test py.test -c 'config/testing.ini' -s -q \
	  test/unit
.PHONY: test\:unit

test\:func:  ## Run functional tests
	ENV=test py.test -c 'config/testing.ini' -s -q \
	  test/func
.PHONY: test\:func

test\:route:  ## Run only route tests
	ENV=test py.test -c 'config/testing.ini' -s -q \
	  test/route_test.py
.PHONY: test\:route

test\:integration:  ## Run integration tests on browser (Firefox Headless)
	ENV=test TEST_DOMAIN=localhost TEST_SESSION_COOKIE_DOMAIN=localhost \
	  py.test -c 'config/testing.ini' -s -v \
	  --driver Firefox --driver-path ./bin/geckodriver test/integration
.PHONY: test\:integration

test\:doc:  ## Run doctest in Python code
	ENV=test ./bin/run_doctest
.PHONY: test\:doc

test\:coverage:  ## Run `test` with coverage outputs
	ENV=test py.test -c 'config/testing.ini' -s -q \
	  test/unit test/func \
	  --cov=${app} --cov-report term-missing:skip-covered
.PHONY: test\:coverage


# -- vet

vet: | vet\:style vet\:lint  ## Run `vet:style` and `vet:lint` both (without vet:quality)
.PHONY: vet

vet\:style:  ## Check style using py{code,doc}style (see setup.cfg)
	pycodestyle test ${app}
	pydocstyle test ${app}
.PHONY: vet\:style

vet\:lint:  ## Lint python codes
	pylint test ${app}
.PHONY: vet\:lint


# -- utilities

pack:  ## Assemble assets using rollup
	NODE_ENV=$(NODE_ENV) rollup -c
.PHONY: pack

build: | setup pack ## (Re) Run setup and pack at once
.PHONY: build

clean:  ## Delete unnecessary cache etc.
	find . ! -readable -prune -o \
	  ! -path "./.git/*" ! -path "./node_modules/*" ! -path "./venv*" \
	  ! -path "./doc/*" ! -path "./locale/*" ! -path "./tmp/*" \
	  ! -path "./lib/*" -print | \
	  grep -E "(__pycache__|\.egg-info|\.pyc|\.pyo)" | \
	  xargs rm -rf
.PHONY: clean

shell:  ## Open python REPL in application context
	ENV=$(ENV) ${app}_pshell 'config/${env}.ini#${app}' --python-shell ptpython
.PHONY: shell

routes:  ## Display all routes for the application
	ENV=$(ENV) ${app}_proute 'config/${env}.ini#${app}'
.PHONY: routes

expose:  ## Print untracked (volatile) files
	git ls-files --others | \
	  grep -vE '(lib|tmp|test|static|db|locale|node_modules|\.?cache)/' | \
	  grep -vE '(__pycache__|\.egg-info|venv)/' | \
	  grep -vE '(\.coverage|\.*-version|bin\/gitlab*)'
.PHONY: expose

help:  ## Display this message
	@grep -E '^[0-9a-z\:\\]+: ' $(MAKEFILE_LIST) | grep -E '  ## ' | \
	  sed -e 's/\(\s|\(\s[0-9a-z\:\\]*\)*\)  /  /' | tr -d \\\\ | \
	  awk 'BEGIN {FS = ":  ## "}; {printf "\033[36m%-17s\033[0m %s\n", $$1, $$2}' | \
	  sort
.PHONY: help
