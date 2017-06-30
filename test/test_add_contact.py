# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname='', lastname='', title='', company='', mobilephone='', email='test@mail.ru')] + [
        Contact(firstname=random_string('firstname', 10), lastname=random_string('Petrov', 10), title=random_string('engeneer', 20),
                company=random_string('top labs', 20), mobilephone=random_string('8-888-888-88-88', 30),
                email=random_string('test@mail.ru', 30))
for i in range(5)
    ]

@pytest.mark.parametrize('contact', testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
        pass
        old_contacts = app.contact.get_contact_list()
        app.contact.create(contact)
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
