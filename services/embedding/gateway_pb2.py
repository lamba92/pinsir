# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gateway.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rgateway.proto\x1a\x0c\x63ommon.proto\"C\n\x1f\x43omparePortraitToGalleryRequest\x12\x10\n\x08portrait\x18\x01 \x01(\t\x12\x0e\n\x06galley\x18\x02 \x03(\t\"C\n\x17\x43omparePortraitsRequest\x12\x10\n\x08portrait\x18\x01 \x01(\t\x12\x16\n\x0eother_portrait\x18\x02 \x01(\t\"D\n\x18\x43omparePortraitsResponse\x12\x10\n\x08portrait\x18\x01 \x01(\t\x12\x16\n\x0eother_portrait\x18\x02 \x01(\t\"$\n\x12\x45laborationRequest\x12\x0e\n\x06images\x18\x01 \x03(\t\"\xb7\x02\n\x13\x45laborationResponse\x12=\n\x08\x65lements\x18\x01 \x03(\x0b\x32+.ElaborationResponse.ImageWithExtractedData\x1a\xe0\x01\n\x16ImageWithExtractedData\x12\x15\n\roriginalImage\x18\x01 \x01(\t\x12O\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x41.ElaborationResponse.ImageWithExtractedData.PortraitWithEmbedding\x1a^\n\x15PortraitWithEmbedding\x12\r\n\x05\x61rray\x18\x01 \x03(\x01\x12\x11\n\tfaceImage\x18\x02 \x01(\t\x12#\n\nannotation\x18\x03 \x01(\x0b\x32\x0f.FaceAnnotation2\xd5\x01\n\x07Gateway\x12\x36\n\telaborate\x12\x13.ElaborationRequest\x1a\x14.ElaborationResponse\x12?\n\x10\x63omparePortraits\x12\x18.ComparePortraitsRequest\x1a\x11.ComparisonResult\x12Q\n\x18\x63omparePortraitToGallery\x12 .ComparePortraitToGalleryRequest\x1a\x13.ComparisonResponseb\x06proto3'
  ,
  dependencies=[common__pb2.DESCRIPTOR,])




_COMPAREPORTRAITTOGALLERYREQUEST = _descriptor.Descriptor(
  name='ComparePortraitToGalleryRequest',
  full_name='ComparePortraitToGalleryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='portrait', full_name='ComparePortraitToGalleryRequest.portrait', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='galley', full_name='ComparePortraitToGalleryRequest.galley', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=31,
  serialized_end=98,
)


_COMPAREPORTRAITSREQUEST = _descriptor.Descriptor(
  name='ComparePortraitsRequest',
  full_name='ComparePortraitsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='portrait', full_name='ComparePortraitsRequest.portrait', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='other_portrait', full_name='ComparePortraitsRequest.other_portrait', index=1,
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
  serialized_start=100,
  serialized_end=167,
)


_COMPAREPORTRAITSRESPONSE = _descriptor.Descriptor(
  name='ComparePortraitsResponse',
  full_name='ComparePortraitsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='portrait', full_name='ComparePortraitsResponse.portrait', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='other_portrait', full_name='ComparePortraitsResponse.other_portrait', index=1,
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
  serialized_start=169,
  serialized_end=237,
)


_ELABORATIONREQUEST = _descriptor.Descriptor(
  name='ElaborationRequest',
  full_name='ElaborationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='images', full_name='ElaborationRequest.images', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=239,
  serialized_end=275,
)


_ELABORATIONRESPONSE_IMAGEWITHEXTRACTEDDATA_PORTRAITWITHEMBEDDING = _descriptor.Descriptor(
  name='PortraitWithEmbedding',
  full_name='ElaborationResponse.ImageWithExtractedData.PortraitWithEmbedding',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='array', full_name='ElaborationResponse.ImageWithExtractedData.PortraitWithEmbedding.array', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='faceImage', full_name='ElaborationResponse.ImageWithExtractedData.PortraitWithEmbedding.faceImage', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='annotation', full_name='ElaborationResponse.ImageWithExtractedData.PortraitWithEmbedding.annotation', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=495,
  serialized_end=589,
)

_ELABORATIONRESPONSE_IMAGEWITHEXTRACTEDDATA = _descriptor.Descriptor(
  name='ImageWithExtractedData',
  full_name='ElaborationResponse.ImageWithExtractedData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='originalImage', full_name='ElaborationResponse.ImageWithExtractedData.originalImage', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='ElaborationResponse.ImageWithExtractedData.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ELABORATIONRESPONSE_IMAGEWITHEXTRACTEDDATA_PORTRAITWITHEMBEDDING, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=365,
  serialized_end=589,
)

_ELABORATIONRESPONSE = _descriptor.Descriptor(
  name='ElaborationResponse',
  full_name='ElaborationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='elements', full_name='ElaborationResponse.elements', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ELABORATIONRESPONSE_IMAGEWITHEXTRACTEDDATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=278,
  serialized_end=589,
)

