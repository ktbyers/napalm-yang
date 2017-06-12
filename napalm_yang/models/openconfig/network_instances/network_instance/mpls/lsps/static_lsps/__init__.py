
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

import static_lsp
class static_lsps(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/lsps/static-lsps. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: statically configured LSPs, without dynamic
signaling
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__static_lsp',)

  _yang_name = 'static-lsps'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__static_lsp = YANGDynClass(base=YANGListType("name",static_lsp.static_lsp, yang_name="static-lsp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="static-lsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'static-lsps']

  def _get_static_lsp(self):
    """
    Getter method for static_lsp, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp (list)

    YANG Description: list of defined static LSPs
    """
    return self.__static_lsp
      
  def _set_static_lsp(self, v, load=False):
    """
    Setter method for static_lsp, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static_lsp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static_lsp() directly.

    YANG Description: list of defined static LSPs
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",static_lsp.static_lsp, yang_name="static-lsp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="static-lsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static_lsp must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",static_lsp.static_lsp, yang_name="static-lsp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="static-lsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__static_lsp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static_lsp(self):
    self.__static_lsp = YANGDynClass(base=YANGListType("name",static_lsp.static_lsp, yang_name="static-lsp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="static-lsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  static_lsp = __builtin__.property(_get_static_lsp, _set_static_lsp)


  _pyangbind_elements = {'static_lsp': static_lsp, }


import static_lsp
class static_lsps(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/lsps/static-lsps. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: statically configured LSPs, without dynamic
signaling
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__static_lsp',)

  _yang_name = 'static-lsps'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__static_lsp = YANGDynClass(base=YANGListType("name",static_lsp.static_lsp, yang_name="static-lsp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="static-lsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'static-lsps']

  def _get_static_lsp(self):
    """
    Getter method for static_lsp, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp (list)

    YANG Description: list of defined static LSPs
    """
    return self.__static_lsp
      
  def _set_static_lsp(self, v, load=False):
    """
    Setter method for static_lsp, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static_lsp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static_lsp() directly.

    YANG Description: list of defined static LSPs
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",static_lsp.static_lsp, yang_name="static-lsp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="static-lsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static_lsp must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",static_lsp.static_lsp, yang_name="static-lsp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="static-lsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__static_lsp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static_lsp(self):
    self.__static_lsp = YANGDynClass(base=YANGListType("name",static_lsp.static_lsp, yang_name="static-lsp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="static-lsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  static_lsp = __builtin__.property(_get_static_lsp, _set_static_lsp)


  _pyangbind_elements = {'static_lsp': static_lsp, }


