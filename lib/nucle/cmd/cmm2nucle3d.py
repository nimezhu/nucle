import xml.etree.ElementTree as ET

def help():
    return "convert cmm format to nucle3d format"
def set_parser(p):
    p.add_argument(
        '-i',
        '--input',
       dest='input',
        default='stdin',
        type=str,
        help="input file Default: %(default)s")
    p.add_argument(
        '-g',
        '--genome',
        dest='genome',
        default='hg38',
        type=str,
        help="genome version Default: %(default)s")
    p.add_argument(
        '-b',
        '--binsize',
        dest='binsize',
        default=1000000,
        type=int,
        help="genome version Default: %(default)s")
def run(args):
    tree = ET.parse(args.input)
    genome = args.genome
    binsize = args.binsize
    root = tree.getroot()
    lastchr = ""
    index = 0
    print("TITLE\t%s" % root.attrib["name"])
    print("GENOME\t%s" % genome)
    print("BINSIZE\t%s" % binsize)
    for child in root:
        tag = child.tag
        a = child.attrib
        if tag == "marker":
            if lastchr != a["chrID"]:
                lastchr = a["chrID"]
                print("CHR\t%s" % lastchr)
                index = 0
            print("%s,%s,%s,%s" % (index, a["x"], a["y"], a["z"]))
            index += 1
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(p.print_help())
        exit(0)
    run(p.parse_args())
