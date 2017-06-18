from model.group import Group
from random import randrange


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New group")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
 #   if app.group.count() == 0:
 #       app.group.create(Group(name='test'))
 #   old_groups = app.group.get_group_list()
 #   group = Group(name="New header")
  #  group.id = old_groups[0].id
 #   app.group.modify_first(group)
 #   new_groups = app.group.get_group_list()
  #  assert len(old_groups) == len(new_groups)
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_edit_first_group(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name='test'))
#    old_groups = app.group.get_group_list()
#    group = Group(name="Test", header="Test header", footer="Test footer")
#   group.id = old_groups[0].id
#    app.group.edit_first(group)
#   new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_edit_first_group_to_empty(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name='test'))
#    old_groups = app.group.get_group_list()
#    group = Group(name="", header="", footer="")
#    group.id = old_groups[0].id
#    app.group.edit_first(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)