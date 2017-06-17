from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='test'))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first(Contact(firstname="Test User", lastname="Test", title="Test", company="Test", mobile="00000000", email="testtest@test.ru"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_first_contact_to_empty(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='test'))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first(Contact(firstname="", lastname="", title="", company="", mobile="", email=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)