class customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    @property
    def name(self):
        return self._name