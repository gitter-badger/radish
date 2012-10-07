# -*- coding: utf-8 -*-

import os

from radish.Scenario import Scenario

class Feature( object ):
  def __init__( self, id, sentence, filename ):
    self.id = id
    self.sentence = sentence
    self.filename = filename
    self.scenarios = []
    self.description = ""

  @property
  def Id( self ):
    return self.id

  @property
  def Sentence( self ):
    return self.sentence

  @property
  def Scenarios( self ):
    return self.scenarios

  @property
  def Passed( self ):
    for s in self.scenarios:
      if not s.Passed: return False
    return True

  def AppendScenario( self, scenario ):
    if isinstance( scenario, Scenario ):
      self.scenarios.append( scenario )

  def AppendDescriptionLine( self, line ):
    if self.description == "":
      self.description = line
    else:
      self.description += os.linesep + line
