import csv
import sys
from decimal import Decimal


class DiffFlameGraph():

    def loadCSV(self, filename):
        values = {}
        # read CSV
        with open(filename, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ')
            for line in reader:
                st = line[0].strip()
                val = int(line[1].strip())
                values[st] = val
        return values

    def diffCsv(self, values1, values2):
        values = {}
        for st in values1.keys():
            if st in values2.keys():
                values[st] = values2[st] - values1[st]
            else:
                values[st] = -values1[st]

        # make sure all new keys are added to the graph as well
        for st in values2.keys():
            if st not in values.keys():
                values[st] = values2[st]

        return values

    def equal(self, values1, values2):
        for st in values1.keys():
            if st not in values2.keys():
                return False
            if values1[st] != values2[st]:
                return False
        return len(values1) == len(values2)

    def writeDiff(self, diffCsv, filename):
        with open(filename, "w") as csvfile:
            for st in diffCsv:
                csvfile.write("%s %d\n" % (st, diffCsv[st]))

if __name__ == '__main__':

    if len(sys.argv) < 4:
        print "Usage: python diff_flame_graphs.py profile1 profile2 outputname"
        print "Note: profile(*) is a textfile containing stacktraces and a value for those traces, separated by a space"
        sys.exit(0)

    diff = DiffFlameGraph()
    val1 = diff.loadCSV(sys.argv[1])
    val2 = diff.loadCSV(sys.argv[2])

    diffCsv = diff.diffCsv(val1, val2)
    diff.writeDiff(diffCsv, sys.argv[3])
