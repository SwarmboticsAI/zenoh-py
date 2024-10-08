# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sbai_geographic_protos/geo_pose_stamped.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sbai_geographic_protos import geo_pose_pb2 as sbai__geographic__protos_dot_geo__pose__pb2
from sbai_std_protos import header_pb2 as sbai__std__protos_dot_header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sbai_geographic_protos/geo_pose_stamped.proto',
  package='sbai_geographic_protos',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n-sbai_geographic_protos/geo_pose_stamped.proto\x12\x16sbai_geographic_protos\x1a%sbai_geographic_protos/geo_pose.proto\x1a\x1csbai_std_protos/header.proto\"h\n\x0eGeoPoseStamped\x12\'\n\x06header\x18\x01 \x01(\x0b\x32\x17.sbai_std_protos.Header\x12-\n\x04pose\x18\x02 \x01(\x0b\x32\x1f.sbai_geographic_protos.GeoPoseb\x06proto3'
  ,
  dependencies=[sbai__geographic__protos_dot_geo__pose__pb2.DESCRIPTOR,sbai__std__protos_dot_header__pb2.DESCRIPTOR,])




_GEOPOSESTAMPED = _descriptor.Descriptor(
  name='GeoPoseStamped',
  full_name='sbai_geographic_protos.GeoPoseStamped',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='sbai_geographic_protos.GeoPoseStamped.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pose', full_name='sbai_geographic_protos.GeoPoseStamped.pose', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=142,
  serialized_end=246,
)

_GEOPOSESTAMPED.fields_by_name['header'].message_type = sbai__std__protos_dot_header__pb2._HEADER
_GEOPOSESTAMPED.fields_by_name['pose'].message_type = sbai__geographic__protos_dot_geo__pose__pb2._GEOPOSE
DESCRIPTOR.message_types_by_name['GeoPoseStamped'] = _GEOPOSESTAMPED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GeoPoseStamped = _reflection.GeneratedProtocolMessageType('GeoPoseStamped', (_message.Message,), {
  'DESCRIPTOR' : _GEOPOSESTAMPED,
  '__module__' : 'sbai_geographic_protos.geo_pose_stamped_pb2'
  # @@protoc_insertion_point(class_scope:sbai_geographic_protos.GeoPoseStamped)
  })
_sym_db.RegisterMessage(GeoPoseStamped)


# @@protoc_insertion_point(module_scope)
