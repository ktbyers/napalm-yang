
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/traffic-engineering/tlvs/tlv/link/sub-tlvs/sub-tlv/unreserved-bandwidths/unreserved-bandwidth/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters relating to the unreserved
bandwidth of the link being described
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__priority','__unreserved_bandwidth',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    self.__unreserved_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=bitarray, restriction_dict={'length': [u'32']}), is_leaf=True, yang_name="unreserved-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'opaque-lsa', u'traffic-engineering', u'tlvs', u'tlv', u'link', u'sub-tlvs', u'sub-tlv', u'unreserved-bandwidths', u'unreserved-bandwidth', u'state']

  def _get_priority(self):
    """
    Getter method for priority, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/unreserved_bandwidths/unreserved_bandwidth/state/priority (uint8)

    YANG Description: The priority level being described
    """
    return self.__priority
      
  def _set_priority(self, v, load=False):
    """
    Setter method for priority, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/unreserved_bandwidths/unreserved_bandwidth/state/priority (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority() directly.

    YANG Description: The priority level being described
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority(self):
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)


  def _get_unreserved_bandwidth(self):
    """
    Getter method for unreserved_bandwidth, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/unreserved_bandwidths/unreserved_bandwidth/state/unreserved_bandwidth (oc-types:ieeefloat32)

    YANG Description: The unreserved bandwidth for at priority level P, where P is
equal to the priority of the current list entry. The reservable
bandwidth at priority P is equal to the sum of the reservable
bandwidth at all levels 0..P.
    """
    return self.__unreserved_bandwidth
      
  def _set_unreserved_bandwidth(self, v, load=False):
    """
    Setter method for unreserved_bandwidth, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/unreserved_bandwidths/unreserved_bandwidth/state/unreserved_bandwidth (oc-types:ieeefloat32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unreserved_bandwidth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unreserved_bandwidth() directly.

    YANG Description: The unreserved bandwidth for at priority level P, where P is
equal to the priority of the current list entry. The reservable
bandwidth at priority P is equal to the sum of the reservable
bandwidth at all levels 0..P.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=bitarray, restriction_dict={'length': [u'32']}), is_leaf=True, yang_name="unreserved-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unreserved_bandwidth must be of a type compatible with oc-types:ieeefloat32""",
          'defined-type': "oc-types:ieeefloat32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=bitarray, restriction_dict={'length': [u'32']}), is_leaf=True, yang_name="unreserved-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)""",
        })

    self.__unreserved_bandwidth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unreserved_bandwidth(self):
    self.__unreserved_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=bitarray, restriction_dict={'length': [u'32']}), is_leaf=True, yang_name="unreserved-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)

  priority = __builtin__.property(_get_priority)
  unreserved_bandwidth = __builtin__.property(_get_unreserved_bandwidth)


  _pyangbind_elements = {'priority': priority, 'unreserved_bandwidth': unreserved_bandwidth, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/traffic-engineering/tlvs/tlv/link/sub-tlvs/sub-tlv/unreserved-bandwidths/unreserved-bandwidth/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters relating to the unreserved
bandwidth of the link being described
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__priority','__unreserved_bandwidth',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    self.__unreserved_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=bitarray, restriction_dict={'length': [u'32']}), is_leaf=True, yang_name="unreserved-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'opaque-lsa', u'traffic-engineering', u'tlvs', u'tlv', u'link', u'sub-tlvs', u'sub-tlv', u'unreserved-bandwidths', u'unreserved-bandwidth', u'state']

  def _get_priority(self):
    """
    Getter method for priority, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/unreserved_bandwidths/unreserved_bandwidth/state/priority (uint8)

    YANG Description: The priority level being described
    """
    return self.__priority
      
  def _set_priority(self, v, load=False):
    """
    Setter method for priority, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/unreserved_bandwidths/unreserved_bandwidth/state/priority (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority() directly.

    YANG Description: The priority level being described
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority(self):
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)


  def _get_unreserved_bandwidth(self):
    """
    Getter method for unreserved_bandwidth, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/unreserved_bandwidths/unreserved_bandwidth/state/unreserved_bandwidth (oc-types:ieeefloat32)

    YANG Description: The unreserved bandwidth for at priority level P, where P is
equal to the priority of the current list entry. The reservable
bandwidth at priority P is equal to the sum of the reservable
bandwidth at all levels 0..P.
    """
    return self.__unreserved_bandwidth
      
  def _set_unreserved_bandwidth(self, v, load=False):
    """
    Setter method for unreserved_bandwidth, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/unreserved_bandwidths/unreserved_bandwidth/state/unreserved_bandwidth (oc-types:ieeefloat32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unreserved_bandwidth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unreserved_bandwidth() directly.

    YANG Description: The unreserved bandwidth for at priority level P, where P is
equal to the priority of the current list entry. The reservable
bandwidth at priority P is equal to the sum of the reservable
bandwidth at all levels 0..P.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=bitarray, restriction_dict={'length': [u'32']}), is_leaf=True, yang_name="unreserved-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unreserved_bandwidth must be of a type compatible with oc-types:ieeefloat32""",
          'defined-type': "oc-types:ieeefloat32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=bitarray, restriction_dict={'length': [u'32']}), is_leaf=True, yang_name="unreserved-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)""",
        })

    self.__unreserved_bandwidth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unreserved_bandwidth(self):
    self.__unreserved_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=bitarray, restriction_dict={'length': [u'32']}), is_leaf=True, yang_name="unreserved-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)

  priority = __builtin__.property(_get_priority)
  unreserved_bandwidth = __builtin__.property(_get_unreserved_bandwidth)


  _pyangbind_elements = {'priority': priority, 'unreserved_bandwidth': unreserved_bandwidth, }


