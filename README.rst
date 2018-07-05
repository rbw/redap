.. code-block::

                      __
       ________  ____/ /___ _____
      / ___/ _ \/ __  / __ `/ __ \
     / /  /  __/ /_/ / /_/ / /_/ /
    /_/   \___/\__,_/\__,_/ .___/
       HTTP/LDAP Gateway /_/


Adding LDAP support can be time-consuming, tedious and complex — but it doesn't have to be.

Redap runs in an easily deployable micro-service which exposes a REST interface for interacting with LDAP-capable directory servers over HTTP/S.

Features
------

Redap was partly inspired by and is conceptually similar to `dthree/addict <https://github.com/dthree/addict>`_, but offers more features:


- RESTful HTTP API
- API key authorization
- Simple and straightforward schemas
- ldap3 *Simplified Query Language* for querying
- LDAP debugging
- Docker image with flask, uwsgi and nginx for Easy Mode deployment
- 5-step development environment setup
- SwaggerUI for browsing


Getting started
-------------
Check out `the wiki <https://github.com/rbw0/redap/wiki>`_ for guides, client examples and more.



Author
------
Robert Wikman <rbw@vault13.org>
