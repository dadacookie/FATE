# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feature-selection-meta.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='feature-selection-meta.proto',
  package='com.webank.ai.fate.core.mlmodel.buffer',
  syntax='proto3',
  serialized_options=b'B\031FeatureSelectionMetaProto',
  serialized_pb=b'\n\x1c\x66\x65\x61ture-selection-meta.proto\x12&com.webank.ai.fate.core.mlmodel.buffer\"\x90\x06\n\x14\x46\x65\x61tureSelectionMeta\x12\x16\n\x0e\x66ilter_methods\x18\x01 \x03(\t\x12\x0c\n\x04\x63ols\x18\x03 \x03(\t\x12L\n\x0bunique_meta\x18\x04 \x01(\x0b\x32\x37.com.webank.ai.fate.core.mlmodel.buffer.UniqueValueMeta\x12S\n\riv_value_meta\x18\x05 \x01(\x0b\x32<.com.webank.ai.fate.core.mlmodel.buffer.IVValueSelectionMeta\x12]\n\x12iv_percentile_meta\x18\x06 \x01(\x0b\x32\x41.com.webank.ai.fate.core.mlmodel.buffer.IVPercentileSelectionMeta\x12]\n\x11variance_coe_meta\x18\x07 \x01(\x0b\x32\x42.com.webank.ai.fate.core.mlmodel.buffer.VarianceOfCoeSelectionMeta\x12V\n\x0coutlier_meta\x18\x08 \x01(\x0b\x32@.com.webank.ai.fate.core.mlmodel.buffer.OutlierColsSelectionMeta\x12Q\n\rmanually_meta\x18\t \x01(\x0b\x32:.com.webank.ai.fate.core.mlmodel.buffer.ManuallyFilterMeta\x12\x10\n\x08need_run\x18\n \x01(\x08\x12`\n\x15pencentage_value_meta\x18\x0b \x01(\x0b\x32\x41.com.webank.ai.fate.core.mlmodel.buffer.PercentageValueFilterMeta\x12R\n\riv_top_k_meta\x18\x0c \x01(\x0b\x32;.com.webank.ai.fate.core.mlmodel.buffer.IVTopKSelectionMeta\"\x1e\n\x0fUniqueValueMeta\x12\x0b\n\x03\x65ps\x18\x01 \x01(\x01\"C\n\x14IVValueSelectionMeta\x12\x17\n\x0fvalue_threshold\x18\x01 \x01(\x01\x12\x12\n\nlocal_only\x18\x02 \x01(\x08\"M\n\x19IVPercentileSelectionMeta\x12\x1c\n\x14percentile_threshold\x18\x01 \x01(\x01\x12\x12\n\nlocal_only\x18\x02 \x01(\x08\"4\n\x13IVTopKSelectionMeta\x12\t\n\x01k\x18\x01 \x01(\x03\x12\x12\n\nlocal_only\x18\x02 \x01(\x08\"5\n\x1aVarianceOfCoeSelectionMeta\x12\x17\n\x0fvalue_threshold\x18\x01 \x01(\x01\"G\n\x18OutlierColsSelectionMeta\x12\x12\n\npercentile\x18\x01 \x01(\x01\x12\x17\n\x0fupper_threshold\x18\x02 \x01(\x01\".\n\x12ManuallyFilterMeta\x12\x18\n\x10\x66ilter_out_names\x18\x01 \x03(\t\".\n\x19PercentageValueFilterMeta\x12\x11\n\tupper_pct\x18\x01 \x01(\x01\x42\x1b\x42\x19\x46\x65\x61tureSelectionMetaProtob\x06proto3'
)




_FEATURESELECTIONMETA = _descriptor.Descriptor(
  name='FeatureSelectionMeta',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureSelectionMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter_methods', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureSelectionMeta.filter_methods', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cols', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureSelectionMeta.cols', index=1,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unique_meta', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureSelectionMeta.unique_meta', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iv_value_meta', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureSelectionMeta.iv_value_meta', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iv_percentile_meta', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureSelectionMeta.iv_percentile_meta', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='variance_coe_meta', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureSelectionMeta.variance_coe_meta', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outlier_meta', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureSelectionMeta.outlier_meta', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manually_meta', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureSelectionMeta.manually_meta', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='need_run', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureSelectionMeta.need_run', index=8,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pencentage_value_meta', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureSelectionMeta.pencentage_value_meta', index=9,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iv_top_k_meta', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureSelectionMeta.iv_top_k_meta', index=10,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=73,
  serialized_end=857,
)


