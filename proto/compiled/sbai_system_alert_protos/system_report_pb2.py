# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sbai_system_alert_protos/system_report.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sbai_system_alert_protos import system_alert_pb2 as sbai__system__alert__protos_dot_system__alert__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sbai_system_alert_protos/system_report.proto',
  package='sbai_system_alert_protos',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,sbai_system_alert_protos/system_report.proto\x12\x18sbai_system_alert_protos\x1a+sbai_system_alert_protos/system_alert.proto\"\x95\x02\n\x0cSystemReport\x12:\n\x0binfo_alerts\x18\x01 \x03(\x0b\x32%.sbai_system_alert_protos.SystemAlert\x12=\n\x0ewarning_alerts\x18\x02 \x03(\x0b\x32%.sbai_system_alert_protos.SystemAlert\x12;\n\x0c\x65rror_alerts\x18\x03 \x03(\x0b\x32%.sbai_system_alert_protos.SystemAlert\x12;\n\x0c\x66\x61tal_alerts\x18\x04 \x03(\x0b\x32%.sbai_system_alert_protos.SystemAlert\x12\x10\n\x08robot_id\x18\x05 \x01(\tb\x06proto3'
  ,
  dependencies=[sbai__system__alert__protos_dot_system__alert__pb2.DESCRIPTOR,])




_SYSTEMREPORT = _descriptor.Descriptor(
  name='SystemReport',
  full_name='sbai_system_alert_protos.SystemReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='info_alerts', full_name='sbai_system_alert_protos.SystemReport.info_alerts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='warning_alerts', full_name='sbai_system_alert_protos.SystemReport.warning_alerts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_alerts', full_name='sbai_system_alert_protos.SystemReport.error_alerts', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fatal_alerts', full_name='sbai_system_alert_protos.SystemReport.fatal_alerts', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='robot_id', full_name='sbai_system_alert_protos.SystemReport.robot_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=120,
  serialized_end=397,
)

_SYSTEMREPORT.fields_by_name['info_alerts'].message_type = sbai__system__alert__protos_dot_system__alert__pb2._SYSTEMALERT
_SYSTEMREPORT.fields_by_name['warning_alerts'].message_type = sbai__system__alert__protos_dot_system__alert__pb2._SYSTEMALERT
_SYSTEMREPORT.fields_by_name['error_alerts'].message_type = sbai__system__alert__protos_dot_system__alert__pb2._SYSTEMALERT
_SYSTEMREPORT.fields_by_name['fatal_alerts'].message_type = sbai__system__alert__protos_dot_system__alert__pb2._SYSTEMALERT
DESCRIPTOR.message_types_by_name['SystemReport'] = _SYSTEMREPORT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SystemReport = _reflection.GeneratedProtocolMessageType('SystemReport', (_message.Message,), {
  'DESCRIPTOR' : _SYSTEMREPORT,
  '__module__' : 'sbai_system_alert_protos.system_report_pb2'
  # @@protoc_insertion_point(class_scope:sbai_system_alert_protos.SystemReport)
  })
_sym_db.RegisterMessage(SystemReport)


# @@protoc_insertion_point(module_scope)
