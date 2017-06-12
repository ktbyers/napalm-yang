
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
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/routed-vlan/ipv4/neighbors/neighbor/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for each configured IPv4
address on the interface
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__ip','__link_layer_address',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ip = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': u'[0-9\\.]*'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='inet:ipv4-address-no-zone', is_config=True)
    self.__link_layer_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}), is_leaf=True, yang_name="link-layer-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='yang:phys-address', is_config=True)

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
      return [u'interfaces', u'interface', u'routed-vlan', u'ipv4', u'neighbors', u'neighbor', u'config']

  def _get_ip(self):
    """
    Getter method for ip, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/neighbors/neighbor/config/ip (inet:ipv4-address-no-zone)

    YANG Description: The IPv4 address of the neighbor node.
    """
    return self.__ip
      
  def _set_ip(self, v, load=False):
    """
    Setter method for ip, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/neighbors/neighbor/config/ip (inet:ipv4-address-no-zone)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip() directly.

    YANG Description: The IPv4 address of the neighbor node.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': u'[0-9\\.]*'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='inet:ipv4-address-no-zone', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip must be of a type compatible with inet:ipv4-address-no-zone""",
          'defined-type': "inet:ipv4-address-no-zone",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': u'[0-9\\.]*'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='inet:ipv4-address-no-zone', is_config=True)""",
        })

    self.__ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip(self):
    self.__ip = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': u'[0-9\\.]*'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='inet:ipv4-address-no-zone', is_config=True)


  def _get_link_layer_address(self):
    """
    Getter method for link_layer_address, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/neighbors/neighbor/config/link_layer_address (yang:phys-address)

    YANG Description: The link-layer address of the neighbor node.
    """
    return self.__link_layer_address
      
  def _set_link_layer_address(self, v, load=False):
    """
    Setter method for link_layer_address, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/neighbors/neighbor/config/link_layer_address (yang:phys-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_layer_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_layer_address() directly.

    YANG Description: The link-layer address of the neighbor node.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}), is_leaf=True, yang_name="link-layer-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='yang:phys-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_layer_address must be of a type compatible with yang:phys-address""",
          'defined-type': "yang:phys-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}), is_leaf=True, yang_name="link-layer-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='yang:phys-address', is_config=True)""",
        })

    self.__link_layer_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_layer_address(self):
    self.__link_layer_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}), is_leaf=True, yang_name="link-layer-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='yang:phys-address', is_config=True)

  ip = __builtin__.property(_get_ip, _set_ip)
  link_layer_address = __builtin__.property(_get_link_layer_address, _set_link_layer_address)


  _pyangbind_elements = {'ip': ip, 'link_layer_address': link_layer_address, }


