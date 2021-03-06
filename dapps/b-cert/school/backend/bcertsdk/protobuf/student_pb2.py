# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/student.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf/student.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16protobuf/student.proto\"\x81\x02\n\x07Student\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12\x16\n\x0e\x61tt_student_id\x18\x02 \x01(\t\x12\x10\n\x08\x61tt_name\x18\x03 \x01(\t\x12\x11\n\tatt_phone\x18\x04 \x01(\t\x12\x11\n\tatt_email\x18\x05 \x01(\t\x12\x13\n\x0b\x61tt_address\x18\x06 \x01(\t\x12\x16\n\x0e\x61tt_public_key\x18\x07 \x01(\t\x12!\n\x19\x66or_certificate_certi_ids\x18\x08 \x03(\t\x12\x1d\n\x15\x66or_result_result_ids\x18\t \x03(\t\x12$\n\x1c\x66or_university_university_id\x18\n \x01(\t\"-\n\x10StudentContainer\x12\x19\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x08.Studentb\x06proto3')
)




_STUDENT = _descriptor.Descriptor(
  name='Student',
  full_name='Student',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Student.timestamp', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='att_student_id', full_name='Student.att_student_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='att_name', full_name='Student.att_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='att_phone', full_name='Student.att_phone', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='att_email', full_name='Student.att_email', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='att_address', full_name='Student.att_address', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='att_public_key', full_name='Student.att_public_key', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='for_certificate_certi_ids', full_name='Student.for_certificate_certi_ids', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='for_result_result_ids', full_name='Student.for_result_result_ids', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='for_university_university_id', full_name='Student.for_university_university_id', index=9,
      number=10, type=9, cpp_type=9, label=1,
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
  serialized_start=27,
  serialized_end=284,
)


_STUDENTCONTAINER = _descriptor.Descriptor(
  name='StudentContainer',
  full_name='StudentContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='StudentContainer.entries', index=0,
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
  serialized_start=286,
  serialized_end=331,
)

_STUDENTCONTAINER.fields_by_name['entries'].message_type = _STUDENT
DESCRIPTOR.message_types_by_name['Student'] = _STUDENT
DESCRIPTOR.message_types_by_name['StudentContainer'] = _STUDENTCONTAINER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Student = _reflection.GeneratedProtocolMessageType('Student', (_message.Message,), {
  'DESCRIPTOR' : _STUDENT,
  '__module__' : 'protobuf.student_pb2'
  # @@protoc_insertion_point(class_scope:Student)
  })
_sym_db.RegisterMessage(Student)

StudentContainer = _reflection.GeneratedProtocolMessageType('StudentContainer', (_message.Message,), {
  'DESCRIPTOR' : _STUDENTCONTAINER,
  '__module__' : 'protobuf.student_pb2'
  # @@protoc_insertion_point(class_scope:StudentContainer)
  })
_sym_db.RegisterMessage(StudentContainer)


# @@protoc_insertion_point(module_scope)
