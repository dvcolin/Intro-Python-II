class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __getitem__(self, item):
        return self

    def __str__(self):
        return f"{self.name}: {self.description}"
