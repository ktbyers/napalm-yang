
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

import level1_to_level2
import level2_to_level1
class inter_level_propagation_policies(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/global/inter-level-propagation-policies. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Policies to propagate prefixes between IS-IS levels.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__level1_to_level2','__level2_to_level1',)

  _yang_name = 'inter-level-propagation-policies'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__level1_to_level2 = YANGDynClass(base=level1_to_level2.level1_to_level2, is_container='container', yang_name="level1-to-level2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__level2_to_level1 = YANGDynClass(base=level2_to_level1.level2_to_level1, is_container='container', yang_name="level2-to-level1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'global', u'inter-level-propagation-policies']

  def _get_level1_to_level2(self):
    """
    Getter method for level1_to_level2, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/inter_level_propagation_policies/level1_to_level2 (container)

    YANG Description: Policies relating to prefixes to be propagated from
Level 1 to Level 2.
    """
    return self.__level1_to_level2
      
  def _set_level1_to_level2(self, v, load=False):
    """
    Setter method for level1_to_level2, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/inter_level_propagation_policies/level1_to_level2 (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_level1_to_level2 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_level1_to_level2() directly.

    YANG Description: Policies relating to prefixes to be propagated from
Level 1 to Level 2.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=level1_to_level2.level1_to_level2, is_container='container', yang_name="level1-to-level2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """level1_to_level2 must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=level1_to_level2.level1_to_level2, is_container='container', yang_name="level1-to-level2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__level1_to_level2 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_level1_to_level2(self):
    self.__level1_to_level2 = YANGDynClass(base=level1_to_level2.level1_to_level2, is_container='container', yang_name="level1-to-level2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_level2_to_level1(self):
    """
    Getter method for level2_to_level1, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/inter_level_propagation_policies/level2_to_level1 (container)

    YANG Description: Policies relating to prefixes to be propagated from
Level2 to Level 1.
    """
    return self.__level2_to_level1
      
  def _set_level2_to_level1(self, v, load=False):
    """
    Setter method for level2_to_level1, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/inter_level_propagation_policies/level2_to_level1 (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_level2_to_level1 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_level2_to_level1() directly.

    YANG Description: Policies relating to prefixes to be propagated from
Level2 to Level 1.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=level2_to_level1.level2_to_level1, is_container='container', yang_name="level2-to-level1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """level2_to_level1 must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=level2_to_level1.level2_to_level1, is_container='container', yang_name="level2-to-level1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__level2_to_level1 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_level2_to_level1(self):
    self.__level2_to_level1 = YANGDynClass(base=level2_to_level1.level2_to_level1, is_container='container', yang_name="level2-to-level1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  level1_to_level2 = __builtin__.property(_get_level1_to_level2, _set_level1_to_level2)
  level2_to_level1 = __builtin__.property(_get_level2_to_level1, _set_level2_to_level1)


  _pyangbind_elements = {'level1_to_level2': level1_to_level2, 'level2_to_level1': level2_to_level1, }


import level1_to_level2
import level2_to_level1
class inter_level_propagation_policies(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/global/inter-level-propagation-policies. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Policies to propagate prefixes between IS-IS levels.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__level1_to_level2','__level2_to_level1',)

  _yang_name = 'inter-level-propagation-policies'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__level1_to_level2 = YANGDynClass(base=level1_to_level2.level1_to_level2, is_container='container', yang_name="level1-to-level2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__level2_to_level1 = YANGDynClass(base=level2_to_level1.level2_to_level1, is_container='container', yang_name="level2-to-level1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'global', u'inter-level-propagation-policies']

  def _get_level1_to_level2(self):
    """
    Getter method for level1_to_level2, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/inter_level_propagation_policies/level1_to_level2 (container)

    YANG Description: Policies relating to prefixes to be propagated from
Level 1 to Level 2.
    """
    return self.__level1_to_level2
      
  def _set_level1_to_level2(self, v, load=False):
    """
    Setter method for level1_to_level2, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/inter_level_propagation_policies/level1_to_level2 (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_level1_to_level2 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_level1_to_level2() directly.

    YANG Description: Policies relating to prefixes to be propagated from
Level 1 to Level 2.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=level1_to_level2.level1_to_level2, is_container='container', yang_name="level1-to-level2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """level1_to_level2 must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=level1_to_level2.level1_to_level2, is_container='container', yang_name="level1-to-level2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__level1_to_level2 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_level1_to_level2(self):
    self.__level1_to_level2 = YANGDynClass(base=level1_to_level2.level1_to_level2, is_container='container', yang_name="level1-to-level2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_level2_to_level1(self):
    """
    Getter method for level2_to_level1, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/inter_level_propagation_policies/level2_to_level1 (container)

    YANG Description: Policies relating to prefixes to be propagated from
Level2 to Level 1.
    """
    return self.__level2_to_level1
      
  def _set_level2_to_level1(self, v, load=False):
    """
    Setter method for level2_to_level1, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/inter_level_propagation_policies/level2_to_level1 (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_level2_to_level1 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_level2_to_level1() directly.

    YANG Description: Policies relating to prefixes to be propagated from
Level2 to Level 1.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=level2_to_level1.level2_to_level1, is_container='container', yang_name="level2-to-level1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """level2_to_level1 must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=level2_to_level1.level2_to_level1, is_container='container', yang_name="level2-to-level1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__level2_to_level1 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_level2_to_level1(self):
    self.__level2_to_level1 = YANGDynClass(base=level2_to_level1.level2_to_level1, is_container='container', yang_name="level2-to-level1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  level1_to_level2 = __builtin__.property(_get_level1_to_level2, _set_level1_to_level2)
  level2_to_level1 = __builtin__.property(_get_level2_to_level1, _set_level2_to_level1)


  _pyangbind_elements = {'level1_to_level2': level1_to_level2, 'level2_to_level1': level2_to_level1, }


