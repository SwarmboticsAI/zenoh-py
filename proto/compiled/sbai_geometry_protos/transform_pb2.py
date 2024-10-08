# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sbai_geometry_protos/transform.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sbai_geometry_protos import quaternion_pb2 as sbai__geometry__protos_dot_quaternion__pb2
from sbai_geometry_protos import vector3_pb2 as sbai__geometry__protos_dot_vector3__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sbai_geometry_protos/transform.proto',
  package='sbai_geometry_protos',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$sbai_geometry_protos/transform.proto\x12\x14sbai_geometry_protos\x1a%sbai_geometry_protos/quaternion.proto\x1a\"sbai_geometry_protos/vector3.proto\"s\n\tTransform\x12\x32\n\x0btranslation\x18\x01 \x01(\x0b\x32\x1d.sbai_geometry_protos.Vector3\x12\x32\n\x08rotation\x18\x02 \x01(\x0b\x32 .sbai_geometry_protos.Quaternionb\x06proto3'
  ,
  dependencies=[sbai__geometry__protos_dot_quaternion__pb2.DESCRIPTOR,sbai__geometry__protos_dot_vector3__pb2.DESCRIPTOR,])




_TRANSFORM = _descriptor.Descriptor(
  name='Transform',
  full_name='sbai_geometry_protos.Transform',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='translation', full_name='sbai_geometry_protos.Transform.translation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rotation', full_name='sbai_geometry_protos.Transform.rotation', index=1,
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
  serialized_start=137,
  serialized_end=252,
)

_TRANSFORM.fields_by_name['translation'].message_type = sbai__geometry__protos_dot_vector3__pb2._VECTOR3
_TRANSFORM.fields_by_name['rotation'].message_type = sbai__geometry__protos_dot_quaternion__pb2._QUATERNION
DESCRIPTOR.message_types_by_name['Transform'] = _TRANSFORM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Transform = _reflection.GeneratedProtocolMessageType('Transform', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORM,
  '__module__' : 'sbai_geometry_protos.transform_pb2'
  # @@protoc_insertion_point(class_scope:sbai_geometry_protos.Transform)
  })
_sym_db.RegisterMessage(Transform)


# @@protoc_insertion_point(module_scope)
