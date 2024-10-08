# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sbai_task_assignment_protos/winning_agent.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sbai_task_assignment_protos/winning_agent.proto',
  package='sbai_task_assignment_protos',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n/sbai_task_assignment_protos/winning_agent.proto\x12\x1bsbai_task_assignment_protos\"1\n\x0cWinningAgent\x12\x0f\n\x07task_id\x18\x02 \x01(\x05\x12\x10\n\x08robot_id\x18\x01 \x01(\tb\x06proto3'
)




_WINNINGAGENT = _descriptor.Descriptor(
  name='WinningAgent',
  full_name='sbai_task_assignment_protos.WinningAgent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='sbai_task_assignment_protos.WinningAgent.task_id', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='robot_id', full_name='sbai_task_assignment_protos.WinningAgent.robot_id', index=1,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=80,
  serialized_end=129,
)

DESCRIPTOR.message_types_by_name['WinningAgent'] = _WINNINGAGENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WinningAgent = _reflection.GeneratedProtocolMessageType('WinningAgent', (_message.Message,), {
  'DESCRIPTOR' : _WINNINGAGENT,
  '__module__' : 'sbai_task_assignment_protos.winning_agent_pb2'
  # @@protoc_insertion_point(class_scope:sbai_task_assignment_protos.WinningAgent)
  })
_sym_db.RegisterMessage(WinningAgent)


# @@protoc_insertion_point(module_scope)
