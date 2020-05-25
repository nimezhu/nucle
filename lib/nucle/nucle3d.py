import numpy as np
from io import StringIO
import falcon
class hssreader(object):
    def __init__(self,db):
        self.db = db
        self.coords = np.transpose(db['coordinates'][:],(1,0,2))
        genome = db['genome']
        assembly = genome["assembly"][...]
        self.assembly = str(assembly)
        self.chroms = genome['chroms'][:]
        origins = genome['origins'][:]
        lengths = genome['lengths'][:]

        index = db['index']
        iChrom = index['chrom'][:]
        self.chromSizes = index['chrom_sizes'][:]
        iStart = index['start'][:]
        iEnd = index['end'][:]
        self.res = iEnd[2] - iStart[2]  # TODO
    def on_get(self,req,resp,i):
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = (self.output(i))
    def output(self,i):
        buf = StringIO()
        buf.write("TITLE\t%d\n" % i)
        buf.write("GENOME\t%s\n" % self.assembly)
        buf.write("BINSIZE\t%d\n" % self.res)
        k=0
        for i0,st in enumerate(self.chroms):
            buf.write("CHR\t")
            buf.write("%s\n"%str(st.decode("ascii")))
            for j in range(self.chromSizes[i0]):
                st = self.coords[i][k]
                buf.write("%d,%.2f,%.2f,%.2f\n" % (j,st[0],st[1],st[2]))
                k+=1
        return buf.getvalue().strip("\n")
