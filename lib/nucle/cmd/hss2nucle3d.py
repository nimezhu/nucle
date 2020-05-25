import h5py
from io import StringIO
import numpy as np
from nucle.nucle3d import hssreader

def help():
    return "extract a structure in a hss file and output it as nucle3d format"
def set_parser(p):
    p.add_argument('-i','--input',dest='input',default='stdin',type=str,help="input file Default: %(default)s")
    p.add_argument('-n',dest='n',default=1,type=int,help="output nth structure Default: %(default)s")
def run(args):
    h5f = h5py.File(args.input, 'r')
    n = hssreader(h5f)
    i = args.n
    print(n.output(i-1))
    h5f.close()

if __name__=="__main__":
    if len(sys.argv)==1:
        print(p.print_help())
        exit(0)
    run(p.parse_args())
