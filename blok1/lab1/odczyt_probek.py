import pandas as pd


class SamplesReader:
    samples = None

    def __init__(self, filename=None):
        try:
            self.read_file(filename)
        except ValueError:
            pass

    def read_file(self, filename):
        self.samples = pd.read_csv(filename, header=None, delim_whitespace=True)

    def get_col(self, x):
        return self.samples[x]

    def get_row(self, y):
        return self.samples.loc[y]

    def get_sample(self, y, x):
        return self.samples.loc[y, x]


class AttributesReader:
    attributes = None

    def __init__(self, filename=None):
        try:
            self.read_file(filename)
        except ValueError:
            pass

    def read_file(self, filename):
        self.attributes = pd.read_csv(filename, header=None, delim_whitespace=True)

    def get_attr_name(self, y):
        return self.attributes.loc[y, 0]

    def is_symb_attr(self, y):
        return self.attributes.loc[y, 1] == 's'

