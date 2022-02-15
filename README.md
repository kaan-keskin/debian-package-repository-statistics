# Debian Package Repository Statistics (DPRS) Tool

Debian uses *deb packages to deploy and upgrade software.
The packages are stored in repositories and each repository contains the "Contents Index".
The format of that file is well described here: https://wiki.debian.org/RepositoryFormat#A.22Contents.22_indices

This tool takes the architecture (amd64, arm64, i386 etc.) as an argument,
and downloads the compressed Contents-*.gz file associated with it from a Debian package repository mirror.
The program will parse the file and output the statistics of the top 10 packages that have the most files associated with them.

An example output could be:
```shell
./dprs.py amd64

1. <package name 1> <number of files>
2. <package name 2> <number of files>
...
10. <package name 10> <number of files>
```

The following Debian mirror will be used as a default package repository:
http://ftp.uk.debian.org/debian/dists/stable/main/.

## Installlation Options

### Installation with PIP (Recommended)

```shell
$ pip install .
```

```
Processing ~/debian-package-repository-statistics
Building wheels for collected packages: dprs
  Building wheel for dprs (setup.py) ... done
  Created wheel for dprs: filename=dprs-1.0-py3-none-any.whl size=12082 sha256=cabba4818b27aa6c6d606333d4108fa86dfb130fcff460593b0a67dca9cdaaeb
  Stored in directory: ~/.cache/pip/wheels/eb/61/37/15310951587be91d6a793dabcdf29a4d0da4c7d81b70b2105b
Successfully built dprs
Installing collected packages: dprs
Successfully installed dprs-1.0
```

### Uninstallation with PIP (Recommended)

```shell
$ pip uninstall dprs
```

```
Found existing installation: dprs 1.0
Uninstalling dprs-1.0:
  Would remove:
    /home/kaan/anaconda3/bin/dprs
    /home/kaan/anaconda3/lib/python3.9/site-packages/dprs-1.0.dist-info/*
    /home/kaan/anaconda3/lib/python3.9/site-packages/pkg/*
Proceed (Y/n)? y
  Successfully uninstalled dprs-1.0
```

### Installation with SetupTools

You need to remove all files manually, and also undo any other stuff that installation did manually.

If you don't know the list of all files, you can reinstall it with the --record option, 
and take a look at the list this produces.

```shell
$ python setup.py install --record installation-files.txt
```

Note: Avoid this option!

## Usages

### Usage without Installation
Give the execute permission for dprs.py file and run it:

```shell
$ chmod +x dprs.py
$ ./dprs.py --help
```

Or, you can directly run it with the python command:

```shell
$ python dprs.py --help
```

### Usage with Installation

```shell
$ dprs --help
```

### CLI Help Output

```shell
$ dprs.py --help
```
```
usage: dprs.py [-h] [-c] [-m MIRROR_URL] [-n NUMBER] [-o OUTPUT_DIR] [-r] [-s] [-u] [{amd64,arm64,armel,armhf,i386,mips64el,mipsel,ppc64el,s390x,None}]

Debian Repository Package Statistics (DRPS) Tool Tool takes the architecture (amd64, arm64, mipsel etc.) as an argument, and downloads the compressed Contents file associated with it from a Debian mirror. The program will parse the file, and output the statistics of the top 10 packages that have the
most files associated with them.

positional arguments:
  {amd64,arm64,armel,armhf,i386,mips64el,mipsel,ppc64el,s390x,None}
                        The architecture type of the Contents-*.gz file in the Debian repository. Options: ['amd64', 'arm64', 'armel', 'armhf', 'i386', 'mips64el', 'mipsel', 'ppc64el', 's390x', None]

optional arguments:
  -h, --help            show this help message and exit
  -c, --clean           Clean the outputs folder. This operation can not be irreversible. Default value: False
  -m MIRROR_URL, --mirror_url MIRROR_URL
                        Debian Package Repository Mirror URL. Default value: http://ftp.uk.debian.org/debian/dists/stable/main/
  -n NUMBER, --number NUMBER
                        Number of the top packages to show. Use -1 to show all packages. Default value: 10
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR
                        Directory to store downloaded contents. Default value: /home/kaan/softdev/git-repos/debian-package-repository-statistics/outputs
  -r, --reuse_contents_file
                        Reuses Contents-*.gz file if it exists in the output directory. Default value: True
  -s, --sort_descending
                        Sort package statistics by descending order. Default value: True
  -u, --include_udeb    Include udeb file for the given architecture. Default value: False
```

### Getting Debian Package Statistics For Different CPU Architectures

#### CPU Architecture:amd64 Top 10 Statistics

```shell
$ dprs.py amd64
```
```
./debian-package-repository-statistics/outputs/Contents-amd64
Order           Package Name                                   Number of Files
1               devel/piglit                                             51784
2               science/esys-particle                                    18015
3               libdevel/libboost1.74-dev                                14333
4               math/acl2-books                                          12668
5               golang/golang-1.15-src                                    9015
6               libdevel/liboce-modeling-dev                              7457
7               net/zoneminder                                            7002
8               libdevel/paraview-dev                                     6178
9               kernel/linux-headers-5.10.0-10-amd64                      6148
10              kernel/linux-headers-5.10.0-9-amd64                       6148
```

