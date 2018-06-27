.. code-block::

                      __
       ________  ____/ /___ _____
      / ___/ _ \/ __  / __ `/ __ \
     / /  /  __/ /_/ / /_/ / /_/ /
    /_/   \___/\__,_/\__,_/ .___/
       HTTP/LDAP Gateway /_/


Powered by Flask—robust and customizable enough for production use—simple enough for grandma to operate.


Motivation
-------
Adding LDAP support to an application can be a time-consuming, tedious and complex task.

Redap adds an abstraction layer on top of LDAP, in its own little habitat—or micro-service, if you will—providing flexibility, customizability and simplicity.


Features
------

Redap was partly inspired by and is conceptually similar to `dthree/addict <https://github.com/dthree/addict>`_, but offers more features:


- RESTful HTTP API
- API key authorization
- Custom schemas
- Simplified Query Language
- LDAP debugging
- Robust application stack
- Production-ready Docker image
- SwaggerUI


Getting started
-------------
Check out `the wiki <https://github.com/rbw0/redap/wiki>`_ for guides and other info.


Quick demo?
--------
If you have **docker-compose** installed—run the following commands to *download, install, configure* and *start* the full server stack (with a connection ready to demo1.freeipa.org) in ~30 seconds.

.. code-block::

  $ wget -q -O- https://git.io/f45Px | sudo docker-compose -f - up -d
  $ ~/.redap/scripts/keys.sh add "My first API key"


...then point a browser to *http://127.0.0.1:5000/api-docs*, click **Authorize** and provide the generated API key.



Project status
-----------
Early stages of development. There might be a bug or three.

At a high level, Redap currently provides:

- Solid CRUD support for LDAP-conformant directory servers
- Support for extended operations in Active Directory 

The long-term goal is to provide helpers for common operations in other, also popular directory servers.



Needless to say: create an Issue if you've found a bug, or a PR if you have a code contribution.


**Being worked on**

- tests
- nginx ssl
- pagination
- more directory types




Author
------
Robert Wikman <rbw@vault13.org>
