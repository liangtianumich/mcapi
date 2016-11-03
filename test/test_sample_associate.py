import unittest
from random import randint
from mcapi import create_project, create_experiment, create_process_from_template, create_samples
from mcapi import add_samples_to_process

def fake_name(prefix):
    number="%05d" % randint(0,99999)
    return prefix+number

class TestSampleAssociate(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.base_project_name = "Project-TestSampleAssociate"
        description = "Test project generated by automated test"
        self.base_project = create_project(self.base_project_name, description)
        self.base_project_id = self.base_project.id
        name = fake_name("TestExperiment-")
        description = "Test experiment generated by automated test"
        self.base_experiment = create_experiment(self.base_project_id,name, description)
        self.base_experiment_id = self.base_experiment.id
        template_id = "global_Create Samples"
        self.base_create_sample_process = create_process_from_template(self.base_project_id,self.base_experiment_id,template_id)
        self.base_sample = create_samples(self.base_project_id, self.base_create_sample_process.id, ['Test Sample 1'])[0]
        template_id = "global_Computation"
        self.base_compute_process = create_process_from_template(self.base_project_id,self.base_experiment_id,template_id)

    def test_is_setup_correctly(self):
        self.assertIsNotNone(self.base_project)
        self.assertIsNotNone(self.base_project.name)
        self.assertEqual(self.base_project_name, self.base_project.name)
        self.assertIsNotNone(self.base_project.id)
        self.assertEqual(self.base_project_id, self.base_project.id)

        self.assertIsNotNone(self.base_experiment)
        self.assertIsNotNone(self.base_experiment.id)
        self.assertEqual(self.base_experiment_id, self.base_experiment.id)

        self.assertIsNotNone(self.base_create_sample_process)
        self.assertIsNotNone(self.base_create_sample_process.id)
        self.assertIsNotNone(self.base_create_sample_process.process_type)
        self.assertEqual(self.base_create_sample_process.process_type, 'create')
        self.assertTrue(self.base_create_sample_process.does_transform)

        self.assertIsNotNone(self.base_sample.id)
        self.assertIsNotNone(self.base_sample.name)

        self.assertIsNotNone(self.base_compute_process)
        self.assertIsNotNone(self.base_compute_process.id)
        self.assertIsNotNone(self.base_compute_process.process_type)
        self.assertEqual(self.base_compute_process.process_type, 'analysis')
        self.assertFalse(self.base_compute_process.does_transform)

    def test_associate_sample_with_process(self):
        process_with_sample = add_samples_to_process(self.base_project_id, self.base_experiment_id,
                                                     self.base_compute_process,[self.base_sample])
        self.assertEqual(process_with_sample.name,'Computation')
        self.assertEqual(len(process_with_sample.input_samples),1)
        self.assertEqual(process_with_sample.input_samples[0].name,self.base_sample.name)
        #self.assertTrue(False)