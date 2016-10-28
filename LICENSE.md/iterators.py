# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)

        self.items = items
        self.i = 0
        self.unique_data = []

    def __next__(self):
        if (self.ignore_case == True):
            self.items = [str(i).lower() for i in self.items]
        while self.items[self.i] in self.unique_data:
            if (len(self.items) == self.i + 1):
                raise StopIteration
            self.i += 1

        self.unique_data.append(self.items[self.i])
        return self.items[self.i]

    def __iter__(self):
        return self