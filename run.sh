#!/bin/bash

export FLASK_APP=backend/main.py
export FLASK_DEBUG=1
flask run --host=0.0.0.0
