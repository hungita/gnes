# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/gnes.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/gnes.proto',
  package='gnes',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x10proto/gnes.proto\x12\x04gnes\">\n\x05\x41rray\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\x0c\x12\x11\n\x05shape\x18\x02 \x03(\rB\x02\x10\x01\x12\x14\n\x05\x64type\x18\x03 \x02(\t:\x05\x66loat\"(\n\tArrayList\x12\x1b\n\x06\x61rrays\x18\x01 \x03(\x0b\x32\x0b.gnes.Array\"\xd2\x01\n\x05\x43hunk\x12\x0e\n\x06\x64oc_id\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x02(\r\x12\x19\n\nis_encoded\x18\x03 \x02(\x08:\x05\x66\x61lse\x12\x0c\n\x04text\x18\x04 \x01(\t\x12\x19\n\x04\x62lob\x18\x05 \x01(\x0b\x32\x0b.gnes.Array\x12\x1b\n\x06\x65ncode\x18\x06 \x01(\x0b\x32\x0b.gnes.Array\x12+\n\x0b\x63oordinates\x18\x07 \x03(\x0b\x32\x16.gnes.Chunk.Coordinate\x1a\x1b\n\nCoordinate\x12\r\n\x01x\x18\x01 \x03(\rB\x02\x10\x01\"\x84\x01\n\x08\x44ocument\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x19\n\x04\x62lob\x18\x04 \x01(\x0b\x32\x0b.gnes.Array\x12\x18\n\tis_parsed\x18\x05 \x02(\x08:\x05\x66\x61lse\x12\x1b\n\x06\x63hunks\x18\x06 \x03(\x0b\x32\x0b.gnes.Chunk\"z\n\x05Query\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x19\n\x04\x62lob\x18\x02 \x01(\x0b\x32\x0b.gnes.Array\x12\x18\n\tis_parsed\x18\x03 \x02(\x08:\x05\x66\x61lse\x12\x1b\n\x06\x63hunks\x18\x04 \x03(\x0b\x32\x0b.gnes.Chunk\x12\x11\n\x05top_k\x18\x05 \x01(\r:\x02\x31\x30\"R\n\rSearchRequest\x12\x13\n\x0b_request_id\x18\x01 \x02(\t\x12\x1a\n\x05query\x18\x02 \x02(\x0b\x32\x0b.gnes.Query\x12\x10\n\x08time_out\x18\x03 \x01(\r\"p\n\x0cIndexRequest\x12\x13\n\x0b_request_id\x18\x01 \x02(\t\x12\x1c\n\x04\x64ocs\x18\x02 \x03(\x0b\x32\x0e.gnes.Document\x12\x10\n\x08time_out\x18\x03 \x01(\r\x12\x1b\n\x0cupdate_model\x18\x04 \x02(\x08:\x05\x66\x61lse\"u\n\x0eSearchResponse\x12,\n\x07results\x18\x01 \x03(\x0b\x32\x1b.gnes.SearchResponse.Result\x12\x0c\n\x04size\x18\x02 \x02(\r\x1a\'\n\x06Result\x12\x0e\n\x06\x64oc_id\x18\x01 \x02(\t\x12\r\n\x05score\x18\x02 \x02(\x02\"\xd2\x01\n\x07Message\x12\x0e\n\x06msg_id\x18\x01 \x01(\t\x12\x10\n\x08msg_type\x18\x02 \x02(\t\x12\r\n\x05route\x18\x03 \x02(\t\x12\x12\n\x07part_id\x18\x04 \x02(\r:\x01\x30\x12\x13\n\x08num_part\x18\x05 \x02(\r:\x01\x31\x12\'\n\x04mode\x18\x06 \x02(\x0e\x32\x12.gnes.Message.Mode:\x05QUERY\x12\x1b\n\x06\x63hunks\x18\x07 \x03(\x0b\x32\x0b.gnes.Chunk\"\'\n\x04Mode\x12\t\n\x05QUERY\x10\x00\x12\t\n\x05INDEX\x10\x01\x12\t\n\x05TRAIN\x10\x02')
)



_MESSAGE_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='gnes.Message.Mode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='QUERY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDEX', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRAIN', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1093,
  serialized_end=1132,
)
_sym_db.RegisterEnumDescriptor(_MESSAGE_MODE)


_ARRAY = _descriptor.Descriptor(
  name='Array',
  full_name='gnes.Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='gnes.Array.data', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape', full_name='gnes.Array.shape', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='gnes.Array.dtype', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=_b("float").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=88,
)


