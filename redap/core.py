# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_ldapconn import LDAPConn
from flasgger import Swagger
from flask_migrate import Migrate
from flask_jsonrpc import JSONRPC


cors = CORS()
ldap = LDAPConn()
swagger = Swagger()
db = SQLAlchemy()
migrate = Migrate()
rpc = JSONRPC()
