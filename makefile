export FLASK_APP=index.py
ifeq ($(OS),Windows_NT)
    PYTHON = venv\Scripts\python.exe
    PIP = venv\Scripts\pip.exe
    CLEANEXEC = rmdir /s /q venv
else
    PYTHON = venv/bin/python3
    PIP = venv/bin/pip
    CLEANEXEC = rm -rf venv
endif

.PHONY: run install venv clean

run:
	$(PYTHON) -m flask run

install: venv
	$(PIP) install -r requirements.txt

venv:
	python -m venv venv

clean:
	$(CLEANEXEC)
