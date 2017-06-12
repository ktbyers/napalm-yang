
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

class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/ipv4-internal-reachability/prefixes/prefixes/error-metric/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of error-metric.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__metric','__flags',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..63']}), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:narrow-metric', is_config=False)
    self.__flags = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INTERNAL': {}, u'UNSUPPORTED': {}},)), is_leaf=False, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='isis-metric-flags', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'ipv4-internal-reachability', u'prefixes', u'prefixes', u'error-metric', u'state']

  def _get_metric(self):
    """
    Getter method for metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_internal_reachability/prefixes/prefixes/error_metric/state/metric (oc-isis-types:narrow-metric)

    YANG Description: ISIS error metric value. This metric measures the residual error
probability of the associated circuit. It is an optional metric,
which if assigned to a circuit shall have a non-zero value. Higher
values indicate a larger probability of undetected errors on the
circuit.
    """
    return self.__metric
      
  def _set_metric(self, v, load=False):
    """
    Setter method for metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_internal_reachability/prefixes/prefixes/error_metric/state/metric (oc-isis-types:narrow-metric)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_metric() directly.

    YANG Description: ISIS error metric value. This metric measures the residual error
probability of the associated circuit. It is an optional metric,
which if assigned to a circuit shall have a non-zero value. Higher
values indicate a larger probability of undetected errors on the
circuit.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..63']}), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:narrow-metric', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """metric must be of a type compatible with oc-isis-types:narrow-metric""",
          'defined-type': "oc-isis-types:narrow-metric",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..63']}), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:narrow-metric', is_config=False)""",
        })

    self.__metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_metric(self):
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..63']}), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:narrow-metric', is_config=False)


  def _get_flags(self):
    """
    Getter method for flags, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_internal_reachability/prefixes/prefixes/error_metric/state/flags (isis-metric-flags)

    YANG Description: IS-IS error metric flags.
    """
    return self.__flags
      
  def _set_flags(self, v, load=False):
    """
    Setter method for flags, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_internal_reachability/prefixes/prefixes/error_metric/state/flags (isis-metric-flags)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_flags is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_flags() directly.

    YANG Description: IS-IS error metric flags.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INTERNAL': {}, u'UNSUPPORTED': {}},)), is_leaf=False, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='isis-metric-flags', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """flags must be of a type compatible with isis-metric-flags""",
          'defined-type': "openconfig-network-instance:isis-metric-flags",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INTERNAL': {}, u'UNSUPPORTED': {}},)), is_leaf=False, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='isis-metric-flags', is_config=False)""",
        })

    self.__flags = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_flags(self):
    self.__flags = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INTERNAL': {}, u'UNSUPPORTED': {}},)), is_leaf=False, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='isis-metric-flags', is_config=False)

  metric = __builtin__.property(_get_metric)
  flags = __builtin__.property(_get_flags)


  _pyangbind_elements = {'metric': metric, 'flags': flags, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/ipv4-internal-reachability/prefixes/prefixes/error-metric/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of error-metric.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__metric','__flags',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..63']}), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:narrow-metric', is_config=False)
    self.__flags = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INTERNAL': {}, u'UNSUPPORTED': {}},)), is_leaf=False, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='isis-metric-flags', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'ipv4-internal-reachability', u'prefixes', u'prefixes', u'error-metric', u'state']

  def _get_metric(self):
    """
    Getter method for metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_internal_reachability/prefixes/prefixes/error_metric/state/metric (oc-isis-types:narrow-metric)

    YANG Description: ISIS error metric value. This metric measures the residual error
probability of the associated circuit. It is an optional metric,
which if assigned to a circuit shall have a non-zero value. Higher
values indicate a larger probability of undetected errors on the
circuit.
    """
    return self.__metric
      
  def _set_metric(self, v, load=False):
    """
    Setter method for metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_internal_reachability/prefixes/prefixes/error_metric/state/metric (oc-isis-types:narrow-metric)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_metric() directly.

    YANG Description: ISIS error metric value. This metric measures the residual error
probability of the associated circuit. It is an optional metric,
which if assigned to a circuit shall have a non-zero value. Higher
values indicate a larger probability of undetected errors on the
circuit.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..63']}), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:narrow-metric', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """metric must be of a type compatible with oc-isis-types:narrow-metric""",
          'defined-type': "oc-isis-types:narrow-metric",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..63']}), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:narrow-metric', is_config=False)""",
        })

    self.__metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_metric(self):
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..63']}), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:narrow-metric', is_config=False)


  def _get_flags(self):
    """
    Getter method for flags, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_internal_reachability/prefixes/prefixes/error_metric/state/flags (isis-metric-flags)

    YANG Description: IS-IS error metric flags.
    """
    return self.__flags
      
  def _set_flags(self, v, load=False):
    """
    Setter method for flags, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_internal_reachability/prefixes/prefixes/error_metric/state/flags (isis-metric-flags)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_flags is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_flags() directly.

    YANG Description: IS-IS error metric flags.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INTERNAL': {}, u'UNSUPPORTED': {}},)), is_leaf=False, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='isis-metric-flags', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """flags must be of a type compatible with isis-metric-flags""",
          'defined-type': "openconfig-network-instance:isis-metric-flags",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INTERNAL': {}, u'UNSUPPORTED': {}},)), is_leaf=False, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='isis-metric-flags', is_config=False)""",
        })

    self.__flags = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_flags(self):
    self.__flags = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INTERNAL': {}, u'UNSUPPORTED': {}},)), is_leaf=False, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='isis-metric-flags', is_config=False)

  metric = __builtin__.property(_get_metric)
  flags = __builtin__.property(_get_flags)


  _pyangbind_elements = {'metric': metric, 'flags': flags, }


