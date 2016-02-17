.. vim: set fileencoding=utf-8 :
.. Andre Anjos <andre.anjos@idiap.ch>
.. Tue 16 Feb 2016 15:38:40 CET

.. image:: http://img.shields.io/badge/docs-stable-yellow.png
   :target: http://pythonhosted.org/bob.ip.facelandmarks/index.html
.. image:: http://img.shields.io/badge/docs-latest-orange.png
   :target: https://www.idiap.ch/software/bob/docs/latest/bioidiap/bob.ip.facelandmarks/master/index.html
.. image:: https://travis-ci.org/bioidiap/bob.ip.facelandmarks.svg?branch=master
   :target: https://travis-ci.org/bioidiap/bob.ip.facelandmarks?branch=master
.. image:: https://coveralls.io/repos/bioidiap/bob.ip.facelandmarks/badge.svg?branch=master
   :target: https://coveralls.io/r/bioidiap/bob.ip.facelandmarks?branch=master
.. image:: https://img.shields.io/badge/github-master-0000c0.png
   :target: https://github.com/bioidiap/bob.ip.facelandmarks/tree/master
.. image:: http://img.shields.io/pypi/v/bob.ip.facelandmarks.png
   :target: https://pypi.python.org/pypi/bob.ip.facelandmarks
.. image:: http://img.shields.io/pypi/dm/bob.ip.facelandmarks.png
   :target: https://pypi.python.org/pypi/bob.ip.facelandmarks

=====================================
 Face Keypoint Detection using menpo
=====================================

This package includes a `Bob`_ interface to `menpo`_ and menpofit, allowing you
to detect keypoints on faces from images and videos. The model was provided by
Epameinondas Antonakos from the `iBug`_ laboratory at Imperial College, London,
UK.


References
----------

If you use this package, the authors of `menpo`_ would appreciate if could cite
them::

  @inproceedings{menpo2014,
    author = {J. Alabort-i-Medina AND E. Antonakos AND J. Booth AND P. Snape AND S. Zafeiriou},
    title = {"Menpo: A comprehensive platform for parametric image alignment and visual deformable models},
    year = {2014},
    booktitle = {ACM International Conference on Multimedia, Orlando, FL, USA},
    publisher = {ACM Press},
    url = {http://www.menpo.org/pages/paper/Menpo_ACM_MM_2014.pdf},
  }

Please also cite `Bob`_ as the base framework you're using::

  @inproceedings{bob2012,
    author = {A. Anjos AND L. El Shafey AND R. Wallace AND
              M. G\"unther AND C. McCool AND S. Marcel},
    title = {Bob: a free signal processing and machine learning toolbox for researchers},
    year = {2012},
    month = oct,
    booktitle = {20th ACM Conference on Multimedia Systems (ACMMM), Nara, Japan},
    publisher = {ACM Press},
    url = {http://publications.idiap.ch/downloads/papers/2012/Anjos_Bob_ACMMM12.pdf},
  }


Installation Notes
------------------

`Menpo`_ requires the package `cyvlfeat`_ to be properly installed before the
model built-in this package can be loaded. In order to compile `cyvlfeat`_, the
library `VLFeat`_ must be installed on the system, with SIFT extensions
compiled in. If you use this package through MacPorts or Ubuntu, then execute
our `binary installation instructions`_ and you'll be almost all set.

.. note::

   If you use MacPorts, install the package ``py27-scikit-learn`` as it is
   required by menpofit::

     $ sudo port install py27-scikit-learn

   If you use Python3.4, you may also install ``py34-scikit-learn``.

.. note::

   If you use Ubuntu, you may *optionally* install the package python-sklearn
   as it is required by menpofit::

     $ sudo apt-get install python-sklearn

   Scikit Learn is, unfortunately, not available in precompiled format for
   Ubuntu as of today (February/2016).


You may then bootstrap your buildout like this::

  $ python bootstrap-buildout.py
  $ ./bin/buildout

If your system depends on an incomplete version of VLFeat without SIFT support,
such as in a pure Debian distribution, then you'll need to do slightly
different, as we need to build and compile `VLFeat`_ prior to `cyvlfeat`_. For
this purpose, use a slightly different buildout procedure::

  $ python bootstrap-buildout.py
  $ ./bin/buildout -c debian.cfg

This buildout will download and compile `VLFeat` locally before attempting to
build `cyvlfeat`.


Usage
-----

After installing this package, simply call the program ``detect_landmarks.py``
from the command-line. It has a self-explanatory help message::

  $ ./bin/detect_landmarks.py --help


.. _bob: https://www.idiap.ch/software/bob/
.. _menpo: http://www.menpo.org/
.. _ibug: http://ibug.doc.ic.ac.uk/
.. _cyvlfeat: http://github.com/menpo/cyvlfeat/
.. _vlfeat: http://www.vlfeat.org/
.. _binary installation instructions: https://github.com/idiap/bob/wiki/Binary-Installation
