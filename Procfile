web: gunicorn medico.wsgi --chdir backend --limit-request-line 8188 --log-file -
worker: celery --workdir backend --app=medico worker -B --loglevel=info
beat: celery --workdir backend --app=medico beat -S redbeat.RedBeatScheduler --loglevel=info
