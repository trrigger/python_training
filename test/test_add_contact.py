# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname='Ivan', lastname='Petrov', title='engeneer', company='top labs', mobile='8-888-888-88-88', email='test@mail.ru'))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname='', lastname='', title='', company='', mobile='', email='test@mail.ru'))
    app.session.logout()
