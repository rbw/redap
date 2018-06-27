# -*- coding: utf-8 -*-

import sys
import getpass
import click
from sqlalchemy.orm.exc import NoResultFound
from flask.cli import AppGroup
from redap.models.apikey import APIKey
from redap.utils import generate_apikey_table
from redap.exceptions import InvalidConfiguration

try:
    from redap.api import create_app

    app = create_app()
except InvalidConfiguration as error:
    sys.stderr.write("Configuration file '{0}' failed validation: \n{1}".format(error.file, error.cause))
    sys.exit(4)


key_cli = AppGroup('auth', help='Manage API keys')


@key_cli.command('add')
@click.argument('description')
def add_key(description):
    new_key = APIKey.add({
        'created_by': '{0} (from CLI)'.format(getpass.getuser()),
        'description': description
    })

    app.logger.info('Added new API key: {0}'.format(new_key.description))
    sys.stdout.write('Created: {0}\n'.format(new_key.key))


@key_cli.command('del')
@click.argument('key')
def del_key(key):
    try:
        APIKey.delete(key)
        sys.stdout.write('Deleted: {0}'.format(key))
        app.logger.info('Deleted API key: {0}'.format(key))
    except NoResultFound:
        sys.stderr.write('No such key')


@key_cli.command('get')
@click.argument('key', required=False)
def get_keys(key=None):
    try:
        if key:
            sys.stdout.write(APIKey.get_one(key, as_json=True))
        else:
            sys.stdout.write(generate_apikey_table(APIKey.get_many()))
            sys.stdout.write('\n\nUse `get <key>` for details about a specific key\n')

    except NoResultFound:
        sys.stderr.write('No such key')


app.cli.add_command(key_cli)
