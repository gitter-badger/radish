#!/usr/bin/python
# -*- coding: utf-8 -*-

import radish

import os
import time
#import argparse
import optparse

def main( ):
  parser = optparse.OptionParser( description = "radish is a smart 'Test-Driven Developement'-Tool", epilog = "(C) Copyright 2012 by Timo Furrer <tuxtimo@gmail.com>" )
  parser.add_option( "-b", "--basedir",
                    dest    = "basedir",
                    default = os.path.join( os.getcwd( ), "radish" ),
                    help    = "The basedir is used to locate the steps.py and terrain.py"
                  )
  parser.add_option( "-a", "--abort-fail",
                     dest   = "abort_fail",
                     action = "store_true",
                     help   = "If one feature file fails this option will stop the execution"
                   )
  parser.add_option( "-v", "--verbosity",
                     dest    = "verbosity",
                     default = 1,
                     help    = "The verbosity level for the output"
                   )
  parser.add_option( "-m", "--marker",
                     dest    = "marker",
                     default = int( time.time( )),
                     help    = "A specific marker for the step loggings"
                   )
  parser.add_option( "-d", "--dry-run",
                     dest    = "dry_run",
                     action  = "store_true",
                     help    = "Executes a dry run to validate steps"
                   )
  parser.add_option( "--with-xunit",
                     dest    = "with_xunit",
                     action  = "store_true",
                     default = False,
                     help    = "Generate JUnit xml report to a file"
                   )
  parser.add_option( "--xunit-file",
                     dest    = "xunit_file",
                     default = None,
                     help    = "Location where to write to JUnit xml report file"
                   )

  options, args = parser.parse_args( )

  # initialize config object
  cf = radish.Config( )
  cf.SetBasedir( radish.FileSystemHelper.expand( options.basedir ))
  cf.feature_files = args
  cf.abort_fail    = options.abort_fail
  cf.verbosity     = options.verbosity
  cf.marker        = options.marker
  cf.dry_run       = options.dry_run
  cf.with_xunit    = options.with_xunit
  cf.xunit_file    = options.xunit_file

  # parse feature files
  fp = radish.FeatureParser( )
  fp.parse( )

  # load terrain and steps
  loader = radish.Loader( fp.Features )
  loader.load( )

  # run the features
  runner = radish.Runner( fp.Features )
  endResult = runner.run( )

  # report writer
  if cf.with_xunit:
    rw = radish.ReportWriter( endResult )
    rw.write( )

if __name__ == "__main__":
  main( )
