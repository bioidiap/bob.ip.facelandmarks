#!/usr/bin/env python
# encoding: utf-8
# Andre Anjos <andre.anjos@idiap.ch>
# Tue 16 Feb 2016 15:52:30 CET

'''Face keypoint detector using menpofit (%(version)s)

Usage:
  %(prog)s [--verbose...] <input> <output>
  %(prog)s (--help | -h)
  %(prog)s (--version | -V)


Options:
  -h, --help             Show this help message and exit
  -v, --verbose          Increases the verbosity (may appear multiple times)
  -V, --version          Show version


Examples:

  To run the keypoint detection over an image and produce an output image
  showing the detected keypoints, do:

    $ %(prog)s image.png output.png

  To dump the extracted keypoints into a machine-readable HDF5 file, do:

    $ %(prog)s image.png keypoints.hdf5

  You can also process video sequences like this:

    $ %(prog)s video.avi output.avi


See '%(prog)s --help' for more information.

'''

import os
import sys
import pkg_resources

import logging
__logging_format__='[%(levelname)s] %(message)s'
logging.basicConfig(format=__logging_format__)
logger = logging.getLogger(__name__)

from docopt import docopt

version = pkg_resources.require('bob.ip.menpofit')[0].version

import bob.io.base
import bob.io.video
import bob.io.image

def main(user_input=None):

  # Parse the command-line arguments
  if user_input is not None:
      arguments = user_input
  else:
      arguments = sys.argv[1:]

  prog = os.path.basename(sys.argv[0])
  completions = dict(
          prog=prog,
          version=version,
          )
  args = docopt(
      __doc__ % completions,
      argv=arguments,
      version='Skin color extraction for videos (%s)' % version,
      )

  # if the user wants more verbosity, lowers the logging level
  if args['--verbose'] == 1: logging.getLogger().setLevel(logging.INFO)
  elif args['--verbose'] >= 2: logging.getLogger().setLevel(logging.DEBUG)

  import numpy as np
  import menpo.io as mio
  import bob.ip.facedetect

  import pkg_resources
  model_file = pkg_resources.resource_filename(__name__,
      os.path.join('..', 'data', 'keypoint_model.pkl.gz'))
  model = mio.import_pickle(model_file)

  # detect the face location on the given image
  data = bob.io.base.load(args['<input>'])
  bounding_box, quality = bob.ip.facedetect.detect_single_face(data)

  # detect keypoints
  keypoints = model.fit_from_bb(data, bounding_box)

  import ipdb; ipdb.set_trace()