_ARRAYLIST = _descriptor.Descriptor(
  name='ArrayList',
  full_name='gnes.ArrayList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='arrays', full_name='gnes.ArrayList.arrays', index=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=130,
)


_CHUNK_COORDINATE = _descriptor.Descriptor(
  name='Coordinate',
  full_name='gnes.Chunk.Coordinate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='gnes.Chunk.Coordinate.x', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=316,
  serialized_end=343,
)

_CHUNK = _descriptor.Descriptor(
  name='Chunk',
  full_name='gnes.Chunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='doc_id', full_name='gnes.Chunk.doc_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='gnes.Chunk.offset', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_encoded', full_name='gnes.Chunk.is_encoded', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='gnes.Chunk.text', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blob', full_name='gnes.Chunk.blob', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encode', full_name='gnes.Chunk.encode', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coordinates', full_name='gnes.Chunk.coordinates', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CHUNK_COORDINATE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=343,
)


_DOCUMENT = _descriptor.Descriptor(
  name='Document',
  full_name='gnes.Document',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gnes.Document.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='gnes.Document.uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='gnes.Document.text', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blob', full_name='gnes.Document.blob', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_parsed', full_name='gnes.Document.is_parsed', index=4,
      number=5, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunks', full_name='gnes.Document.chunks', index=5,
      number=6, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=346,
  serialized_end=478,
)


_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='gnes.Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='gnes.Query.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blob', full_name='gnes.Query.blob', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_parsed', full_name='gnes.Query.is_parsed', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunks', full_name='gnes.Query.chunks', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='top_k', full_name='gnes.Query.top_k', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=10,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=480,
  serialized_end=602,
)


_SEARCHREQUEST = _descriptor.Descriptor(
  name='SearchRequest',
  full_name='gnes.SearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='_request_id', full_name='gnes.SearchRequest._request_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query', full_name='gnes.SearchRequest.query', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_out', full_name='gnes.SearchRequest.time_out', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=604,
  serialized_end=686,
)


_INDEXREQUEST = _descriptor.Descriptor(
  name='IndexRequest',
  full_name='gnes.IndexRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='_request_id', full_name='gnes.IndexRequest._request_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='docs', full_name='gnes.IndexRequest.docs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_out', full_name='gnes.IndexRequest.time_out', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_model', full_name='gnes.IndexRequest.update_model', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=688,
  serialized_end=800,
)


_SEARCHRESPONSE_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='gnes.SearchResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='doc_id', full_name='gnes.SearchResponse.Result.doc_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='gnes.SearchResponse.Result.score', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=880,
  serialized_end=919,
)

_SEARCHRESPONSE = _descriptor.Descriptor(
  name='SearchResponse',
  full_name='gnes.SearchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='gnes.SearchResponse.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='gnes.SearchResponse.size', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SEARCHRESPONSE_RESULT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=802,
  serialized_end=919,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='gnes.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_id', full_name='gnes.Message.msg_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg_type', full_name='gnes.Message.msg_type', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='route', full_name='gnes.Message.route', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='part_id', full_name='gnes.Message.part_id', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_part', full_name='gnes.Message.num_part', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='gnes.Message.mode', index=5,
      number=6, type=14, cpp_type=8, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunks', full_name='gnes.Message.chunks', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MESSAGE_MODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=922,
  serialized_end=1132,
)

