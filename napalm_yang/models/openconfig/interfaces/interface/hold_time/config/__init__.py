
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
 long = int
 unicode = str

class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/hold-time/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for interface hold-time settings.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__up','__down',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__down = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="down", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='uint32', is_config=True)
    self.__up = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='uint32', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'interfaces', u'interface', u'hold-time', u'config']

  def _get_up(self):
    """
    Getter method for up, mapped from YANG variable /interfaces/interface/hold_time/config/up (uint32)

    YANG Description: Dampens advertisement when the interface
transitions from down to up.  A zero value means dampening
is turned off, i.e., immediate notification.
    """
    return self.__up
      
  def _set_up(self, v, load=False):
    """
    Setter method for up, mapped from YANG variable /interfaces/interface/hold_time/config/up (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_up is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_up() directly.

    YANG Description: Dampens advertisement when the interface
transitions from down to up.  A zero value means dampening
is turned off, i.e., immediate notification.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """up must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='uint32', is_config=True)""",
        })

    self.__up = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_up(self):
    self.__up = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='uint32', is_config=True)


  def _get_down(self):
    """
    Getter method for down, mapped from YANG variable /interfaces/interface/hold_time/config/down (uint32)

    YANG Description: Dampens advertisement when the interface transitions from
up to down.  A zero value means dampening is turned off,
i.e., immediate notification.
    """
    return self.__down
      
  def _set_down(self, v, load=False):
    """
    Setter method for down, mapped from YANG variable /interfaces/interface/hold_time/config/down (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_down is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_down() directly.

    YANG Description: Dampens advertisement when the interface transitions from
up to down.  A zero value means dampening is turned off,
i.e., immediate notification.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="down", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """down must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="down", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='uint32', is_config=True)""",
        })

    self.__down = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_down(self):
    self.__down = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="down", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='uint32', is_config=True)

  up = __builtin__.property(_get_up, _set_up)
  down = __builtin__.property(_get_down, _set_down)


  _pyangbind_elements = {'up': up, 'down': down, }


