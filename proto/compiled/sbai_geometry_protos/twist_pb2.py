# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sbai_geometry_protos/twist.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sbai_geometry_protos import vector3_pb2 as sbai__geometry__protos_dot_vector3__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sbai_geometry_protos/twist.proto',
  package='sbai_geometry_protos',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n sbai_geometry_protos/twist.proto\x12\x14sbai_geometry_protos\x1a\"sbai_geometry_protos/vector3.proto\"f\n\x05Twist\x12-\n\x06linear\x18\x01 \x01(\x0b\x32\x1d.sbai_geometry_protos.Vector3\x12.\n\x07\x61ngular\x18\x02 \x01(\x0b\x32\x1d.sbai_geometry_protos.Vector3b\x06proto3'
  ,
  dependencies=[sbai__geometry__protos_dot_vector3__pb2.DESCRIPTOR,])




_TWIST = _descriptor.Descriptor(
  name='Twist',
  full_name='sbai_geometry_protos.Twist',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='linear', full_name='sbai_geometry_protos.Twist.linear', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='angular', full_name='sbai_geometry_protos.Twist.angular', index=1,
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
  serialized_start=94,
  serialized_end=196,
)

_TWIST.fields_by_name['linear'].message_type = sbai__geometry__protos_dot_vector3__pb2._VECTOR3
_TWIST.fields_by_name['angular'].message_type = sbai__geometry__protos_dot_vector3__pb2._VECTOR3
DESCRIPTOR.message_types_by_name['Twist'] = _TWIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Twist = _reflection.GeneratedProtocolMessageType('Twist', (_message.Message,), {
  'DESCRIPTOR' : _TWIST,
  '__module__' : 'sbai_geometry_protos.twist_pb2'
  # @@protoc_insertion_point(class_scope:sbai_geometry_protos.Twist)
  })
_sym_db.RegisterMessage(Twist)


# @@protoc_insertion_point(module_scope)