_ARRAYLIST.fields_by_name['arrays'].message_type = _ARRAY
_CHUNK_COORDINATE.containing_type = _CHUNK
_CHUNK.fields_by_name['blob'].message_type = _ARRAY
_CHUNK.fields_by_name['encode'].message_type = _ARRAY
_CHUNK.fields_by_name['coordinates'].message_type = _CHUNK_COORDINATE
_DOCUMENT.fields_by_name['blob'].message_type = _ARRAY
_DOCUMENT.fields_by_name['chunks'].message_type = _CHUNK
_QUERY.fields_by_name['blob'].message_type = _ARRAY
_QUERY.fields_by_name['chunks'].message_type = _CHUNK
_SEARCHREQUEST.fields_by_name['query'].message_type = _QUERY
_INDEXREQUEST.fields_by_name['docs'].message_type = _DOCUMENT
_SEARCHRESPONSE_RESULT.containing_type = _SEARCHRESPONSE
_SEARCHRESPONSE.fields_by_name['results'].message_type = _SEARCHRESPONSE_RESULT
_MESSAGE.fields_by_name['mode'].enum_type = _MESSAGE_MODE
_MESSAGE.fields_by_name['chunks'].message_type = _CHUNK
_MESSAGE_MODE.containing_type = _MESSAGE
DESCRIPTOR.message_types_by_name['Array'] = _ARRAY
DESCRIPTOR.message_types_by_name['ArrayList'] = _ARRAYLIST
DESCRIPTOR.message_types_by_name['Chunk'] = _CHUNK
DESCRIPTOR.message_types_by_name['Document'] = _DOCUMENT
DESCRIPTOR.message_types_by_name['Query'] = _QUERY
DESCRIPTOR.message_types_by_name['SearchRequest'] = _SEARCHREQUEST
DESCRIPTOR.message_types_by_name['IndexRequest'] = _INDEXREQUEST
DESCRIPTOR.message_types_by_name['SearchResponse'] = _SEARCHRESPONSE
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Array = _reflection.GeneratedProtocolMessageType('Array', (_message.Message,), dict(
  DESCRIPTOR = _ARRAY,
  __module__ = 'proto.gnes_pb2'
  # @@protoc_insertion_point(class_scope:gnes.Array)
  ))
_sym_db.RegisterMessage(Array)

ArrayList = _reflection.GeneratedProtocolMessageType('ArrayList', (_message.Message,), dict(
  DESCRIPTOR = _ARRAYLIST,
  __module__ = 'proto.gnes_pb2'
  # @@protoc_insertion_point(class_scope:gnes.ArrayList)
  ))
_sym_db.RegisterMessage(ArrayList)

Chunk = _reflection.GeneratedProtocolMessageType('Chunk', (_message.Message,), dict(

  Coordinate = _reflection.GeneratedProtocolMessageType('Coordinate', (_message.Message,), dict(
    DESCRIPTOR = _CHUNK_COORDINATE,
    __module__ = 'proto.gnes_pb2'
    # @@protoc_insertion_point(class_scope:gnes.Chunk.Coordinate)
    ))
  ,
  DESCRIPTOR = _CHUNK,
  __module__ = 'proto.gnes_pb2'
  # @@protoc_insertion_point(class_scope:gnes.Chunk)
  ))
_sym_db.RegisterMessage(Chunk)
_sym_db.RegisterMessage(Chunk.Coordinate)

Document = _reflection.GeneratedProtocolMessageType('Document', (_message.Message,), dict(
  DESCRIPTOR = _DOCUMENT,
  __module__ = 'proto.gnes_pb2'
  # @@protoc_insertion_point(class_scope:gnes.Document)
  ))
_sym_db.RegisterMessage(Document)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), dict(
  DESCRIPTOR = _QUERY,
  __module__ = 'proto.gnes_pb2'
  # @@protoc_insertion_point(class_scope:gnes.Query)
  ))
_sym_db.RegisterMessage(Query)

SearchRequest = _reflection.GeneratedProtocolMessageType('SearchRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHREQUEST,
  __module__ = 'proto.gnes_pb2'
  # @@protoc_insertion_point(class_scope:gnes.SearchRequest)
  ))
_sym_db.RegisterMessage(SearchRequest)

IndexRequest = _reflection.GeneratedProtocolMessageType('IndexRequest', (_message.Message,), dict(
  DESCRIPTOR = _INDEXREQUEST,
  __module__ = 'proto.gnes_pb2'
  # @@protoc_insertion_point(class_scope:gnes.IndexRequest)
  ))
_sym_db.RegisterMessage(IndexRequest)

SearchResponse = _reflection.GeneratedProtocolMessageType('SearchResponse', (_message.Message,), dict(

  Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
    DESCRIPTOR = _SEARCHRESPONSE_RESULT,
    __module__ = 'proto.gnes_pb2'
    # @@protoc_insertion_point(class_scope:gnes.SearchResponse.Result)
    ))
  ,
  DESCRIPTOR = _SEARCHRESPONSE,
  __module__ = 'proto.gnes_pb2'
  # @@protoc_insertion_point(class_scope:gnes.SearchResponse)
  ))
_sym_db.RegisterMessage(SearchResponse)
_sym_db.RegisterMessage(SearchResponse.Result)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'proto.gnes_pb2'
  # @@protoc_insertion_point(class_scope:gnes.Message)
  ))
_sym_db.RegisterMessage(Message)


_ARRAY.fields_by_name['shape']._options = None
_CHUNK_COORDINATE.fields_by_name['x']._options = None
# @@protoc_insertion_point(module_scope)
