import locust
import random
import uuid
import time

import gevent

class MyTaskSet(locust.TaskSet):

    @locust.task(2)
    def get_root(self):
        self.client.get('/')

    @locust.task(3)
    def do_post(self):
        start = time.time()
        with self.client.post('/posts', data='data!',
                              catch_response=True) as resp:

            # normally, poll for an active/completed status instead of sleeping
            gevent.sleep(random.randint(2, 5))

            response_time = (time.time() - start) * 1000

            resp.locust_request_meta['response_time'] = int(response_time)
            resp.success()

    @locust.task(3)
    def do_mightfail(self):
        self.client.get('/mightfail')

    @locust.task(2)
    def get_posted_thing(self):
        self.client.get('/posts/%s' % str(uuid.uuid4()), name='/posts/ID')


class MyLocust(locust.HttpLocust):
    task_set = MyTaskSet

    min_wait = 800
    max_wait = 1200

    host = 'http://localhost:5000'
