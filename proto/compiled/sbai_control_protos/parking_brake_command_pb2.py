# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sbai_control_protos/parking_brake_command.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sbai_control_protos/parking_brake_command.proto',
  package='sbai_control_protos',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n/sbai_control_protos/parking_brake_command.proto\x12\x13sbai_control_protos\x1a\x1egoogle/protobuf/wrappers.proto\"N\n\x13ParkingBrakeCommand\x12\x37\n\x13should_engage_brake\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_PARKINGBRAKECOMMAND = _descriptor.Descriptor(
  name='ParkingBrakeCommand',
  full_name='sbai_control_protos.ParkingBrakeCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='should_engage_brake', full_name='sbai_control_protos.ParkingBrakeCommand.should_engage_brake', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=104,
  serialized_end=182,
)

_PARKINGBRAKECOMMAND.fields_by_name['should_engage_brake'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
DESCRIPTOR.message_types_by_name['ParkingBrakeCommand'] = _PARKINGBRAKECOMMAND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ParkingBrakeCommand = _reflection.GeneratedProtocolMessageType('ParkingBrakeCommand', (_message.Message,), {
  'DESCRIPTOR' : _PARKINGBRAKECOMMAND,
  '__module__' : 'sbai_control_protos.parking_brake_command_pb2'
  # @@protoc_insertion_point(class_scope:sbai_control_protos.ParkingBrakeCommand)
  })
_sym_db.RegisterMessage(ParkingBrakeCommand)


# @@protoc_insertion_point(module_scope)
