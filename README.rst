|PyPI| |Travis| |PyPI| |Documentation Status| |Join the chat at
https://gitter.im/seemethere/nba\_py|

*nba\_py - `stats.nba.com <http://stats.nba.com>`__ API for python*
===================================================================

`stats.nba.com Endpoint Documentation <https://github.com/seemethere/nba_py/wiki/stats.nba.com-Endpoint-Documentation>`__
-------------------------------------------------------------------------------------------------------------------------

Stable version: **v0.1a1**

This branches version: **v0.1a2**

Summary
-------

A python facing API for stats.nba.com (Still in heavy development)

Originally based off https://github.com/bradleyfay/NBAStats

Installation
------------

NOTE: Developmental builds, are by no means stable If you want the
stable version use:

::

    $ pip install nba_py

Else: - Download from source (git clone, zipped package) - Run from the
root directory:

::

    $ pip install .

Requirements |Requires.io|
--------------------------

-  `requests <http://www.python-requests.org/en/latest/>`__

Nice to have
------------

Pandas is nice to have because it'll put the data in an easy to manage
object, but it is by no means necessary. All data, if pandas is not
installed is returned in a nice json list format with headers! -
`pandas <http://pandas.pydata.org/>`__ `(Installation
Help) <https://github.com/seemethere/nba_py/wiki/Installing-pandas>`__

Completed work
--------------

-  See the
   `wiki <https://github.com/seemethere/nba_py/wiki/Completed-Work-Log>`__

Planned development
-------------------

1. Documentation
~~~~~~~~~~~~~~~~

-  All around documentation not only of nba\_py but also stats.nba.com
   (it's pretty nonexistent)

[STRIKEOUT:2. Map rest of API] (Completed)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |PyPI| image:: https://img.shields.io/pypi/v/nba_py.svg?style=flat-square
   :target: https://pypi.python.org/pypi/nba_py
.. |Travis| image:: https://img.shields.io/travis/seemethere/nba_py.svg?style=flat-square
   :target: https://travis-ci.org/seemethere/nba_py
.. |PyPI| image:: https://img.shields.io/pypi/l/nba_py.svg?style=flat-square
   :target: https://github.com/seemethere/nba_py/blob/master/LICENSE
.. |Documentation Status| image:: https://readthedocs.org/projects/nba-py/badge/?version=0.1a2
   :target: http://nba-py.readthedocs.org/en/0.1a2/
.. |Join the chat at https://gitter.im/seemethere/nba\_py| image:: https://badges.gitter.im/Join%20Chat.svg
   :target: https://gitter.im/seemethere/nba_py?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
.. |Requires.io| image:: https://img.shields.io/requires/github/seemethere/nba_py.svg?style=flat-square
   :target: https://requires.io/github/seemethere/nba_py/requirements/?branch=master
