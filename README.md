# Nucleome Tools
## Python version: nucle
Python tools for nucleome browser.

include following functions:

cmm2nucle3d convert cmm format to nucle3d format.
hss2nucle3d extract structures from hss file and output as nucle3d format.
servehss    read hss file and provide a web data service 

## Nucle3D Structure Text Format
nucle3d format is used in Nucleome Browser Chromosome 3D Structure viewer web component.
Generate a nucle3d format file and put it in a web server 
make sure that the URL can accessed by "http(s)://vis.nucleome.org"  (set its header "CORS").
input the file URL in Nucleome Browser Chromosome 3D Structure viewer.

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

