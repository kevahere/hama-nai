<<<<<<< HEAD
from app import create_app, db
from flask_script import Manager, Server
from app.models import ForumPost, ForumThread
from flask_migrate import Migrate, MigrateCommand
=======
from flask_script import Manager, Server
from app import create_app
>>>>>>> c0d338d063c911a06d62613347a1241a8b78ca42

app = create_app('development')

manager = Manager(app)
<<<<<<< HEAD
migrate = Migrate(app, db)

manager.add_command('server', Server)
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, ForumPost=ForumPost, ForumThread=ForumThread)


if __name__== '__main__':
=======
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict(app=app)

if __name__ == '__main__':
>>>>>>> c0d338d063c911a06d62613347a1241a8b78ca42
    manager.run()