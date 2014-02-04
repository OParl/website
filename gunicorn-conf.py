workers = 3
bind = '127.0.0.1:5001'
accesslog = '/home/oparl/logs/gunicorn/oparl.access.log'
errorlog = '/home/oparl/logs/gunicorn/oparl.error.log'
proc_name = 'oparl'
loglevel = 'info'
