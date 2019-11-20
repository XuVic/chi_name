class ValuesWrapper(object):
    def __init__(self, values):
        self.values = values 
        self.records = self.__create_records(values[0], values[1:])

    def __repr__(self):
        return "Values attr{}: {}".format(self.values[0], len(self.values[1:]))

    def __create_records(self, attributes, records):
        data = []
        for record in records:
            temp_data = {attributes[i]: record[i]  for i in range(len(record)) }
            data.append(temp_data)
        return data
    
    def __len__(self):
        return len(self.records)

    def __getitem__(self, key):
       return self.records[key]

    def __iter__(self):
        return self.records.__iter__()

    def __contains__(self, item):
        return item in self.records

    def __add__(self, another):
        self.records + another.records
        return self