_ELABORATIONRESPONSE_IMAGEWITHEXTRACTEDDATA_PORTRAITWITHEMBEDDING.fields_by_name['annotation'].message_type = common__pb2._FACEANNOTATION
_ELABORATIONRESPONSE_IMAGEWITHEXTRACTEDDATA_PORTRAITWITHEMBEDDING.containing_type = _ELABORATIONRESPONSE_IMAGEWITHEXTRACTEDDATA
_ELABORATIONRESPONSE_IMAGEWITHEXTRACTEDDATA.fields_by_name['data'].message_type = _ELABORATIONRESPONSE_IMAGEWITHEXTRACTEDDATA_PORTRAITWITHEMBEDDING
_ELABORATIONRESPONSE_IMAGEWITHEXTRACTEDDATA.containing_type = _ELABORATIONRESPONSE
_ELABORATIONRESPONSE.fields_by_name['elements'].message_type = _ELABORATIONRESPONSE_IMAGEWITHEXTRACTEDDATA
DESCRIPTOR.message_types_by_name['ComparePortraitToGalleryRequest'] = _COMPAREPORTRAITTOGALLERYREQUEST
DESCRIPTOR.message_types_by_name['ComparePortraitsRequest'] = _COMPAREPORTRAITSREQUEST
DESCRIPTOR.message_types_by_name['ComparePortraitsResponse'] = _COMPAREPORTRAITSRESPONSE
DESCRIPTOR.message_types_by_name['ElaborationRequest'] = _ELABORATIONREQUEST
DESCRIPTOR.message_types_by_name['ElaborationResponse'] = _ELABORATIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ComparePortraitToGalleryRequest = _reflection.GeneratedProtocolMessageType('ComparePortraitToGalleryRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMPAREPORTRAITTOGALLERYREQUEST,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:ComparePortraitToGalleryRequest)
  })
_sym_db.RegisterMessage(ComparePortraitToGalleryRequest)

ComparePortraitsRequest = _reflection.GeneratedProtocolMessageType('ComparePortraitsRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMPAREPORTRAITSREQUEST,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:ComparePortraitsRequest)
  })
_sym_db.RegisterMessage(ComparePortraitsRequest)

ComparePortraitsResponse = _reflection.GeneratedProtocolMessageType('ComparePortraitsResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMPAREPORTRAITSRESPONSE,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:ComparePortraitsResponse)
  })
_sym_db.RegisterMessage(ComparePortraitsResponse)

ElaborationRequest = _reflection.GeneratedProtocolMessageType('ElaborationRequest', (_message.Message,), {
  'DESCRIPTOR' : _ELABORATIONREQUEST,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:ElaborationRequest)
  })
_sym_db.RegisterMessage(ElaborationRequest)

ElaborationResponse = _reflection.GeneratedProtocolMessageType('ElaborationResponse', (_message.Message,), {

  'ImageWithExtractedData' : _reflection.GeneratedProtocolMessageType('ImageWithExtractedData', (_message.Message,), {

    'PortraitWithEmbedding' : _reflection.GeneratedProtocolMessageType('PortraitWithEmbedding', (_message.Message,), {
      'DESCRIPTOR' : _ELABORATIONRESPONSE_IMAGEWITHEXTRACTEDDATA_PORTRAITWITHEMBEDDING,
      '__module__' : 'gateway_pb2'
      # @@protoc_insertion_point(class_scope:ElaborationResponse.ImageWithExtractedData.PortraitWithEmbedding)
      })
    ,
    'DESCRIPTOR' : _ELABORATIONRESPONSE_IMAGEWITHEXTRACTEDDATA,
    '__module__' : 'gateway_pb2'
    # @@protoc_insertion_point(class_scope:ElaborationResponse.ImageWithExtractedData)
    })
  ,
  'DESCRIPTOR' : _ELABORATIONRESPONSE,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:ElaborationResponse)
  })
_sym_db.RegisterMessage(ElaborationResponse)
_sym_db.RegisterMessage(ElaborationResponse.ImageWithExtractedData)
_sym_db.RegisterMessage(ElaborationResponse.ImageWithExtractedData.PortraitWithEmbedding)



_GATEWAY = _descriptor.ServiceDescriptor(
  name='Gateway',
  full_name='Gateway',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=592,
  serialized_end=805,
  methods=[
  _descriptor.MethodDescriptor(
    name='elaborate',
    full_name='Gateway.elaborate',
    index=0,
    containing_service=None,
    input_type=_ELABORATIONREQUEST,
    output_type=_ELABORATIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='comparePortraits',
    full_name='Gateway.comparePortraits',
    index=1,
    containing_service=None,
    input_type=_COMPAREPORTRAITSREQUEST,
    output_type=common__pb2._COMPARISONRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='comparePortraitToGallery',
    full_name='Gateway.comparePortraitToGallery',
    index=2,
    containing_service=None,
    input_type=_COMPAREPORTRAITTOGALLERYREQUEST,
    output_type=common__pb2._COMPARISONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GATEWAY)

DESCRIPTOR.services_by_name['Gateway'] = _GATEWAY

# @@protoc_insertion_point(module_scope)