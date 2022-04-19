#!/bin/sh

set -e

gunicorn --bind 0.0.0.0:8001 -w 4 --limit-request-line 6094 --access-logfile - src.wsgi:application
# newrelic-admin run-program gunicorn --bind 0.0.0.0:8001 --access-logfile - src.wsgi:application
