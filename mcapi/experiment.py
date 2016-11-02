from mcapi import api, MCObject


class Experiment(MCObject):
    def __init__(self, project_id=None, name=None, description=None, id=None, goals=None, aims=None, tasks=None,
                 data={}):

        # attr = ['id', 'name', 'description', 'birthtime', 'mtime', '_type', 'owner']
        super(Experiment, self).__init__(data)

        attr = ['status', 'tasks', 'funding', 'publications', 'notes', 'papers',
                'collaborators', 'note', 'citations', 'goals', 'aims']
        for a in attr:
            setattr(self, a, data.get(a, None))

        if (name): self.name = name
        if (description): self.description = description
        if (project_id): self.project_id = project_id
        if (id): self.id = id

        if (goals):
            self.goals = goals
        else:
            self.goals = []

        if (aims):
            self.aims = aims
        else:
            self.aims = []

        if (tasks):
            self.tasks = tasks
        else:
            self.tasks = []


def create_experiment(project_id, name, description):
    experiment_json = api.create_experiment(project_id, name, description)
    return Experiment(data=experiment_json)


__example_sample__ = {u'status': u'active',
                      u'_type': u'experiment',
                      u'tasks': [
                          {u'due_date': 0, u'_type': u'experiment_task', u'tasks': [], u'name': u'', u'index': 0,
                           u'mtime': {u'timezone': u'+00:00', u'$reql_type$': u'TIME', u'epoch_time': 1478019910.16},
                           u'template_id': u'', u'note': u'Notes here...', u'parent_id': u'', u'process_id': u'',
                           u'flags': {u'starred': False, u'onhold': False, u'done': False, u'flagged': False},
                           u'experiment_id': u'79b53479-3ab2-4d53-80fe-f029d63aaf02',
                           u'experiment_task_id': u'33f12642-003f-4523-a4b9-fd7f5cf786d3',
                           u'owner': u'terry.weymouth@gmail.com',
                           u'birthtime': {u'timezone': u'+00:00', u'$reql_type$': u'TIME',
                                          u'epoch_time': 1478019910.16},
                           u'estimate': {u'value': 0, u'unit': u''}, u'id': u'33f12642-003f-4523-a4b9-fd7f5cf786d3'}],
                      u'funding': [], u'description': u'Test experiment generated by automated test',
                      u'publications': [],
                      u'notes': [], u'papers': [], u'collaborators': [], u'note': u'<h2>Experiment Notes</h2>',
                      u'citations': [],
                      u'goals': [],
                      u'mtime': {u'timezone': u'+00:00', u'$reql_type$': u'TIME', u'epoch_time': 1478019910.086},
                      u'owner': u'terry.weymouth@gmail.com',
                      u'birthtime': {u'timezone': u'+00:00', u'$reql_type$': u'TIME', u'epoch_time': 1478019910.086},
                      u'id': u'79b53479-3ab2-4d53-80fe-f029d63aaf02', u'name': u'TestExperiment-25048'}