
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/lsps/static-lsps/static-lsp/ingress/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for ingress LSPs
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__next_hop','__incoming_label','__push_label',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__push_label = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="push-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)
    self.__next_hop = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ip-address', is_config=False)
    self.__incoming_label = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="incoming-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)

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
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'static-lsps', u'static-lsp', u'ingress', u'state']

  def _get_next_hop(self):
    """
    Getter method for next_hop, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/ingress/state/next_hop (inet:ip-address)

    YANG Description: next hop IP address for the LSP
    """
    return self.__next_hop
      
  def _set_next_hop(self, v, load=False):
    """
    Setter method for next_hop, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/ingress/state/next_hop (inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_next_hop is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_next_hop() directly.

    YANG Description: next hop IP address for the LSP
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ip-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """next_hop must be of a type compatible with inet:ip-address""",
          'defined-type': "inet:ip-address",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ip-address', is_config=False)""",
        })

    self.__next_hop = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_next_hop(self):
    self.__next_hop = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ip-address', is_config=False)


  def _get_incoming_label(self):
    """
    Getter method for incoming_label, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/ingress/state/incoming_label (oc-mplst:mpls-label)

    YANG Description: label value on the incoming packet
    """
    return self.__incoming_label
      
  def _set_incoming_label(self, v, load=False):
    """
    Setter method for incoming_label, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/ingress/state/incoming_label (oc-mplst:mpls-label)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_incoming_label is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_incoming_label() directly.

    YANG Description: label value on the incoming packet
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="incoming-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """incoming_label must be of a type compatible with oc-mplst:mpls-label""",
          'defined-type': "oc-mplst:mpls-label",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="incoming-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)""",
        })

    self.__incoming_label = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_incoming_label(self):
    self.__incoming_label = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="incoming-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)


  def _get_push_label(self):
    """
    Getter method for push_label, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/ingress/state/push_label (oc-mplst:mpls-label)

    YANG Description: label value to push at the current hop for the
LSP
    """
    return self.__push_label
      
  def _set_push_label(self, v, load=False):
    """
    Setter method for push_label, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/ingress/state/push_label (oc-mplst:mpls-label)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_push_label is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_push_label() directly.

    YANG Description: label value to push at the current hop for the
LSP
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="push-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """push_label must be of a type compatible with oc-mplst:mpls-label""",
          'defined-type': "oc-mplst:mpls-label",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="push-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)""",
        })

    self.__push_label = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_push_label(self):
    self.__push_label = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="push-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)

  next_hop = __builtin__.property(_get_next_hop)
  incoming_label = __builtin__.property(_get_incoming_label)
  push_label = __builtin__.property(_get_push_label)


  _pyangbind_elements = {'next_hop': next_hop, 'incoming_label': incoming_label, 'push_label': push_label, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/lsps/static-lsps/static-lsp/ingress/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for ingress LSPs
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__next_hop','__incoming_label','__push_label',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__push_label = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="push-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)
    self.__next_hop = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ip-address', is_config=False)
    self.__incoming_label = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="incoming-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)

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
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'static-lsps', u'static-lsp', u'ingress', u'state']

  def _get_next_hop(self):
    """
    Getter method for next_hop, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/ingress/state/next_hop (inet:ip-address)

    YANG Description: next hop IP address for the LSP
    """
    return self.__next_hop
      
  def _set_next_hop(self, v, load=False):
    """
    Setter method for next_hop, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/ingress/state/next_hop (inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_next_hop is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_next_hop() directly.

    YANG Description: next hop IP address for the LSP
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ip-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """next_hop must be of a type compatible with inet:ip-address""",
          'defined-type': "inet:ip-address",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ip-address', is_config=False)""",
        })

    self.__next_hop = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_next_hop(self):
    self.__next_hop = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ip-address', is_config=False)


  def _get_incoming_label(self):
    """
    Getter method for incoming_label, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/ingress/state/incoming_label (oc-mplst:mpls-label)

    YANG Description: label value on the incoming packet
    """
    return self.__incoming_label
      
  def _set_incoming_label(self, v, load=False):
    """
    Setter method for incoming_label, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/ingress/state/incoming_label (oc-mplst:mpls-label)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_incoming_label is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_incoming_label() directly.

    YANG Description: label value on the incoming packet
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="incoming-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """incoming_label must be of a type compatible with oc-mplst:mpls-label""",
          'defined-type': "oc-mplst:mpls-label",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="incoming-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)""",
        })

    self.__incoming_label = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_incoming_label(self):
    self.__incoming_label = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="incoming-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)


  def _get_push_label(self):
    """
    Getter method for push_label, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/ingress/state/push_label (oc-mplst:mpls-label)

    YANG Description: label value to push at the current hop for the
LSP
    """
    return self.__push_label
      
  def _set_push_label(self, v, load=False):
    """
    Setter method for push_label, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/ingress/state/push_label (oc-mplst:mpls-label)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_push_label is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_push_label() directly.

    YANG Description: label value to push at the current hop for the
LSP
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="push-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """push_label must be of a type compatible with oc-mplst:mpls-label""",
          'defined-type': "oc-mplst:mpls-label",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="push-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)""",
        })

    self.__push_label = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_push_label(self):
    self.__push_label = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'16..1048575']}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NO_LABEL': {}, u'IPV6_EXPLICIT_NULL': {'value': 2}, u'ENTROPY_LABEL_INDICATOR': {'value': 7}, u'IPV4_EXPLICIT_NULL': {'value': 0}, u'ROUTER_ALERT': {'value': 1}, u'IMPLICIT_NULL': {'value': 3}},),], is_leaf=True, yang_name="push-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)

  next_hop = __builtin__.property(_get_next_hop)
  incoming_label = __builtin__.property(_get_incoming_label)
  push_label = __builtin__.property(_get_push_label)


  _pyangbind_elements = {'next_hop': next_hop, 'incoming_label': incoming_label, 'push_label': push_label, }


