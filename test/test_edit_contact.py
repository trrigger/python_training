from model.contact import Contact
from random import randrange


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='test'))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="", lastname="", title="Test", company="Test", mobilephone="00000000", email="test@test.ru")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_edit_first_contact_to_empty(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname='test'))
#    old_contacts = app.contact.get_contact_list()
#   contact = Contact(firstname="", lastname="", title="", company="", mobilephone="", email="")
#    contact.id = old_contacts[0].id
#    app.contact.edit_first(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
#    old_contacts[0] = contact
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)