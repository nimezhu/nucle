# Nucleome Tools
## Python version: nucle
Python tools for nucleome browser.

include following functions:

```
usage: nucle [-h] [-v]
             {hssinfo,servehss,cmm2nucle3d,hss2nucle3d,createdatasheet} ...

python tools for nucleome browser

positional arguments:
  {hssinfo,servehss,cmm2nucle3d,hss2nucle3d,createdatasheet}
                        subcommand help
    hssinfo             output basic info about hss file
    servehss            hss to microservice[TODO]
    cmm2nucle3d         convert cmm format to nucle3d format
    hss2nucle3d         extract a structure in hss file and output it to
                        nucle3d format
    createdatasheet     download data from 4DN data portal and prepare a input
                        data sheet for nucleserver

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
```

## Nucle3D Structure Text Format
nucle3d format is used in Nucleome Browser Chromosome 3D Structure viewer web component.
Generate a nucle3d format file and put it in a web server 
make sure that the URL can accessed by "http(s)://vis.nucleome.org"  
(set its header "CORS").
Then, input the file URL in Nucleome Browser Chromosome 3D Structure viewer.

version 0.0.1
```
TITLE   [NAME]        # Tab split
GENOME  hg38          # Tab split
BINSIZE [binsize]
CHR chr1 # Tab split
i,x,y,z
i,x,y,z
..
CHR chr2
..
```
i is 0-index, gap of index i permitted

