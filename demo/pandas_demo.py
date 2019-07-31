import pandas as pd


class ReadCVSDataDemo:
    def __init__(self):
        self.data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv', sep='\t')
        return

    def exercise1(self):
        # examine the data
        print(self.data.head)

        # get total orders
        print(self.data.quantity.sum())

        # get data shape
        print(self.data.shape)

        # what are the names of the columns
        print(self.data.columns)

        # how many orders are in the DataSet?
        # use value_counts()
        print(self.data['order_id'].value_counts().count())


class ReadTTLDataDemo:
    def __init__(self):
        self.data = pd.read_csv('../src/data/agg_application_pod_hourly.csv', header=None, na_values=[r'\N'])
        return

    def demo(self):
        print(self.data.head)

        # Set the names of the columns
        header_str = 'hour_key, date_key, datacenter, superpod, pod,' \
                     ' mem_utilization, max_app_cpu, avg_app_cpu, gc_perc,' \
                     'p95_app_cpu, last_modified, app_host_count_active, ' \
                     'app_transacting_host_count'
        self.data.columns = header_str.split(', ')
        print(self.data.head())

        # Inspect the column max_app_cpu
        print(self.data['max_app_cpu'].describe())

        # drop the missing data
        print(self.data['max_app_cpu'].dropna().describe())

        # What is the maximum value for the app_host_count_active column?
        print(self.data['app_host_count_active'].dropna().max())

        # How many times did the maximum values occur in the dataset
        print(self.data[self.data['app_host_count_active'] == 50].count())
