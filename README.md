# M2ICast #

## Setting up environment ##

* Run in root directory of the project
`virtualenv --no-site-packages --distribute -p python3 env`

* Run `source env/bin/activate` to activate the virtualenv, the environment should automatically activate, with a "(env)" in front of the PS1.

* `pip install -e .` will install the required packages.

* Install and set up Redis. 

* Set the SECRET\_KEY and the CELERY\_BROKER\_URL in settings.py to the appropriate values.
