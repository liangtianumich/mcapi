import unittest
from random import randint
from mcapi import set_remote_config_url, get_remote_config_url
from mcapi import Project
from mcapi import list_projects
from mcapi import create_project

url = 'http://mctest.localhost/api'

def fake_name(prefix):
    number="%05d" % randint(0,99999)
    return prefix+number

class TestProject(unittest.TestCase):
    def setup(self):
        set_remote_config_url(url)

    def test_is_setup_correctly(self):
        self.assertEqual(get_remote_config_url(), url)

    def test_list_projects_object(self):
        projects = list_projects()
        project = projects[0]
        self.assertIsNotNone(project.name)
        self.assertTrue(isinstance(project,Project))
        self.assertIsNotNone(project.description)
        self.assertIsNotNone(project.id)
        self.assertNotEqual(project.name,"")

    def test_create_project_object(self):
        name = fake_name("TestProject-")
        description = "Test project generated by automated test"
        project = create_project(name,description)
        self.assertIsNotNone(project.name)
        self.assertTrue(isinstance(project,Project))
        self.assertIsNotNone(project.description)
        self.assertIsNotNone(project.id)
        self.assertNotEqual(project.name,"")
        self.assertEqual(name,project.name)
        self.assertEqual(description,project.description)