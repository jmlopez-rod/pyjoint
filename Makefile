# pyjoint makefile

all: install-user

install:
	python setup.py install

install-user:
	python setup.py install --user

build:
	python setup.py sdist

develop:
	python setup.py develop --user

export:
	git archive --format zip --output pyjoint.zip master

clean:
	rm -rf pyjoint.egg-info
	rm -rf build

pypi:
	python setup.py sdist upload