_UNIQUEVALUEMETA = _descriptor.Descriptor(
  name='UniqueValueMeta',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.UniqueValueMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='eps', full_name='com.webank.ai.fate.core.mlmodel.buffer.UniqueValueMeta.eps', index=0,
      number=1, type=1, cpp_type=5, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=859,
  serialized_end=889,
)


_IVVALUESELECTIONMETA = _descriptor.Descriptor(
  name='IVValueSelectionMeta',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.IVValueSelectionMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value_threshold', full_name='com.webank.ai.fate.core.mlmodel.buffer.IVValueSelectionMeta.value_threshold', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_only', full_name='com.webank.ai.fate.core.mlmodel.buffer.IVValueSelectionMeta.local_only', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=891,
  serialized_end=958,
)


_IVPERCENTILESELECTIONMETA = _descriptor.Descriptor(
  name='IVPercentileSelectionMeta',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.IVPercentileSelectionMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='percentile_threshold', full_name='com.webank.ai.fate.core.mlmodel.buffer.IVPercentileSelectionMeta.percentile_threshold', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_only', full_name='com.webank.ai.fate.core.mlmodel.buffer.IVPercentileSelectionMeta.local_only', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=960,
  serialized_end=1037,
)


_IVTOPKSELECTIONMETA = _descriptor.Descriptor(
  name='IVTopKSelectionMeta',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.IVTopKSelectionMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='k', full_name='com.webank.ai.fate.core.mlmodel.buffer.IVTopKSelectionMeta.k', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_only', full_name='com.webank.ai.fate.core.mlmodel.buffer.IVTopKSelectionMeta.local_only', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1039,
  serialized_end=1091,
)


_VARIANCEOFCOESELECTIONMETA = _descriptor.Descriptor(
  name='VarianceOfCoeSelectionMeta',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.VarianceOfCoeSelectionMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value_threshold', full_name='com.webank.ai.fate.core.mlmodel.buffer.VarianceOfCoeSelectionMeta.value_threshold', index=0,
      number=1, type=1, cpp_type=5, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1093,
  serialized_end=1146,
)


_OUTLIERCOLSSELECTIONMETA = _descriptor.Descriptor(
  name='OutlierColsSelectionMeta',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.OutlierColsSelectionMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='percentile', full_name='com.webank.ai.fate.core.mlmodel.buffer.OutlierColsSelectionMeta.percentile', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upper_threshold', full_name='com.webank.ai.fate.core.mlmodel.buffer.OutlierColsSelectionMeta.upper_threshold', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1148,
  serialized_end=1219,
)


_MANUALLYFILTERMETA = _descriptor.Descriptor(
  name='ManuallyFilterMeta',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.ManuallyFilterMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter_out_names', full_name='com.webank.ai.fate.core.mlmodel.buffer.ManuallyFilterMeta.filter_out_names', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=1221,
  serialized_end=1267,
)


_PERCENTAGEVALUEFILTERMETA = _descriptor.Descriptor(
  name='PercentageValueFilterMeta',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.PercentageValueFilterMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='upper_pct', full_name='com.webank.ai.fate.core.mlmodel.buffer.PercentageValueFilterMeta.upper_pct', index=0,
      number=1, type=1, cpp_type=5, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1269,
  serialized_end=1315,
)

