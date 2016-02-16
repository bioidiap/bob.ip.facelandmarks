.. vim: set fileencoding=utf-8 :
.. Andre Anjos <andre.anjos@idiap.ch>
.. Tue 16 Feb 2016 15:38:40 CET

.. image:: http://img.shields.io/badge/docs-stable-yellow.png
   :target: http://pythonhosted.org/bob.ip.menpofit/index.html
.. image:: http://img.shields.io/badge/docs-latest-orange.png
   :target: https://www.idiap.ch/software/bob/docs/latest/bioidiap/bob.ip.menpofit/master/index.html
.. image:: https://travis-ci.org/bioidiap/bob.ip.menpofit.svg?branch=master
   :target: https://travis-ci.org/bioidiap/bob.ip.menpofit?branch=master
.. image:: https://coveralls.io/repos/bioidiap/bob.ip.menpofit/badge.svg?branch=master
   :target: https://coveralls.io/r/bioidiap/bob.ip.menpofit?branch=master
.. image:: https://img.shields.io/badge/github-master-0000c0.png
   :target: https://github.com/bioidiap/bob.ip.menpofit/tree/master
.. image:: http://img.shields.io/pypi/v/bob.ip.menpofit.png
   :target: https://pypi.python.org/pypi/bob.ip.menpofit
.. image:: http://img.shields.io/pypi/dm/bob.ip.menpofit.png
   :target: https://pypi.python.org/pypi/bob.ip.menpofit

========================================
 Face Keypoint Detection using menpofit
========================================

This package includes a `Bob`_ interface to `menpofit`_ allowing you to detect
keypoints on faces from images and videos. The model was provided by
Epameinondas Antonakos from the `iBug`_ laboratory at Imperial College, London,
UK.


Usage
-----

After installing this package, simply call the program ``detect_keypoints.py``
from the command-line. It has a self-explanatory help message::

  $ ./bin/detect_keypoints.py --help


.. _bob: https://www.idiap.ch/software/bob/
.. _menpofit: http://www.menpo.org/
.. _ibug: http://ibug.doc.ic.ac.uk/
