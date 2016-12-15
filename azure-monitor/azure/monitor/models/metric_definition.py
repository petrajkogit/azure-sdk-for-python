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

from msrest.serialization import Model


class MetricDefinition(Model):
    """Metric definition class specifies the metadata for a metric.

    :param resource_id: the resource identifier of the resource that emitted
     the metric.
    :type resource_id: str
    :param name: the name and the display name of the metric, i.e. it is a
     localizable string.
    :type name: :class:`LocalizableString
     <azure.monitor.models.LocalizableString>`
    :param unit: the unit of the metric. Possible values include: 'Count',
     'Bytes', 'Seconds', 'CountPerSecond', 'BytesPerSecond', 'Percent',
     'MilliSeconds'
    :type unit: str or :class:`Unit <azure.monitor.models.Unit>`
    :param primary_aggregation_type: the primary aggregation type value
     defining how to use the values for display. Possible values include:
     'None', 'Average', 'Count', 'Minimum', 'Maximum', 'Total'
    :type primary_aggregation_type: str or :class:`AggregationType
     <azure.monitor.models.AggregationType>`
    :param metric_availabilities: the collection of what aggregation intervals
     are available to be queried.
    :type metric_availabilities: list of :class:`MetricAvailability
     <azure.monitor.models.MetricAvailability>`
    :param id: the resource identifier of the metric definition.
    :type id: str
    """

    _attribute_map = {
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'LocalizableString'},
        'unit': {'key': 'unit', 'type': 'Unit'},
        'primary_aggregation_type': {'key': 'primaryAggregationType', 'type': 'AggregationType'},
        'metric_availabilities': {'key': 'metricAvailabilities', 'type': '[MetricAvailability]'},
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(self, resource_id=None, name=None, unit=None, primary_aggregation_type=None, metric_availabilities=None, id=None):
        self.resource_id = resource_id
        self.name = name
        self.unit = unit
        self.primary_aggregation_type = primary_aggregation_type
        self.metric_availabilities = metric_availabilities
        self.id = id
