# -*- coding: utf-8 -*-

import os

from radish.Colorful import colorful
from radish.Scenario import Scenario

class Feature( object ):
  def __init__( self, id, sentence, filename ):
    self.id = id
    self.sentence = sentence
    self.filename = filename
    self.scenarios = []
    self.description = ""

  @property
  def Scenarios( self ):
    return self.scenarios

  def AppendScenario( self, scenario ):
    if isinstance( scenario, Scenario ):
      self.scenarios.append( scenario )

  def AppendDescriptionLine( self, line ):
    if self.description == "":
      self.description = line
    else:
      self.description += os.linesep + line

  def write( self ):
    colorful.out.bold_white( "  " + self.sentence )
    for l in self.description.splitlines( ): colorful.out.white( "    " + l )
    print( "" )
