# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: image_search.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12image_search.proto\x12\x0cimage_search\" \n\rSearchRequest\x12\x0f\n\x07keyword\x18\x01 \x01(\t\"#\n\rImageResponse\x12\x12\n\nimage_data\x18\x01 \x01(\x0c\"\r\n\x0bPingRequest\"\x1f\n\x0cPingResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\x99\x01\n\x0bImageSearch\x12I\n\x0bSearchImage\x12\x1b.image_search.SearchRequest\x1a\x1b.image_search.ImageResponse\"\x00\x12?\n\x04Ping\x12\x19.image_search.PingRequest\x1a\x1a.image_search.PingResponse\"\x00\x42\x1fZ\x1dimage_search_client/generatedb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'image_search_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\035image_search_client/generated'
  _globals['_SEARCHREQUEST']._serialized_start=36
  _globals['_SEARCHREQUEST']._serialized_end=68
  _globals['_IMAGERESPONSE']._serialized_start=70
  _globals['_IMAGERESPONSE']._serialized_end=105
  _globals['_PINGREQUEST']._serialized_start=107
  _globals['_PINGREQUEST']._serialized_end=120
  _globals['_PINGRESPONSE']._serialized_start=122
  _globals['_PINGRESPONSE']._serialized_end=153
  _globals['_IMAGESEARCH']._serialized_start=156
  _globals['_IMAGESEARCH']._serialized_end=309
# @@protoc_insertion_point(module_scope)