# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""

import pytest
import testing.postgresql
from app.app import create_app
from flask import Config
from flask.app import Flask

from app.database import db as _db


class TestConfig(Config):
    TESTING = True
    DEBUG = True


@pytest.yield_fixture(scope='session')
def temporary_postgresql_database():
    testdb = testing.postgresql.Postgresql()
    yield testdb
    testdb.stop()


@pytest.yield_fixture(scope='function')
def app(temporary_postgresql_database):
    """An application for the tests."""
    TestConfig.SQLALCHEMY_DATABASE_URI = temporary_postgresql_database.url()
    _app = create_app(TestConfig)
    ctx = _app.test_request_context()
    ctx.push()
    yield _app
    ctx.pop()


@pytest.yield_fixture(scope='function')
def db(app: Flask):
    _db.app = app
    yield _db
    _db.session.close()
