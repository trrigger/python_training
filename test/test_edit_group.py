from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first(Group(name="New group"))


def test_modify_group_header(app):
    app.group.modify_first(Group(header="New header"))


def test_edit_first_group(app):
    app.group.edit_first(Group(name="Test", header="Test header", footer="Test footer"))


def test_edit_first_group_to_empty(app):
    app.group.edit_first(Group(name="", header="", footer=""))