
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

import apply_policy
class inter_instance_policies(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/inter-instance-policies. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Policies dictating how RIB or FIB entries are imported
to and exported from this instance
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__apply_policy',)

  _yang_name = 'inter-instance-policies'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__apply_policy = YANGDynClass(base=apply_policy.apply_policy, is_container='container', yang_name="apply-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return [u'network-instances', u'network-instance', u'inter-instance-policies']

  def _get_apply_policy(self):
    """
    Getter method for apply_policy, mapped from YANG variable /network_instances/network_instance/inter_instance_policies/apply_policy (container)

    YANG Description: Anchor point for routing policies in the model.
Import and export policies are with respect to the local
routing table, i.e., export (send) and import (receive),
depending on the context.
    """
    return self.__apply_policy
      
  def _set_apply_policy(self, v, load=False):
    """
    Setter method for apply_policy, mapped from YANG variable /network_instances/network_instance/inter_instance_policies/apply_policy (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_apply_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_apply_policy() directly.

    YANG Description: Anchor point for routing policies in the model.
Import and export policies are with respect to the local
routing table, i.e., export (send) and import (receive),
depending on the context.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=apply_policy.apply_policy, is_container='container', yang_name="apply-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """apply_policy must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=apply_policy.apply_policy, is_container='container', yang_name="apply-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__apply_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_apply_policy(self):
    self.__apply_policy = YANGDynClass(base=apply_policy.apply_policy, is_container='container', yang_name="apply-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  apply_policy = __builtin__.property(_get_apply_policy, _set_apply_policy)


  _pyangbind_elements = {'apply_policy': apply_policy, }


import apply_policy
class inter_instance_policies(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/inter-instance-policies. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Policies dictating how RIB or FIB entries are imported
to and exported from this instance
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__apply_policy',)

  _yang_name = 'inter-instance-policies'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__apply_policy = YANGDynClass(base=apply_policy.apply_policy, is_container='container', yang_name="apply-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return [u'network-instances', u'network-instance', u'inter-instance-policies']

  def _get_apply_policy(self):
    """
    Getter method for apply_policy, mapped from YANG variable /network_instances/network_instance/inter_instance_policies/apply_policy (container)

    YANG Description: Anchor point for routing policies in the model.
Import and export policies are with respect to the local
routing table, i.e., export (send) and import (receive),
depending on the context.
    """
    return self.__apply_policy
      
  def _set_apply_policy(self, v, load=False):
    """
    Setter method for apply_policy, mapped from YANG variable /network_instances/network_instance/inter_instance_policies/apply_policy (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_apply_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_apply_policy() directly.

    YANG Description: Anchor point for routing policies in the model.
Import and export policies are with respect to the local
routing table, i.e., export (send) and import (receive),
depending on the context.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=apply_policy.apply_policy, is_container='container', yang_name="apply-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """apply_policy must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=apply_policy.apply_policy, is_container='container', yang_name="apply-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__apply_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_apply_policy(self):
    self.__apply_policy = YANGDynClass(base=apply_policy.apply_policy, is_container='container', yang_name="apply-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  apply_policy = __builtin__.property(_get_apply_policy, _set_apply_policy)


  _pyangbind_elements = {'apply_policy': apply_policy, }