#### CPU Architecture:amd64 Top 20 Statistics For UDEB Packages

```shell
$ dprs.py -u -n 20 amd64
```
```
./debian-package-repository-statistics/outputs/Contents-amd64
Order           Package Name                                   Number of Files
1               devel/piglit                                             51784
2               science/esys-particle                                    18015
3               libdevel/libboost1.74-dev                                14333
4               math/acl2-books                                          12668
5               golang/golang-1.15-src                                    9015
6               libdevel/liboce-modeling-dev                              7457
7               net/zoneminder                                            7002
8               libdevel/paraview-dev                                     6178
9               kernel/linux-headers-5.10.0-10-amd64                      6148
10              kernel/linux-headers-5.10.0-9-amd64                       6148
11              kernel/linux-headers-5.10.0-9-rt-amd64                    6144
12              kernel/linux-headers-5.10.0-10-rt-amd64                   6142
13              localization/locales-all                                  5956
14              math/coq-theories                                         5588
15              utils/pcp-testsuite                                       4704
16              games/tuxfootball                                         4670
17              electronics/horizon-eda                                   4266
18              libdevel/libinsighttoolkit4-dev                           4029
19              kernel/linux-image-5.10.0-10-amd64-unsigned               3923
20              kernel/linux-image-5.10.0-9-amd64-unsigned                3923
```

#### CPU Architecture:arm64 Top 20 Statistics

```shell
$ dprs.py -n 20 arm64
```
```
./debian-package-repository-statistics/outputs/Contents-arm64
Order           Package Name                                   Number of Files
1               devel/piglit                                             51784
2               science/esys-particle                                    18015
3               libdevel/libboost1.74-dev                                14333
4               math/acl2-books                                          12668
5               golang/golang-1.15-src                                    9015
6               libdevel/liboce-modeling-dev                              7457
7               net/zoneminder                                            7002
8               libdevel/paraview-dev                                     6178
9               localization/locales-all                                  5956
10              kernel/linux-headers-5.10.0-10-arm64                      5854
11              kernel/linux-headers-5.10.0-9-arm64                       5854
12              kernel/linux-headers-5.10.0-9-rt-arm64                    5794
13              kernel/linux-headers-5.10.0-10-rt-arm64                   5792
14              utils/pcp-testsuite                                       4704
15              games/tuxfootball                                         4670
16              electronics/horizon-eda                                   4266
17              science/eso-midas                                         3789
18              kernel/linux-image-5.10.0-10-arm64-unsigned               3749
19              kernel/linux-image-5.10.0-9-arm64-unsigned                3749
20              kernel/linux-image-5.10.0-10-arm64                        3748
```

#### CPU Architecture:i386 Statistics with UDEB Packages

```shell
$ dprs.py -u i386
```
```
./debian-package-repository-statistics/outputs/Contents-i386
Order           Package Name                                   Number of Files
1               devel/piglit                                             51784
2               science/esys-particle                                    18015
3               libdevel/libboost1.74-dev                                14333
4               math/acl2-books                                          12660
5               golang/golang-1.15-src                                    9015
6               libdevel/liboce-modeling-dev                              7457
7               net/zoneminder                                            7002
8               kernel/linux-headers-5.10.0-10-rt-686-pae                 6183
9               kernel/linux-headers-5.10.0-9-rt-686-pae                  6183
10              kernel/linux-headers-5.10.0-10-686-pae                    6179
```

### Reuse Downloaded Contents-*.gz File

```shell
$ dprs.py -r amd64
```
```
./debian-package-repository-statistics/outputs/Contents-amd64
Order           Package Name                                   Number of Files
1               devel/piglit                                             51784
2               science/esys-particle                                    18015
3               libdevel/libboost1.74-dev                                14333
4               math/acl2-books                                          12668
5               golang/golang-1.15-src                                    9015
6               libdevel/liboce-modeling-dev                              7457
7               net/zoneminder                                            7002
8               libdevel/paraview-dev                                     6178
9               kernel/linux-headers-5.10.0-10-amd64                      6148
10              kernel/linux-headers-5.10.0-9-amd64                       6148

```

### Use Different Output Folder

```shell
$ dprs.py -o /tmp amd64
```
```
/tmp/Contents-amd64
Order           Package Name                                         Number of Files
1               devel/piglit                                                   51784
2               science/esys-particle                                          18015
3               libdevel/libboost1.74-dev                                      14333
4               math/acl2-books                                                12668
5               golang/golang-1.15-src                                          9015
6               libdevel/liboce-modeling-dev                                    7457
7               net/zoneminder                                                  7002
8               libdevel/paraview-dev                                           6178
9               kernel/linux-headers-5.10.0-10-amd64                            6148
10              kernel/linux-headers-5.10.0-9-amd64                             6148
```

### Clean Output Folder

```shell
$ dprs.py -c
```
```shell
$ ls
dprs.py  LICENSE  outputs  pkg  README.md

$ ls outputs 
Contents-amd64  Contents-amd64.gz  Contents-arm64  Contents-arm64.gz  Contents-i386  Contents-i386.gz  Contents-udeb-amd64  Contents-udeb-amd64.gz  Contents-udeb-i386  Contents-udeb-i386.gz

$ dprs.py -c           

$ ls          
dprs.py  LICENSE  pkg  README.md
```


