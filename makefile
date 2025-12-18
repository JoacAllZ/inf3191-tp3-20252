ifeq ($(OS),Windows_NT)
    PYTHON = venv\Scripts\python.exe
    PIP = venv\Scripts\pip.exe
    CLEANEXEC = rmdir /s /q venv
	PYTHON_GLOBAL = python
else
    PYTHON = venv/bin/python3
    PIP = venv/bin/pip
    CLEANEXEC = rm -rf venv
	PYTHON_GLOBAL = python3
endif

.PHONY: run install clean

run: install
	$(PYTHON) -m flask --app index run

install: venv
	$(PIP) install -r requirements.txt

venv:
	$(PYTHON_GLOBAL) -m venv venv

clean:
	$(CLEANEXEC)
