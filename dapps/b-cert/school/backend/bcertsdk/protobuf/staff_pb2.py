# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/staff.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf/staff.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14protobuf/staff.proto\"\xcf\x01\n\x05Staff\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12\x14\n\x0c\x61tt_staff_id\x18\x02 \x01(\t\x12\x10\n\x08\x61tt_name\x18\x03 \x01(\t\x12\x11\n\tatt_email\x18\x04 \x01(\t\x12\x11\n\tatt_phone\x18\x05 \x01(\t\x12\x13\n\x0b\x61tt_address\x18\x06 \x01(\t\x12\x12\n\natt_status\x18\x07 \x01(\t\x12\x16\n\x0e\x61tt_public_key\x18\x08 \x01(\t\x12$\n\x1c\x66or_university_university_id\x18\t \x01(\t\")\n\x0eStaffContainer\x12\x17\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x06.Staffb\x06proto3')
)




_STAFF = _descriptor.Descriptor(
  name='Staff',
  full_name='Staff',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Staff.timestamp', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='att_staff_id', full_name='Staff.att_staff_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='att_name', full_name='Staff.att_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='att_email', full_name='Staff.att_email', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='att_phone', full_name='Staff.att_phone', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='att_address', full_name='Staff.att_address', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='att_status', full_name='Staff.att_status', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='att_public_key', full_name='Staff.att_public_key', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='for_university_university_id', full_name='Staff.for_university_university_id', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=25,
  serialized_end=232,
)


_STAFFCONTAINER = _descriptor.Descriptor(
  name='StaffContainer',
  full_name='StaffContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='StaffContainer.entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=234,
  serialized_end=275,
)

_STAFFCONTAINER.fields_by_name['entries'].message_type = _STAFF
DESCRIPTOR.message_types_by_name['Staff'] = _STAFF
DESCRIPTOR.message_types_by_name['StaffContainer'] = _STAFFCONTAINER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Staff = _reflection.GeneratedProtocolMessageType('Staff', (_message.Message,), {
  'DESCRIPTOR' : _STAFF,
  '__module__' : 'protobuf.staff_pb2'
  # @@protoc_insertion_point(class_scope:Staff)
  })
_sym_db.RegisterMessage(Staff)

StaffContainer = _reflection.GeneratedProtocolMessageType('StaffContainer', (_message.Message,), {
  'DESCRIPTOR' : _STAFFCONTAINER,
  '__module__' : 'protobuf.staff_pb2'
  # @@protoc_insertion_point(class_scope:StaffContainer)
  })
_sym_db.RegisterMessage(StaffContainer)


# @@protoc_insertion_point(module_scope)
