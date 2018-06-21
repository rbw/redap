.. code-block::

      __                __                    
     / /___ _____  ____/ /___ _____  ________ 
    / / __ `/ __ \/ __  / __ `/ __ \/ ___/ _ \
   / / /_/ / /_/ / /_/ / /_/ / / / / /__/  __/
  /_/\__,_/ .___/\__,_/\__,_/_/ /_/\___/\___/ 
    HTTP /_/ LDAP directory-agnostic gateway



Motivation
------
Adding LDAP support to an application can be a time-consuming and complex task; Lapdance remedies this by creating a layer of abstraction on top of the LDAP protocol. Also, as Lapdance runs in its own self-contained environment—it provides not only flexibility, but also customizability—leaving you in control!


Description
------
Powered by Flask—robust and customizable enough for production use—simple enough for grandma to operate.

It was partly inspired by, and is conceptually similar to Addict—but offers more sugar:

- API key authorization
- LDAP3 Simplified Query Language
- Schemas with mappings and validation
- Server logging
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
