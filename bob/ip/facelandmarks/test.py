#!/usr/bin/env python
# encoding: utf-8
# Andre Anjos <andre.anjos@idiap.ch>
# Wed 17 Feb 14:32:58 CET 2016

'''Test units for bob.ip.facelandmarks'''

import os
import nose.tools
import pkg_resources

import bob.io.base
import bob.io.base.test_utils

from .utils import detect_landmarks, draw_landmarks
from .script.detect_landmarks import main as app


F = lambda n: pkg_resources.resource_filename(__name__, os.path.join('data', n))


def test_lena():
  data = bob.io.base.load(F('lena.jpg'))
  result = detect_landmarks(data, 1)
  nose.tools.eq_(len(result), 1)
  draw_landmarks(data, result)


def test_multiple():
  data = bob.io.base.load(F('multiple-faces.jpg'))
  result = detect_landmarks(data, 5)
  nose.tools.eq_(len(result), 5)
  draw_landmarks(data, result)


def test_app_lena_outputting_image():
  image = F('lena.jpg')
  output = bob.io.base.test_utils.temporary_filename(prefix="bobtest_",
      suffix='.png')
  status = app(['-n1', image, output])
  nose.tools.eq_(status, 0)


def test_app_multiple_outputting_image():
  image = F('multiple-faces.jpg')
  output = bob.io.base.test_utils.temporary_filename(prefix="bobtest_",
      suffix='.png')
  status = app(['-n5', image, output])
  nose.tools.eq_(status, 0)
  assert os.path.exists(output)
  os.remove(output)


def test_app_lena_outputting_image():
  image = F('lena.jpg')
  output = bob.io.base.test_utils.temporary_filename(prefix="bobtest_",
      suffix='.png')
  status = app(['-n1', image, output])
  nose.tools.eq_(status, 0)
  assert os.path.exists(output)
  os.remove(output)


def test_app_lena_outputting_hdf5():
  image = F('lena.jpg')
  output = bob.io.base.test_utils.temporary_filename(prefix="bobtest_",
      suffix='.hdf5')
  status = app(['-n1', image, output])
  nose.tools.eq_(status, 0)
  assert os.path.exists(output)
  os.remove(output)
