# -*- coding: utf-8 -*-

class Step( object ):
  def __init__( self, id, sentence, filename ):
    self.id = id
    self.sentence = sentence
    self.filename = filename
    self.func = None
  @property
  def Sentence( self ):
    return self.sentence