_FEATURESELECTIONMETA.fields_by_name['unique_meta'].message_type = _UNIQUEVALUEMETA
_FEATURESELECTIONMETA.fields_by_name['iv_value_meta'].message_type = _IVVALUESELECTIONMETA
_FEATURESELECTIONMETA.fields_by_name['iv_percentile_meta'].message_type = _IVPERCENTILESELECTIONMETA
_FEATURESELECTIONMETA.fields_by_name['variance_coe_meta'].message_type = _VARIANCEOFCOESELECTIONMETA
_FEATURESELECTIONMETA.fields_by_name['outlier_meta'].message_type = _OUTLIERCOLSSELECTIONMETA
_FEATURESELECTIONMETA.fields_by_name['manually_meta'].message_type = _MANUALLYFILTERMETA
_FEATURESELECTIONMETA.fields_by_name['pencentage_value_meta'].message_type = _PERCENTAGEVALUEFILTERMETA
_FEATURESELECTIONMETA.fields_by_name['iv_top_k_meta'].message_type = _IVTOPKSELECTIONMETA
DESCRIPTOR.message_types_by_name['FeatureSelectionMeta'] = _FEATURESELECTIONMETA
DESCRIPTOR.message_types_by_name['UniqueValueMeta'] = _UNIQUEVALUEMETA
DESCRIPTOR.message_types_by_name['IVValueSelectionMeta'] = _IVVALUESELECTIONMETA
DESCRIPTOR.message_types_by_name['IVPercentileSelectionMeta'] = _IVPERCENTILESELECTIONMETA
DESCRIPTOR.message_types_by_name['IVTopKSelectionMeta'] = _IVTOPKSELECTIONMETA
DESCRIPTOR.message_types_by_name['VarianceOfCoeSelectionMeta'] = _VARIANCEOFCOESELECTIONMETA
DESCRIPTOR.message_types_by_name['OutlierColsSelectionMeta'] = _OUTLIERCOLSSELECTIONMETA
DESCRIPTOR.message_types_by_name['ManuallyFilterMeta'] = _MANUALLYFILTERMETA
DESCRIPTOR.message_types_by_name['PercentageValueFilterMeta'] = _PERCENTAGEVALUEFILTERMETA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeatureSelectionMeta = _reflection.GeneratedProtocolMessageType('FeatureSelectionMeta', (_message.Message,), {
  'DESCRIPTOR' : _FEATURESELECTIONMETA,
  '__module__' : 'feature_selection_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.FeatureSelectionMeta)
  })
_sym_db.RegisterMessage(FeatureSelectionMeta)

UniqueValueMeta = _reflection.GeneratedProtocolMessageType('UniqueValueMeta', (_message.Message,), {
  'DESCRIPTOR' : _UNIQUEVALUEMETA,
  '__module__' : 'feature_selection_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.UniqueValueMeta)
  })
_sym_db.RegisterMessage(UniqueValueMeta)

IVValueSelectionMeta = _reflection.GeneratedProtocolMessageType('IVValueSelectionMeta', (_message.Message,), {
  'DESCRIPTOR' : _IVVALUESELECTIONMETA,
  '__module__' : 'feature_selection_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.IVValueSelectionMeta)
  })
_sym_db.RegisterMessage(IVValueSelectionMeta)

IVPercentileSelectionMeta = _reflection.GeneratedProtocolMessageType('IVPercentileSelectionMeta', (_message.Message,), {
  'DESCRIPTOR' : _IVPERCENTILESELECTIONMETA,
  '__module__' : 'feature_selection_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.IVPercentileSelectionMeta)
  })
_sym_db.RegisterMessage(IVPercentileSelectionMeta)

IVTopKSelectionMeta = _reflection.GeneratedProtocolMessageType('IVTopKSelectionMeta', (_message.Message,), {
  'DESCRIPTOR' : _IVTOPKSELECTIONMETA,
  '__module__' : 'feature_selection_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.IVTopKSelectionMeta)
  })
_sym_db.RegisterMessage(IVTopKSelectionMeta)

VarianceOfCoeSelectionMeta = _reflection.GeneratedProtocolMessageType('VarianceOfCoeSelectionMeta', (_message.Message,), {
  'DESCRIPTOR' : _VARIANCEOFCOESELECTIONMETA,
  '__module__' : 'feature_selection_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.VarianceOfCoeSelectionMeta)
  })
_sym_db.RegisterMessage(VarianceOfCoeSelectionMeta)

OutlierColsSelectionMeta = _reflection.GeneratedProtocolMessageType('OutlierColsSelectionMeta', (_message.Message,), {
  'DESCRIPTOR' : _OUTLIERCOLSSELECTIONMETA,
  '__module__' : 'feature_selection_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.OutlierColsSelectionMeta)
  })
_sym_db.RegisterMessage(OutlierColsSelectionMeta)

ManuallyFilterMeta = _reflection.GeneratedProtocolMessageType('ManuallyFilterMeta', (_message.Message,), {
  'DESCRIPTOR' : _MANUALLYFILTERMETA,
  '__module__' : 'feature_selection_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.ManuallyFilterMeta)
  })
_sym_db.RegisterMessage(ManuallyFilterMeta)

PercentageValueFilterMeta = _reflection.GeneratedProtocolMessageType('PercentageValueFilterMeta', (_message.Message,), {
  'DESCRIPTOR' : _PERCENTAGEVALUEFILTERMETA,
  '__module__' : 'feature_selection_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.PercentageValueFilterMeta)
  })
_sym_db.RegisterMessage(PercentageValueFilterMeta)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
