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

from .service_bus_message import ServiceBusMessage


class ServiceBusQueueMessage(ServiceBusMessage):
    """ServiceBusQueueMessage.

    :param authentication: Gets or sets the Service Bus authentication.
    :type authentication: :class:`ServiceBusAuthentication
     <azure.mgmt.scheduler.models.ServiceBusAuthentication>`
    :param brokered_message_properties: Gets or sets the brokered message
     properties.
    :type brokered_message_properties:
     :class:`ServiceBusBrokeredMessageProperties
     <azure.mgmt.scheduler.models.ServiceBusBrokeredMessageProperties>`
    :param custom_message_properties: Gets or sets the custom message
     properties.
    :type custom_message_properties: dict
    :param message: Gets or sets the message.
    :type message: str
    :param namespace: Gets or sets the namespace.
    :type namespace: str
    :param transport_type: Gets or sets the transport type. Possible values
     include: 'NotSpecified', 'NetMessaging', 'AMQP'
    :type transport_type: str or :class:`ServiceBusTransportType
     <azure.mgmt.scheduler.models.ServiceBusTransportType>`
    :param queue_name: Gets or sets the queue name.
    :type queue_name: str
    """ 

    _attribute_map = {
        'authentication': {'key': 'authentication', 'type': 'ServiceBusAuthentication'},
        'brokered_message_properties': {'key': 'brokeredMessageProperties', 'type': 'ServiceBusBrokeredMessageProperties'},
        'custom_message_properties': {'key': 'customMessageProperties', 'type': '{str}'},
        'message': {'key': 'message', 'type': 'str'},
        'namespace': {'key': 'namespace', 'type': 'str'},
        'transport_type': {'key': 'transportType', 'type': 'ServiceBusTransportType'},
        'queue_name': {'key': 'queueName', 'type': 'str'},
    }

    def __init__(self, authentication=None, brokered_message_properties=None, custom_message_properties=None, message=None, namespace=None, transport_type=None, queue_name=None):
        super(ServiceBusQueueMessage, self).__init__(authentication=authentication, brokered_message_properties=brokered_message_properties, custom_message_properties=custom_message_properties, message=message, namespace=namespace, transport_type=transport_type)
        self.queue_name = queue_name
