#!/bin/bash

NAME="trello-poli"
DJANGODIR=$(dirname $(cd `dirname $0` && pwd))
SOCKFILE=/tmp/gunicorn-trello.sock
LOGDIR=${DJANGODIR}/logs/gunicorn.log
USER=rick
GROUP=rick
NUM_WORKERS=5
DJANGO_WSGI_MODULE=sgpa.wsgi

rm -frv $SOCKFILE

echo $DJANGODIR

cd $DJANGODIR
pipenv shell
exec ${DJANGODIR}/env/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=$LOGDIR