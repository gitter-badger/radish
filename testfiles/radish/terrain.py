from radish import *

@before.all
def before_all( ):
  #print "before_all"
  pass

@after.all
def after_all( ):
  #print "after_all"
  pass

@before.each_feature
def bef( feature ):
  #print "Before feature: " + feature.sentence
  pass

@after.each_feature
def aef( feature ):
  #print "After feature: " + feature.sentence
  pass

@before.each_scenario
def bes( scenario ):
  #print "Before scenario: " + scenario.sentence
  pass

@after.each_scenario
def aes( scenario ):
  #print "After scenario: " + scenario.sentence
  pass

@before.each_step
def bestep( step ):
  #print "Before step: " + step.sentence
  pass

@after.each_step
def aestep( step ):
  #print "After step: " + step.sentence
  pass