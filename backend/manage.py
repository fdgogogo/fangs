import sys
import os

from flask import url_for
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager, Shell

dirname = os.path.dirname
sys.path.insert(0, dirname(dirname(os.path.abspath(__file__))))

import backend
import backend.blog.models
import backend.utils.wordpress_importer


migrate = Migrate()
migrate.init_app(backend.app, backend.db)

manager = Manager(backend.app)
manager.add_command('db', MigrateCommand)

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
