from falcon import testing

from main.main import app


class BaseTest(testing.TestCase):
    def setUp(self):
        super(BaseTest, self).setUp()

        self.app = app
