import os
import unittest
import coverage
from app import create_app
from app.models import User, Business, Review
from flask_script import Manager
from flask_script import Shell

app = create_app(os.getenv('APPLICATION_CONFIG') or 'default')
manager = Manager(app)


@manager.command
def run_test():
    """Run the unit tests."""
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def run_coverage():
    """Run tests with coverage"""
    cov =  coverage.coverage(branch=True, include='app/*')
    cov.start()
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    cov.stop()
    cov.save()
    print('Test Coverage Summary')
    cov.report()
    basedir = os.path.abspath(os.path.dirname(__file__))
    coverage_dir = os.path.join(basedir,'coverage')
    cov.html_report(directory=coverage_dir)
    cov.erase()

@manager.command
def deploy():
    pass


def make_shell_context():
    return dict(app=app, User=User, Business=Business, Review=Review)


manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
