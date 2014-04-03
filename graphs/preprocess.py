import csv
import sys
import hashlib


class Preprocessor():
    def preprocessIO(self, filename):
        val = self.loadIOCSV(filename)
        rewr = {}
        for v in val.keys():
            st = v.split('<-')
            # remove empty strings
            st = filter(None, st)
            st = [s.replace(' ', '') for s in st]
            # reverse stacktrace
            st = st[::-1]
            st = ';'.join(st)
            rewr[st] = [val[v]]
        self.writeCsv(rewr, "%s_rewr" % filename)

    def loadIOCSV(self, filename):
        values = {}
        # read CSV
        with open(filename, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for line in reader:
                st = line[1].strip()
                val = int(line[2].strip())
                values[st] = val
        return values

    def writeCsv(self, csv, filename):
        with open(filename, "w") as csvfile:
            for st in csv.keys():
                csvfile.write("%s %d\n" % (st, csv[st][0]))


if __name__ == '__main__':

    if len(sys.argv) < 3:
        print "Usage: python preprocess.py filename type"
        print "type: {IO}"
        sys.exit(0)

    p = Preprocessor()

    if sys.argv[2] == "IO":
        p.preprocessIO(sys.argv[1])
