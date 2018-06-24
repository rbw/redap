.. code-block::

      __                __                    
     / /___ _____  ____/ /___ _____  ________ 
    / / __ `/ __ \/ __  / __ `/ __ \/ ___/ _ \
   / / /_/ / /_/ / /_/ / /_/ / / / / /__/  __/
  /_/\__,_/ .___/\__,_/\__,_/_/ /_/\___/\___/ 
    HTTP /_/ LDAP directory-agnostic gateway


Adding LDAP support to an application can be a time-consuming, tedious and complex task.

Lapdance creates an abstraction layer on top of LDAP, in its own little habitat—or micro-service if you want—making *everything great again!*.

Description
------
Powered by Flask—robust and customizable enough for production use—simple enough for grandma to operate.

It's partly inspired by, and is conceptually similar to Addict—but offers more functionality:

- RESTful HTTP API
- API key authorization
- Custom schemas
- Simplified Query Language
- Robust server logging
- LDAP debugging
- Production-ready Docker image
- SwaggerUI

At a higher level, it currently provides:

- Solid CRUD support for LDAP-conformant directory servers
- Support for extended operations in Active Directory 

The long-term goal is to provide helpers for common operations in other, also popular LDAP directory servers.


Documentation
-------------
Check out `the wiki <https://github.com/rbw0/lapdance/wiki>`_ for guides and other info.


Author
------
Robert Wikman <rbw@vault13.org>
