# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sbai_geometry_protos/pose_stamped.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sbai_geometry_protos import pose_pb2 as sbai__geometry__protos_dot_pose__pb2
from sbai_std_protos import header_pb2 as sbai__std__protos_dot_header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sbai_geometry_protos/pose_stamped.proto',
  package='sbai_geometry_protos',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'sbai_geometry_protos/pose_stamped.proto\x12\x14sbai_geometry_protos\x1a\x1fsbai_geometry_protos/pose.proto\x1a\x1csbai_std_protos/header.proto\"`\n\x0bPoseStamped\x12\'\n\x06header\x18\x01 \x01(\x0b\x32\x17.sbai_std_protos.Header\x12(\n\x04pose\x18\x02 \x01(\x0b\x32\x1a.sbai_geometry_protos.Poseb\x06proto3'
  ,
  dependencies=[sbai__geometry__protos_dot_pose__pb2.DESCRIPTOR,sbai__std__protos_dot_header__pb2.DESCRIPTOR,])




_POSESTAMPED = _descriptor.Descriptor(
  name='PoseStamped',
  full_name='sbai_geometry_protos.PoseStamped',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='sbai_geometry_protos.PoseStamped.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pose', full_name='sbai_geometry_protos.PoseStamped.pose', index=1,
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
  serialized_start=128,
  serialized_end=224,
)

_POSESTAMPED.fields_by_name['header'].message_type = sbai__std__protos_dot_header__pb2._HEADER
_POSESTAMPED.fields_by_name['pose'].message_type = sbai__geometry__protos_dot_pose__pb2._POSE
DESCRIPTOR.message_types_by_name['PoseStamped'] = _POSESTAMPED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PoseStamped = _reflection.GeneratedProtocolMessageType('PoseStamped', (_message.Message,), {
  'DESCRIPTOR' : _POSESTAMPED,
  '__module__' : 'sbai_geometry_protos.pose_stamped_pb2'
  # @@protoc_insertion_point(class_scope:sbai_geometry_protos.PoseStamped)
  })
_sym_db.RegisterMessage(PoseStamped)


# @@protoc_insertion_point(module_scope)
