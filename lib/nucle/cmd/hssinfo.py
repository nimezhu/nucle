import h5py

def help():
    return "output basic info about hss file "
def set_parser(p):
    p.add_argument('-i','--input',dest='input',default='stdin',type=str,help="input file Default: %(default)s")
def run(args):
    h5f = h5py.File(args.input, 'r')
    genome = h5f['genome']['assembly'][...]
    print("Genome Version:", genome)
    h5f.close()



if __name__=="__main__":
    if len(sys.argv)==1:
        print(p.print_help())
        exit(0)
    run(p.parse_args())
