# -*- coding: utf-8 -*-

import traceback
import inspect
import sys
import datetime
import time

from radish.Colorful import colorful
from radish.Config import Config
from radish.UtilRegistry import UtilRegistry
from radish.Exceptions import ValidationException

class Step( object ):
  CHARS_PER_LINE = 100

  def __init__( self, id, sentence, filename, line_no ):
    self.id          = id
    self.sentence    = sentence
    self.filename    = filename
    self.line_no     = line_no
    self.func        = None
    self.match       = None
    self.passed      = None
    self.fail_reason = None
    self.starttime   = None
    self.endtime     = None

  @property
  def Id( self ):
    return self.id

  @property
  def LineNo( self ):
    return self.line_no

  @property
  def Sentence( self ):
    return self.sentence

  @property
  def SplittedSentence( self ):
    ur = UtilRegistry( )
    if ur.has_util( "split_sentence" ):
      try:
        return ur.call_util( "split_sentence", self )
      except KeyboardInterrupt, e:
        pass
    splitted = [self.sentence[i:i+Step.CHARS_PER_LINE] for i in range( 0, len( self.sentence ), Step.CHARS_PER_LINE )]
    return len( splitted ), ( "\n" + self.SentenceIndentation ).join( splitted )

  @property
  def Indentation( self ):
    return "  " + " " * ( len( str( Config( ).highest_feature_id )) + len( str( Config( ).highest_scenario_id ))) + "    "

  @property
  def SentenceIndentation( self ):
    return self.Indentation + " " * len( str( Config( ).highest_step_id )) + "  "

  @property
  def DryRun( self ):
    return Config( ).dry_run

  @property
  def Func( self ):
    return self.func

  @property
  def Match( self ):
    return self.match

  @property
  def Passed( self ):
    return self.passed

  @property
  def Duration( self ):
    if self.Passed == True or self.Passed == False:
      td = self.endtime - self.starttime
      return (td.microseconds + (td.seconds + td.days * 24 * 3600) * 1e6) / 1e6
    return -1

  class FailReason( object ):
    def __init__( self, e ):
      self.exception = e
      self.reason = unicode( e )
      self.traceback = traceback.format_exc( e )

  def run( self ):
    kw = self.match.groupdict( )
    try:
      self.starttime = datetime.datetime.now( )
      if kw:
        self.func( self, **kw )
      else:
        self.func( self, *self.match.groups( ))
      self.passed = True
    except Exception, e:
      self.passed = False
      self.fail_reason = Step.FailReason( e )
      if self.DryRun:
        caller = inspect.trace( )[-1]
        sys.stderr.write( "%s:%d: error: %s\n"%( caller[1], caller[2], unicode( e )))
    self.endtime = datetime.datetime.now( )
    return self.passed

  def ValidationError( self, msg ):
    if self.DryRun:
      #caller = inspect.getouterframes( inspect.currentframe( ))[1]
      #sys.stderr.write( "%s:%d: error: %s\n"%( caller[1], caller[2], msg ))
      sys.stderr.write( "%s:%d: error: %s\n"%( self.filename, self.line_no, msg ))
    else:
      raise ValidationException( msg )
