
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-isn/neighbors/neighbor/subTLVs/subTLVs/lan-adjacency-sid/sid/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of LAN Adjacency-SID.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__value','__flags','__weight','__neighbor_id',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__flags = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LOCAL': {}, u'SET': {}, u'BACKUP': {}, u'ADDRESS_FAMILY': {}, u'VALUE': {}},)), is_leaf=False, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)
    self.__weight = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    self.__value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    self.__neighbor_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}'}), is_leaf=True, yang_name="neighbor-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:system-id', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'mt-isn', u'neighbors', u'neighbor', u'subTLVs', u'subTLVs', u'lan-adjacency-sid', u'sid', u'state']

  def _get_value(self):
    """
    Getter method for value, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subTLVs/subTLVs/lan_adjacency_sid/sid/state/value (uint32)

    YANG Description: LAN Adjacency-SID value.
    """
    return self.__value
      
  def _set_value(self, v, load=False):
    """
    Setter method for value, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subTLVs/subTLVs/lan_adjacency_sid/sid/state/value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_value() directly.

    YANG Description: LAN Adjacency-SID value.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_value(self):
    self.__value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)


  def _get_flags(self):
    """
    Getter method for flags, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subTLVs/subTLVs/lan_adjacency_sid/sid/state/flags (enumeration)

    YANG Description: Flags associated with LAN-Adj-Segment-ID.
    """
    return self.__flags
      
  def _set_flags(self, v, load=False):
    """
    Setter method for flags, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subTLVs/subTLVs/lan_adjacency_sid/sid/state/flags (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_flags is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_flags() directly.

    YANG Description: Flags associated with LAN-Adj-Segment-ID.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LOCAL': {}, u'SET': {}, u'BACKUP': {}, u'ADDRESS_FAMILY': {}, u'VALUE': {}},)), is_leaf=False, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """flags must be of a type compatible with enumeration""",
          'defined-type': "openconfig-network-instance:enumeration",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LOCAL': {}, u'SET': {}, u'BACKUP': {}, u'ADDRESS_FAMILY': {}, u'VALUE': {}},)), is_leaf=False, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)""",
        })

    self.__flags = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_flags(self):
    self.__flags = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LOCAL': {}, u'SET': {}, u'BACKUP': {}, u'ADDRESS_FAMILY': {}, u'VALUE': {}},)), is_leaf=False, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)


  def _get_weight(self):
    """
    Getter method for weight, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subTLVs/subTLVs/lan_adjacency_sid/sid/state/weight (uint8)

    YANG Description: Value that represents the weight of the Adj-SID for the purpose
of load balancing.
    """
    return self.__weight
      
  def _set_weight(self, v, load=False):
    """
    Setter method for weight, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subTLVs/subTLVs/lan_adjacency_sid/sid/state/weight (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_weight is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_weight() directly.

    YANG Description: Value that represents the weight of the Adj-SID for the purpose
of load balancing.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """weight must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__weight = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_weight(self):
    self.__weight = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)


  def _get_neighbor_id(self):
    """
    Getter method for neighbor_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subTLVs/subTLVs/lan_adjacency_sid/sid/state/neighbor_id (oc-isis-types:system-id)

    YANG Description: System ID of the neighbor associated with the LAN-Adj-Segment-ID
value.
    """
    return self.__neighbor_id
      
  def _set_neighbor_id(self, v, load=False):
    """
    Setter method for neighbor_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subTLVs/subTLVs/lan_adjacency_sid/sid/state/neighbor_id (oc-isis-types:system-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor_id() directly.

    YANG Description: System ID of the neighbor associated with the LAN-Adj-Segment-ID
value.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}'}), is_leaf=True, yang_name="neighbor-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:system-id', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor_id must be of a type compatible with oc-isis-types:system-id""",
          'defined-type': "oc-isis-types:system-id",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}'}), is_leaf=True, yang_name="neighbor-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:system-id', is_config=False)""",
        })

    self.__neighbor_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor_id(self):
    self.__neighbor_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}'}), is_leaf=True, yang_name="neighbor-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:system-id', is_config=False)

  value = __builtin__.property(_get_value)
  flags = __builtin__.property(_get_flags)
  weight = __builtin__.property(_get_weight)
  neighbor_id = __builtin__.property(_get_neighbor_id)


  _pyangbind_elements = {'value': value, 'flags': flags, 'weight': weight, 'neighbor_id': neighbor_id, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-isn/neighbors/neighbor/subTLVs/subTLVs/lan-adjacency-sid/sid/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of LAN Adjacency-SID.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__value','__flags','__weight','__neighbor_id',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__flags = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LOCAL': {}, u'SET': {}, u'BACKUP': {}, u'ADDRESS_FAMILY': {}, u'VALUE': {}},)), is_leaf=False, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)
    self.__weight = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    self.__value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    self.__neighbor_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}'}), is_leaf=True, yang_name="neighbor-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:system-id', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'mt-isn', u'neighbors', u'neighbor', u'subTLVs', u'subTLVs', u'lan-adjacency-sid', u'sid', u'state']

  def _get_value(self):
    """
    Getter method for value, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subTLVs/subTLVs/lan_adjacency_sid/sid/state/value (uint32)

    YANG Description: LAN Adjacency-SID value.
    """
    return self.__value
      
  def _set_value(self, v, load=False):
    """
    Setter method for value, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subTLVs/subTLVs/lan_adjacency_sid/sid/state/value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_value() directly.

    YANG Description: LAN Adjacency-SID value.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_value(self):
    self.__value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)


  def _get_flags(self):
    """
    Getter method for flags, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subTLVs/subTLVs/lan_adjacency_sid/sid/state/flags (enumeration)

    YANG Description: Flags associated with LAN-Adj-Segment-ID.
    """
    return self.__flags
      
  def _set_flags(self, v, load=False):
    """
    Setter method for flags, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subTLVs/subTLVs/lan_adjacency_sid/sid/state/flags (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_flags is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_flags() directly.

    YANG Description: Flags associated with LAN-Adj-Segment-ID.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LOCAL': {}, u'SET': {}, u'BACKUP': {}, u'ADDRESS_FAMILY': {}, u'VALUE': {}},)), is_leaf=False, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """flags must be of a type compatible with enumeration""",
          'defined-type': "openconfig-network-instance:enumeration",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LOCAL': {}, u'SET': {}, u'BACKUP': {}, u'ADDRESS_FAMILY': {}, u'VALUE': {}},)), is_leaf=False, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)""",
        })

    self.__flags = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_flags(self):
    self.__flags = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LOCAL': {}, u'SET': {}, u'BACKUP': {}, u'ADDRESS_FAMILY': {}, u'VALUE': {}},)), is_leaf=False, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)


  def _get_weight(self):
    """
    Getter method for weight, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subTLVs/subTLVs/lan_adjacency_sid/sid/state/weight (uint8)

    YANG Description: Value that represents the weight of the Adj-SID for the purpose
of load balancing.
    """
    return self.__weight
      
  def _set_weight(self, v, load=False):
    """
    Setter method for weight, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subTLVs/subTLVs/lan_adjacency_sid/sid/state/weight (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_weight is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_weight() directly.

    YANG Description: Value that represents the weight of the Adj-SID for the purpose
of load balancing.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """weight must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__weight = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_weight(self):
    self.__weight = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)


  def _get_neighbor_id(self):
    """
    Getter method for neighbor_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subTLVs/subTLVs/lan_adjacency_sid/sid/state/neighbor_id (oc-isis-types:system-id)

    YANG Description: System ID of the neighbor associated with the LAN-Adj-Segment-ID
value.
    """
    return self.__neighbor_id
      
  def _set_neighbor_id(self, v, load=False):
    """
    Setter method for neighbor_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subTLVs/subTLVs/lan_adjacency_sid/sid/state/neighbor_id (oc-isis-types:system-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor_id() directly.

    YANG Description: System ID of the neighbor associated with the LAN-Adj-Segment-ID
value.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}'}), is_leaf=True, yang_name="neighbor-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:system-id', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor_id must be of a type compatible with oc-isis-types:system-id""",
          'defined-type': "oc-isis-types:system-id",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}'}), is_leaf=True, yang_name="neighbor-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:system-id', is_config=False)""",
        })

    self.__neighbor_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor_id(self):
    self.__neighbor_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}'}), is_leaf=True, yang_name="neighbor-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:system-id', is_config=False)

  value = __builtin__.property(_get_value)
  flags = __builtin__.property(_get_flags)
  weight = __builtin__.property(_get_weight)
  neighbor_id = __builtin__.property(_get_neighbor_id)


  _pyangbind_elements = {'value': value, 'flags': flags, 'weight': weight, 'neighbor_id': neighbor_id, }


