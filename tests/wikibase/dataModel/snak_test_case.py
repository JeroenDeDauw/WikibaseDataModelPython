class SnakTestCase():

    def new_instance(self):
        raise NotImplementedError('Deriving classes should implement this method')

    def test_can_construct(self):
        self.new_instance()

    def test_get_type_returns_string(self):
        self.assertIsInstance(self.new_instance().getType(), str)
