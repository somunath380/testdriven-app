import os
import unittest

from flask import current_app
from flask_testing import TestCase

from project import create_app

app = create_app()

class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object("project.config.DevelopmentConfig")
        return app
    
    def test_app_is_development(self):
        assert app.config['SECRET_KEY'] == "my_precious"
        assert not current_app == None
        assert app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get("DATABASE_URL")

class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app
    
    def test_app_is_testing(self):
        assert app.config['SECRET_KEY'] == 'my_precious'
        assert app.config['TESTING']
        assert app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get('DATABASE_TEST_URL')

class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.ProductionConfig')
        return app
    def test_app_is_production(self):
        assert app.config['SECRET_KEY'] == 'my_precious'
        assert not app.config['TESTING']

if __name__ == '__main__':
    unittest.main()
    
        

