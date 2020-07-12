from portfolio import cards


def test_get_projects_markdown():
    projects = cards.get_projects_markdown()
    assert isinstance(projects, list)
    assert len(projects) > 0
    for project in projects:
        assert isinstance(project, str)
