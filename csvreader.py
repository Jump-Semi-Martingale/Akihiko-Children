# -*- coding: utf-8 -*-

import pandas as pd

# Get data from csv file
# syukujitsu.csv downloaded from
# http://www8.cao.go.jp/chosei/shukujitsu/gaiyou.html

import pandas as pd
import datetime

class CSVReader:
    def __init__(self, filepath, outputpath):
        self.filepath = filepath
        self.outputpath = outputpath

    def getdata(self):
        self.df = pd.read_csv(self.filepath)
        return self.df

    def savedata(self,data):
        data.to_csv(self.outputpath)

    def getdate(self):
        d = self.df["Date1"]
        d = pd.to_datetime(d)
        print d

if __name__ == "__main__":
    r = CSVReader("syukujitsu.csv", "output.csv")
    d = r.getdata()
    r.savedata(d)
    r.getdate()
