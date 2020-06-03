# Nucleome Tools

## Python version: nucle
### install
Download this repository. And then 
```
cd nucle 
python3 setup.py install
```
### Usage 
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
    servehss            host a hss file as web data service
    cmm2nucle3d         convert cmm format to nucle3d format
    hss2nucle3d         extract a structure in a hss file and output it as
                        nucle3d format
    createdatasheet     download data from 4DN data portal and prepare a input
                        data sheet for nucleserver

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
```

## Nucle3D Structure Text Format
nucle3d format is used in Nucleome Browser Chromosome 3D Structure viewer web component.
Generate a nucle3d format file and put it in a web server. Make sure that the URL can accessed by "http(s)://vis.nucleome.org"  
(set its header "CORS").

### Start a web file server with nucleserver
In [nucleserver](https://github.com/nucleome/nucleserver), we provide a subcommand to start a simple web server with CORS Header "Access-Control-Allow-Origin: https://vis.nucleome.org". 
For example , if you have a nucle3d format file /home/yourname/data/file.nucle3d.
you can start a file web server using our tool [nucleserver](https://github.com/nucleome/nucleserver)
```
nucleserver file -r /home/yourname/data 
```
It will start a server http://127.0.0.1:8611 and the nucle3d file url will be http://127.0.0.1:8611/get/file.nucle3d.
Then, input this file URL in Nucleome Browser Chromosome 3D Structure viewer. The 3D structure will be shown in this panel.
If 8611 port is occupied by another nucleserver program or other program.
You can start with -p parameter to set this web service to another port.

### Nucle3D format
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

