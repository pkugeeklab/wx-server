The config file `secret.conf` should be set correctly.

# Usage ( developing )
1. `pip3 install -r requirements.txt`
2. `python3 main.py`

# Usage ( deploying )
1. `pip3 install gunicorn`
2. `gunicorn main:app -c gunicorn_config.py` 

Maybe supervised should be set correctly to optimized the running process.
