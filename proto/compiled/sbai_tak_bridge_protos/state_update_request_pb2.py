# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sbai_tak_bridge_protos/state_update_request.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sbai_cortex_protos import cortex_state_update_pb2 as sbai__cortex__protos_dot_cortex__state__update__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sbai_tak_bridge_protos/state_update_request.proto',
  package='sbai_tak_bridge_protos',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n1sbai_tak_bridge_protos/state_update_request.proto\x12\x16sbai_tak_bridge_protos\x1a,sbai_cortex_protos/cortex_state_update.proto\"N\n\x12StateUpdateRequest\x12\x38\n\x0frequested_state\x18\x01 \x01(\x0e\x32\x1f.sbai_cortex_protos.CortexStateb\x06proto3'
  ,
  dependencies=[sbai__cortex__protos_dot_cortex__state__update__pb2.DESCRIPTOR,])




_STATEUPDATEREQUEST = _descriptor.Descriptor(
  name='StateUpdateRequest',
  full_name='sbai_tak_bridge_protos.StateUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='requested_state', full_name='sbai_tak_bridge_protos.StateUpdateRequest.requested_state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=123,
  serialized_end=201,
)

_STATEUPDATEREQUEST.fields_by_name['requested_state'].enum_type = sbai__cortex__protos_dot_cortex__state__update__pb2._CORTEXSTATE
DESCRIPTOR.message_types_by_name['StateUpdateRequest'] = _STATEUPDATEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StateUpdateRequest = _reflection.GeneratedProtocolMessageType('StateUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATEUPDATEREQUEST,
  '__module__' : 'sbai_tak_bridge_protos.state_update_request_pb2'
  # @@protoc_insertion_point(class_scope:sbai_tak_bridge_protos.StateUpdateRequest)
  })
_sym_db.RegisterMessage(StateUpdateRequest)


# @@protoc_insertion_point(module_scope)