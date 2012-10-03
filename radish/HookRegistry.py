# -*- coding: utf-8 -*-

class HookRegistry( object ):
  hooks = {
    "all": {
      "before": [],
      "after": []
    },
    "feature": {
      "before": [],
      "after": []
    },
    "scenario": {
      "before": [],
      "after": []
    },
    "step": {
      "before": [],
      "after": []
    }
  }

  possible_hooks = (( "all", "all" ), ( "feature", "each_feature" ), ( "scenario", "each_scenario" ), ( "step", "each_step" ))

  def __new__( type, *args ):
    if not "instance" in type.__dict__:
      type.instance = object.__new__( type )
    return type.instance

  class Hooker( object ):
    def __init__( self, when ):
      self.when = when

    @classmethod
    def _add_hook( cls, what, name ):
      def wrapper( self, func ):
        HookRegistry( ).register( self.when, what, func )
        return func
      wrapper.__name__ = wrapper.fn_name = name
      setattr( cls, name, wrapper )

  def register( self, when, what, func ):
    self.hooks[what][when].append( func )

  def call_hook( self, when, what, *args, **kw ):
    for h in self.hooks[what][when]:
      h( *args, **kw )

for what, name in HookRegistry.possible_hooks:
  HookRegistry.Hooker._add_hook( what, name )

before = HookRegistry.Hooker( "before" )
after = HookRegistry.Hooker( "after" )
