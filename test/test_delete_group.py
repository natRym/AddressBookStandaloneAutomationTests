def test_delete_first_group(app):
    if app.group.count() == 0:
        app.groups.add_new_group("Group fore removing")
    old_list = app.group.get_group_list()
    app.group.delete_a_group()
    new_list = app.group.get_group_list()
    assert len(old_list) - 1 == len(new_list)
    del old_list[0]
    assert sorted(old_list) == sorted(new_list)




