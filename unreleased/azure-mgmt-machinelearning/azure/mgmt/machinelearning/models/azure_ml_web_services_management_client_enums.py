# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class ProvisioningState(Enum):

    unknown = "Unknown"
    provisioning = "Provisioning"
    succeeded = "Succeeded"
    failed = "Failed"


class DiagnosticsLevel(Enum):

    none = "None"
    error = "Error"
    all = "All"


class ColumnType(Enum):

    boolean = "Boolean"
    integer = "Integer"
    number = "Number"
    string = "String"


class ColumnFormat(Enum):

    byte = "Byte"
    char = "Char"
    complex64 = "Complex64"
    complex128 = "Complex128"
    date_time = "Date-time"
    date_time_offset = "Date-timeOffset"
    double = "Double"
    duration = "Duration"
    float_enum = "Float"
    int8 = "Int8"
    int16 = "Int16"
    int32 = "Int32"
    int64 = "Int64"
    uint8 = "Uint8"
    uint16 = "Uint16"
    uint32 = "Uint32"
    uint64 = "Uint64"


class AssetType(Enum):

    module = "Module"
    resource = "Resource"


class InputPortType(Enum):

    dataset = "Dataset"


class OutputPortType(Enum):

    dataset = "Dataset"


class ParameterType(Enum):

    string = "String"
    int_enum = "Int"
    float_enum = "Float"
    enumerated = "Enumerated"
    script = "Script"
    mode = "Mode"
    credential = "Credential"
    boolean = "Boolean"
    double = "Double"
    column_picker = "ColumnPicker"
    parameter_range = "ParameterRange"
    data_gateway_name = "DataGatewayName"
