# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sbai_std_protos/header.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sbai_builtin_protos import time_pb2 as sbai__builtin__protos_dot_time__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sbai_std_protos/header.proto',
  package='sbai_std_protos',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1csbai_std_protos/header.proto\x12\x0fsbai_std_protos\x1a\x1esbai_builtin_protos/time.proto\"D\n\x06Header\x12(\n\x05stamp\x18\x01 \x01(\x0b\x32\x19.sbai_builtin_protos.Time\x12\x10\n\x08\x66rame_id\x18\x02 \x01(\tb\x06proto3'
  ,
  dependencies=[sbai__builtin__protos_dot_time__pb2.DESCRIPTOR,])




_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='sbai_std_protos.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='stamp', full_name='sbai_std_protos.Header.stamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frame_id', full_name='sbai_std_protos.Header.frame_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=81,
  serialized_end=149,
)

_HEADER.fields_by_name['stamp'].message_type = sbai__builtin__protos_dot_time__pb2._TIME
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
  'DESCRIPTOR' : _HEADER,
  '__module__' : 'sbai_std_protos.header_pb2'
  # @@protoc_insertion_point(class_scope:sbai_std_protos.Header)
  })
_sym_db.RegisterMessage(Header)


# @@protoc_insertion_point(module_scope)