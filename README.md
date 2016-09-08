[![PyPI](https://img.shields.io/pypi/v/nba_py.svg?style=flat-square)](https://pypi.python.org/pypi/nba_py) [![Travis](https://img.shields.io/travis/seemethere/nba_py.svg?style=flat-square)](https://travis-ci.org/seemethere/nba_py)    [![License](https://img.shields.io/pypi/l/nba_py.svg?style=flat-square)](https://github.com/seemethere/nba_py/blob/master/LICENSE)
[![Documentation Status](https://readthedocs.org/projects/nba-py/badge/?version=0.1a2)](http://nba-py.readthedocs.org/en/0.1a2/)
[![Join the chat at https://gitter.im/seemethere/nba_py](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/seemethere/nba_py?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

# *nba_py - [stats.nba.com](http://stats.nba.com) API for python*

#### [stats.nba.com Endpoint Documentation](https://github.com/seemethere/nba_py/wiki/stats.nba.com-Endpoint-Documentation)

Stable version: **v0.1a1**

This branches version: **v0.1a2**

## Summary
A python facing API for stats.nba.com (Still in heavy development)


Originally based off [https://github.com/bradleyfay/NBAStats](https://github.com/bradleyfay/NBAStats)

## Installation
NOTE: Developmental builds, are by no means stable If you want the stable version use:

```
$ pip install nba_py
```

Else:
- Download from source (git clone, zipped package)
- Run from the root directory:

```
$ pip install .
```

## Requirements [![Requires.io](https://img.shields.io/requires/github/seemethere/nba_py.svg?style=flat-square)](https://requires.io/github/seemethere/nba_py/requirements/?branch=master)
- [requests](http://www.python-requests.org/en/latest/)

## Nice to have
Pandas is nice to have because it'll put the data in an easy to manage object, but it is by no means necessary. All data, if pandas is not installed is returned in a nice json list format with headers!
- [pandas](http://pandas.pydata.org/) [(Installation Help)](https://github.com/seemethere/nba_py/wiki/Installing-pandas)

Requests-cache is nice to have when you are downloading very large datasets so that subsequent downloads take much less time, but again, it is by no means necessary.
- [requests-cache](https://github.com/reclosedev/requests-cache)

## Completed work
- See the [wiki](https://github.com/seemethere/nba_py/wiki/Completed-Work-Log)

## Planned development
### 1. Documentation
- All around documentation not only of nba_py but also stats.nba.com (it's pretty nonexistent)

### ~~2. Map rest of API~~ (Completed)
