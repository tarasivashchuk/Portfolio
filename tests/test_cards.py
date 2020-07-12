from portfolio.cards import *
from tests import DEBUG


def test_get_projects_markdown():
    projects = get_projects_markdown()
    assert type(projects) == list
    assert len(projects) > 0
    for project in projects:
        assert type(project) == str

