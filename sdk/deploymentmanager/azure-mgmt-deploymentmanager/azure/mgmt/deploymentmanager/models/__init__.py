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

try:
    from ._models_py3 import ApiKeyAuthentication
    from ._models_py3 import ArtifactSource
    from ._models_py3 import ArtifactSourcePropertiesModel
    from ._models_py3 import Authentication
    from ._models_py3 import AzureEntityResource
    from ._models_py3 import CloudErrorBody
    from ._models_py3 import HealthCheckStepAttributes
    from ._models_py3 import HealthCheckStepProperties
    from ._models_py3 import Identity
    from ._models_py3 import Message
    from ._models_py3 import Operation
    from ._models_py3 import OperationDetail
    from ._models_py3 import OperationsList
    from ._models_py3 import PrePostStep
    from ._models_py3 import ProxyResource
    from ._models_py3 import Resource
    from ._models_py3 import ResourceOperation
    from ._models_py3 import RestHealthCheck
    from ._models_py3 import RestHealthCheckStepAttributes
    from ._models_py3 import RestRequest
    from ._models_py3 import RestRequestAuthentication
    from ._models_py3 import RestResponse
    from ._models_py3 import RestResponseRegex
    from ._models_py3 import Rollout
    from ._models_py3 import RolloutIdentityAuthentication
    from ._models_py3 import RolloutOperationInfo
    from ._models_py3 import RolloutPropertiesModel
    from ._models_py3 import RolloutRequest
    from ._models_py3 import RolloutStep
    from ._models_py3 import SasAuthentication
    from ._models_py3 import Service
    from ._models_py3 import ServiceProperties
    from ._models_py3 import ServiceResource
    from ._models_py3 import ServiceTopologyProperties
    from ._models_py3 import ServiceTopologyResource
    from ._models_py3 import ServiceUnit
    from ._models_py3 import ServiceUnitArtifacts
    from ._models_py3 import ServiceUnitProperties
    from ._models_py3 import ServiceUnitResource
    from ._models_py3 import StepGroup
    from ._models_py3 import StepOperationInfo
    from ._models_py3 import StepProperties
    from ._models_py3 import StepResource
    from ._models_py3 import TrackedResource
    from ._models_py3 import WaitStepAttributes
    from ._models_py3 import WaitStepProperties
except (SyntaxError, ImportError):
    from ._models import ApiKeyAuthentication
    from ._models import ArtifactSource
    from ._models import ArtifactSourcePropertiesModel
    from ._models import Authentication
    from ._models import AzureEntityResource
    from ._models import CloudErrorBody
    from ._models import HealthCheckStepAttributes
    from ._models import HealthCheckStepProperties
    from ._models import Identity
    from ._models import Message
    from ._models import Operation
    from ._models import OperationDetail
    from ._models import OperationsList
    from ._models import PrePostStep
    from ._models import ProxyResource
    from ._models import Resource
    from ._models import ResourceOperation
    from ._models import RestHealthCheck
    from ._models import RestHealthCheckStepAttributes
    from ._models import RestRequest
    from ._models import RestRequestAuthentication
    from ._models import RestResponse
    from ._models import RestResponseRegex
    from ._models import Rollout
    from ._models import RolloutIdentityAuthentication
    from ._models import RolloutOperationInfo
    from ._models import RolloutPropertiesModel
    from ._models import RolloutRequest
    from ._models import RolloutStep
    from ._models import SasAuthentication
    from ._models import Service
    from ._models import ServiceProperties
    from ._models import ServiceResource
    from ._models import ServiceTopologyProperties
    from ._models import ServiceTopologyResource
    from ._models import ServiceUnit
    from ._models import ServiceUnitArtifacts
    from ._models import ServiceUnitProperties
    from ._models import ServiceUnitResource
    from ._models import StepGroup
    from ._models import StepOperationInfo
    from ._models import StepProperties
    from ._models import StepResource
    from ._models import TrackedResource
    from ._models import WaitStepAttributes
    from ._models import WaitStepProperties
from ._deployment_manager_client_enums import (
    DeploymentMode,
    RestRequestMethod,
    RestMatchQuantifier,
    RestAuthLocation,
)

__all__ = [
    'ApiKeyAuthentication',
    'ArtifactSource',
    'ArtifactSourcePropertiesModel',
    'Authentication',
    'AzureEntityResource',
    'CloudErrorBody',
    'HealthCheckStepAttributes',
    'HealthCheckStepProperties',
    'Identity',
    'Message',
    'Operation',
    'OperationDetail',
    'OperationsList',
    'PrePostStep',
    'ProxyResource',
    'Resource',
    'ResourceOperation',
    'RestHealthCheck',
    'RestHealthCheckStepAttributes',
    'RestRequest',
    'RestRequestAuthentication',
    'RestResponse',
    'RestResponseRegex',
    'Rollout',
    'RolloutIdentityAuthentication',
    'RolloutOperationInfo',
    'RolloutPropertiesModel',
    'RolloutRequest',
    'RolloutStep',
    'SasAuthentication',
    'Service',
    'ServiceProperties',
    'ServiceResource',
    'ServiceTopologyProperties',
    'ServiceTopologyResource',
    'ServiceUnit',
    'ServiceUnitArtifacts',
    'ServiceUnitProperties',
    'ServiceUnitResource',
    'StepGroup',
    'StepOperationInfo',
    'StepProperties',
    'StepResource',
    'TrackedResource',
    'WaitStepAttributes',
    'WaitStepProperties',
    'DeploymentMode',
    'RestRequestMethod',
    'RestMatchQuantifier',
    'RestAuthLocation',
]
