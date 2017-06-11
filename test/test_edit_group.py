from model.group import Group


def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(name="New group"))
    app.session.logout()


def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(header="New header"))
    app.session.logout()


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="Test", header="Test header", footer="Test footer"))
    app.session.logout()


def test_edit_first_group_to_empty(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="", header="", footer=""))
    app.session.logout()