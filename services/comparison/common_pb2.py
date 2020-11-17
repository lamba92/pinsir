# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x63ommon.proto\"\xbe\x02\n\x0e\x46\x61\x63\x65\x41nnotation\x12 \n\x03\x62ox\x18\x01 \x01(\x0b\x32\x13.FaceAnnotation.Box\x12\x12\n\nconfidence\x18\x02 \x01(\x01\x12,\n\tkeypoints\x18\x03 \x01(\x0b\x32\x19.FaceAnnotation.Keypoints\x1a:\n\x03\x42ox\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\r\n\x05width\x18\x03 \x01(\x05\x12\x0e\n\x06height\x18\x04 \x01(\x05\x1a\x8b\x01\n\tKeypoints\x12\x17\n\x07leftEye\x18\x01 \x01(\x0b\x32\x06.Point\x12\x18\n\x08rightEye\x18\x02 \x01(\x0b\x32\x06.Point\x12\x14\n\x04nose\x18\x03 \x01(\x0b\x32\x06.Point\x12\x19\n\tmouthLeft\x18\x04 \x01(\x0b\x32\x06.Point\x12\x1a\n\nmouthRight\x18\x05 \x01(\x0b\x32\x06.Point\"\x1d\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\"#\n\x12\x45mbeddingContainer\x12\r\n\x05\x61rray\x18\x01 \x03(\x01\"6\n\x10\x43omparisonResult\x12\x0e\n\x06isSame\x18\x01 \x01(\x08\x12\x12\n\nconfidence\x18\x02 \x01(\x01\"8\n\x12\x43omparisonResponse\x12\"\n\x07results\x18\x01 \x03(\x0b\x32\x11.ComparisonResultb\x06proto3'
)




_FACEANNOTATION_BOX = _descriptor.Descriptor(
  name='Box',
  full_name='FaceAnnotation.Box',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='FaceAnnotation.Box.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='FaceAnnotation.Box.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='FaceAnnotation.Box.width', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='FaceAnnotation.Box.height', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=135,
  serialized_end=193,
)

_FACEANNOTATION_KEYPOINTS = _descriptor.Descriptor(
  name='Keypoints',
  full_name='FaceAnnotation.Keypoints',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='leftEye', full_name='FaceAnnotation.Keypoints.leftEye', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rightEye', full_name='FaceAnnotation.Keypoints.rightEye', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nose', full_name='FaceAnnotation.Keypoints.nose', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mouthLeft', full_name='FaceAnnotation.Keypoints.mouthLeft', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mouthRight', full_name='FaceAnnotation.Keypoints.mouthRight', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=196,
  serialized_end=335,
)

_FACEANNOTATION = _descriptor.Descriptor(
  name='FaceAnnotation',
  full_name='FaceAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='box', full_name='FaceAnnotation.box', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='FaceAnnotation.confidence', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keypoints', full_name='FaceAnnotation.keypoints', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_FACEANNOTATION_BOX, _FACEANNOTATION_KEYPOINTS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=335,
)


_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='Point.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='Point.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=337,
  serialized_end=366,
)


_EMBEDDINGCONTAINER = _descriptor.Descriptor(
  name='EmbeddingContainer',
  full_name='EmbeddingContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='array', full_name='EmbeddingContainer.array', index=0,
      number=1, type=1, cpp_type=5, label=3,
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
  serialized_start=368,
  serialized_end=403,
)


_COMPARISONRESULT = _descriptor.Descriptor(
  name='ComparisonResult',
  full_name='ComparisonResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isSame', full_name='ComparisonResult.isSame', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='ComparisonResult.confidence', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=405,
  serialized_end=459,
)


_COMPARISONRESPONSE = _descriptor.Descriptor(
  name='ComparisonResponse',
  full_name='ComparisonResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='ComparisonResponse.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=461,
  serialized_end=517,
)

_FACEANNOTATION_BOX.containing_type = _FACEANNOTATION
_FACEANNOTATION_KEYPOINTS.fields_by_name['leftEye'].message_type = _POINT
_FACEANNOTATION_KEYPOINTS.fields_by_name['rightEye'].message_type = _POINT
_FACEANNOTATION_KEYPOINTS.fields_by_name['nose'].message_type = _POINT
_FACEANNOTATION_KEYPOINTS.fields_by_name['mouthLeft'].message_type = _POINT
_FACEANNOTATION_KEYPOINTS.fields_by_name['mouthRight'].message_type = _POINT
_FACEANNOTATION_KEYPOINTS.containing_type = _FACEANNOTATION
_FACEANNOTATION.fields_by_name['box'].message_type = _FACEANNOTATION_BOX
_FACEANNOTATION.fields_by_name['keypoints'].message_type = _FACEANNOTATION_KEYPOINTS
_COMPARISONRESPONSE.fields_by_name['results'].message_type = _COMPARISONRESULT
DESCRIPTOR.message_types_by_name['FaceAnnotation'] = _FACEANNOTATION
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['EmbeddingContainer'] = _EMBEDDINGCONTAINER
DESCRIPTOR.message_types_by_name['ComparisonResult'] = _COMPARISONRESULT
DESCRIPTOR.message_types_by_name['ComparisonResponse'] = _COMPARISONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FaceAnnotation = _reflection.GeneratedProtocolMessageType('FaceAnnotation', (_message.Message,), {

  'Box' : _reflection.GeneratedProtocolMessageType('Box', (_message.Message,), {
    'DESCRIPTOR' : _FACEANNOTATION_BOX,
    '__module__' : 'common_pb2'
    # @@protoc_insertion_point(class_scope:FaceAnnotation.Box)
    })
  ,

  'Keypoints' : _reflection.GeneratedProtocolMessageType('Keypoints', (_message.Message,), {
    'DESCRIPTOR' : _FACEANNOTATION_KEYPOINTS,
    '__module__' : 'common_pb2'
    # @@protoc_insertion_point(class_scope:FaceAnnotation.Keypoints)
    })
  ,
  'DESCRIPTOR' : _FACEANNOTATION,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:FaceAnnotation)
  })
_sym_db.RegisterMessage(FaceAnnotation)
_sym_db.RegisterMessage(FaceAnnotation.Box)
_sym_db.RegisterMessage(FaceAnnotation.Keypoints)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {
  'DESCRIPTOR' : _POINT,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:Point)
  })
_sym_db.RegisterMessage(Point)

EmbeddingContainer = _reflection.GeneratedProtocolMessageType('EmbeddingContainer', (_message.Message,), {
  'DESCRIPTOR' : _EMBEDDINGCONTAINER,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:EmbeddingContainer)
  })
_sym_db.RegisterMessage(EmbeddingContainer)

ComparisonResult = _reflection.GeneratedProtocolMessageType('ComparisonResult', (_message.Message,), {
  'DESCRIPTOR' : _COMPARISONRESULT,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:ComparisonResult)
  })
_sym_db.RegisterMessage(ComparisonResult)

ComparisonResponse = _reflection.GeneratedProtocolMessageType('ComparisonResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMPARISONRESPONSE,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:ComparisonResponse)
  })
_sym_db.RegisterMessage(ComparisonResponse)


# @@protoc_insertion_point(module_scope)