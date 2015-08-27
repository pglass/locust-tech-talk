import locust
import uuid


class MyTaskSet(locust.TaskSet):

    @locust.task(2)
    def get_root(self):
        self.client.get('/')

    @locust.task(3)
    def do_post(self):
        self.client.post('/posts', data='data!')

    @locust.task(3)
    def do_mightfail(self):
        self.client.get('/mightfail')

    @locust.task(2)
    def get_posted_thing(self):
        self.client.get('/posts/%s' % str(uuid.uuid4()))


class MyLocust(locust.HttpLocust):
    task_set = MyTaskSet

    min_wait = 800
    max_wait = 1200

    host = 'http://localhost:5000'
