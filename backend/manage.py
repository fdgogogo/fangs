from getpass import getpass
import re
import sys
import os

from flask import url_for
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager, Shell, Option
from flask.ext.security import script

dirname = os.path.dirname
sys.path.insert(0, dirname(dirname(os.path.abspath(__file__))))

import backend
import backend.blog.models
import backend.utils.wordpress_importer

migrate = Migrate()
migrate.init_app(backend.app, backend.db)

manager = Manager(backend.app)
manager.add_command('db', MigrateCommand)


class PromotedCreateUserCommand(script.CreateUserCommand):
    """Create a user"""

    option_list = (
        Option('-e', '--email', dest='email', default=None),
        Option('-p', '--password', dest='password', default=None),
        Option('-a', '--active', dest='active', default=''),
    )

    @script.commit
    def run(self, **kwargs):
        # sanitize active input
        ai = re.sub(r'\s', '', str(kwargs['active']))
        kwargs['active'] = ai.lower() in ['', 'y', 'yes', '1', 'active']

        from flask_security.forms import ConfirmRegisterForm
        from werkzeug.datastructures import MultiDict

        if not kwargs.get('password'):
            kwargs['password'] = getpass('password: ')
        form = ConfirmRegisterForm(MultiDict(kwargs), csrf_enabled=False)

        if form.validate():
            kwargs['password'] = script.encrypt_password(kwargs['password'])
            script._datastore.create_user(**kwargs)
            print('User created successfully.')
            kwargs['password'] = '****'
            script.pprint(kwargs)
        else:
            print('Error creating user')
            script.pprint(form.errors)


manager.add_command('create_user', PromotedCreateUserCommand)
manager.add_command('create_role', script.CreateRoleCommand)
manager.add_command('activate_user', script.ActivateUserCommand)
manager.add_command('deactivate_user', script.DeactivateUserCommand)
manager.add_command('add_role', script.AddRoleCommand)
manager.add_command('remove_role', script.RemoveRoleCommand)

manager.add_command('import_wordpress',
                    backend.utils.wordpress_importer.ImportWordpress)


def _make_context():
    return dict(app=backend.app, db=backend.db, models=backend.blog.models)


manager.add_command("shell", Shell(make_context=_make_context))


@manager.command
def list_routes():
    import urllib.parse
    output = []
    for rule in backend.app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.parse.unquote(
            "{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)


if __name__ == '__main__':
    manager.run()
