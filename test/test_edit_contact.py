from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first(Contact(firstname="Test User", lastname="Test", title="Test", company="Test", mobile="00000000", email="testtest@test.ru"))


def test_edit_first_contact_to_empty(app):
    app.contact.edit_first(Contact(firstname="", lastname="", title="", company="", mobile="", email=""))