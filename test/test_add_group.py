def test_add_group(app, xl_groups):
    group = xl_groups
    old_list = app.group.get_group_list()
    app.group.add_new_group(group)
    new_list = app.group.get_group_list()
    old_list.append(group)
    assert sorted(old_list) == sorted(new_list)
