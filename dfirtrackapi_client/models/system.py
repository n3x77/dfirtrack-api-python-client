# coding: utf-8

"""
    DFIRTrack

    OpenAPI 3 - Documentation of DFIRTrack API  # noqa: E501

    The version of the OpenAPI document: 0.4.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dfirtrackapi_client.configuration import Configuration


class System(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'system_id': 'int',
        'system_uuid': 'str',
        'system_name': 'str',
        'domain': 'int',
        'dnsname': 'int',
        'systemstatus': 'int',
        'analysisstatus': 'int',
        'reason': 'int',
        'recommendation': 'int',
        'systemtype': 'int',
        'ip': 'list[int]',
        'os': 'int',
        'osarch': 'int',
        'system_lastbooted_time': 'datetime',
        'system_deprecated_time': 'datetime',
        'system_is_vm': 'bool',
        'host_system': 'int',
        'company': 'list[int]',
        'location': 'int',
        'serviceprovider': 'int',
        'contact': 'int',
        'tag': 'list[int]',
        'case': 'list[int]',
        'system_api_time': 'datetime',
        'system_create_time': 'datetime',
        'system_created_by_user_id': 'int',
        'system_modify_time': 'datetime',
        'system_modified_by_user_id': 'int',
        'system_export_markdown': 'bool',
        'system_export_spreadsheet': 'bool'
    }

    attribute_map = {
        'system_id': 'system_id',
        'system_uuid': 'system_uuid',
        'system_name': 'system_name',
        'domain': 'domain',
        'dnsname': 'dnsname',
        'systemstatus': 'systemstatus',
        'analysisstatus': 'analysisstatus',
        'reason': 'reason',
        'recommendation': 'recommendation',
        'systemtype': 'systemtype',
        'ip': 'ip',
        'os': 'os',
        'osarch': 'osarch',
        'system_lastbooted_time': 'system_lastbooted_time',
        'system_deprecated_time': 'system_deprecated_time',
        'system_is_vm': 'system_is_vm',
        'host_system': 'host_system',
        'company': 'company',
        'location': 'location',
        'serviceprovider': 'serviceprovider',
        'contact': 'contact',
        'tag': 'tag',
        'case': 'case',
        'system_api_time': 'system_api_time',
        'system_create_time': 'system_create_time',
        'system_created_by_user_id': 'system_created_by_user_id',
        'system_modify_time': 'system_modify_time',
        'system_modified_by_user_id': 'system_modified_by_user_id',
        'system_export_markdown': 'system_export_markdown',
        'system_export_spreadsheet': 'system_export_spreadsheet'
    }

    def __init__(self, system_id=None, system_uuid=None, system_name=None, domain=None, dnsname=None, systemstatus=None, analysisstatus=None, reason=None, recommendation=None, systemtype=None, ip=None, os=None, osarch=None, system_lastbooted_time=None, system_deprecated_time=None, system_is_vm=None, host_system=None, company=None, location=None, serviceprovider=None, contact=None, tag=None, case=None, system_api_time=None, system_create_time=None, system_created_by_user_id=None, system_modify_time=None, system_modified_by_user_id=None, system_export_markdown=None, system_export_spreadsheet=None, local_vars_configuration=None):  # noqa: E501
        """System - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._system_id = None
        self._system_uuid = None
        self._system_name = None
        self._domain = None
        self._dnsname = None
        self._systemstatus = None
        self._analysisstatus = None
        self._reason = None
        self._recommendation = None
        self._systemtype = None
        self._ip = None
        self._os = None
        self._osarch = None
        self._system_lastbooted_time = None
        self._system_deprecated_time = None
        self._system_is_vm = None
        self._host_system = None
        self._company = None
        self._location = None
        self._serviceprovider = None
        self._contact = None
        self._tag = None
        self._case = None
        self._system_api_time = None
        self._system_create_time = None
        self._system_created_by_user_id = None
        self._system_modify_time = None
        self._system_modified_by_user_id = None
        self._system_export_markdown = None
        self._system_export_spreadsheet = None
        self.discriminator = None

        if system_id is not None:
            self.system_id = system_id
        if system_uuid is not None:
            self.system_uuid = system_uuid
        self.system_name = system_name
        self.domain = domain
        self.dnsname = dnsname
        self.systemstatus = systemstatus
        self.analysisstatus = analysisstatus
        self.reason = reason
        self.recommendation = recommendation
        self.systemtype = systemtype
        if ip is not None:
            self.ip = ip
        self.os = os
        self.osarch = osarch
        self.system_lastbooted_time = system_lastbooted_time
        self.system_deprecated_time = system_deprecated_time
        self.system_is_vm = system_is_vm
        self.host_system = host_system
        if company is not None:
            self.company = company
        self.location = location
        self.serviceprovider = serviceprovider
        self.contact = contact
        if tag is not None:
            self.tag = tag
        if case is not None:
            self.case = case
        self.system_api_time = system_api_time
        if system_create_time is not None:
            self.system_create_time = system_create_time
        self.system_created_by_user_id = system_created_by_user_id
        self.system_modify_time = system_modify_time
        self.system_modified_by_user_id = system_modified_by_user_id
        if system_export_markdown is not None:
            self.system_export_markdown = system_export_markdown
        if system_export_spreadsheet is not None:
            self.system_export_spreadsheet = system_export_spreadsheet

    @property
    def system_id(self):
        """Gets the system_id of this System.  # noqa: E501


        :return: The system_id of this System.  # noqa: E501
        :rtype: int
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this System.


        :param system_id: The system_id of this System.  # noqa: E501
        :type: int
        """

        self._system_id = system_id

    @property
    def system_uuid(self):
        """Gets the system_uuid of this System.  # noqa: E501


        :return: The system_uuid of this System.  # noqa: E501
        :rtype: str
        """
        return self._system_uuid

    @system_uuid.setter
    def system_uuid(self, system_uuid):
        """Sets the system_uuid of this System.


        :param system_uuid: The system_uuid of this System.  # noqa: E501
        :type: str
        """

        self._system_uuid = system_uuid

    @property
    def system_name(self):
        """Gets the system_name of this System.  # noqa: E501


        :return: The system_name of this System.  # noqa: E501
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """Sets the system_name of this System.


        :param system_name: The system_name of this System.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and system_name is None:  # noqa: E501
            raise ValueError("Invalid value for `system_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                system_name is not None and len(system_name) > 50):
            raise ValueError("Invalid value for `system_name`, length must be less than or equal to `50`")  # noqa: E501

        self._system_name = system_name

    @property
    def domain(self):
        """Gets the domain of this System.  # noqa: E501


        :return: The domain of this System.  # noqa: E501
        :rtype: int
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this System.


        :param domain: The domain of this System.  # noqa: E501
        :type: int
        """

        self._domain = domain

    @property
    def dnsname(self):
        """Gets the dnsname of this System.  # noqa: E501


        :return: The dnsname of this System.  # noqa: E501
        :rtype: int
        """
        return self._dnsname

    @dnsname.setter
    def dnsname(self, dnsname):
        """Sets the dnsname of this System.


        :param dnsname: The dnsname of this System.  # noqa: E501
        :type: int
        """

        self._dnsname = dnsname

    @property
    def systemstatus(self):
        """Gets the systemstatus of this System.  # noqa: E501


        :return: The systemstatus of this System.  # noqa: E501
        :rtype: int
        """
        return self._systemstatus

    @systemstatus.setter
    def systemstatus(self, systemstatus):
        """Sets the systemstatus of this System.


        :param systemstatus: The systemstatus of this System.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and systemstatus is None:  # noqa: E501
            raise ValueError("Invalid value for `systemstatus`, must not be `None`")  # noqa: E501

        self._systemstatus = systemstatus

    @property
    def analysisstatus(self):
        """Gets the analysisstatus of this System.  # noqa: E501


        :return: The analysisstatus of this System.  # noqa: E501
        :rtype: int
        """
        return self._analysisstatus

    @analysisstatus.setter
    def analysisstatus(self, analysisstatus):
        """Sets the analysisstatus of this System.


        :param analysisstatus: The analysisstatus of this System.  # noqa: E501
        :type: int
        """

        self._analysisstatus = analysisstatus

    @property
    def reason(self):
        """Gets the reason of this System.  # noqa: E501


        :return: The reason of this System.  # noqa: E501
        :rtype: int
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this System.


        :param reason: The reason of this System.  # noqa: E501
        :type: int
        """

        self._reason = reason

    @property
    def recommendation(self):
        """Gets the recommendation of this System.  # noqa: E501


        :return: The recommendation of this System.  # noqa: E501
        :rtype: int
        """
        return self._recommendation

    @recommendation.setter
    def recommendation(self, recommendation):
        """Sets the recommendation of this System.


        :param recommendation: The recommendation of this System.  # noqa: E501
        :type: int
        """

        self._recommendation = recommendation

    @property
    def systemtype(self):
        """Gets the systemtype of this System.  # noqa: E501


        :return: The systemtype of this System.  # noqa: E501
        :rtype: int
        """
        return self._systemtype

    @systemtype.setter
    def systemtype(self, systemtype):
        """Sets the systemtype of this System.


        :param systemtype: The systemtype of this System.  # noqa: E501
        :type: int
        """

        self._systemtype = systemtype

    @property
    def ip(self):
        """Gets the ip of this System.  # noqa: E501


        :return: The ip of this System.  # noqa: E501
        :rtype: list[int]
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this System.


        :param ip: The ip of this System.  # noqa: E501
        :type: list[int]
        """

        self._ip = ip

    @property
    def os(self):
        """Gets the os of this System.  # noqa: E501


        :return: The os of this System.  # noqa: E501
        :rtype: int
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this System.


        :param os: The os of this System.  # noqa: E501
        :type: int
        """

        self._os = os

    @property
    def osarch(self):
        """Gets the osarch of this System.  # noqa: E501


        :return: The osarch of this System.  # noqa: E501
        :rtype: int
        """
        return self._osarch

    @osarch.setter
    def osarch(self, osarch):
        """Sets the osarch of this System.


        :param osarch: The osarch of this System.  # noqa: E501
        :type: int
        """

        self._osarch = osarch

    @property
    def system_lastbooted_time(self):
        """Gets the system_lastbooted_time of this System.  # noqa: E501


        :return: The system_lastbooted_time of this System.  # noqa: E501
        :rtype: datetime
        """
        return self._system_lastbooted_time

    @system_lastbooted_time.setter
    def system_lastbooted_time(self, system_lastbooted_time):
        """Sets the system_lastbooted_time of this System.


        :param system_lastbooted_time: The system_lastbooted_time of this System.  # noqa: E501
        :type: datetime
        """

        self._system_lastbooted_time = system_lastbooted_time

    @property
    def system_deprecated_time(self):
        """Gets the system_deprecated_time of this System.  # noqa: E501


        :return: The system_deprecated_time of this System.  # noqa: E501
        :rtype: datetime
        """
        return self._system_deprecated_time

    @system_deprecated_time.setter
    def system_deprecated_time(self, system_deprecated_time):
        """Sets the system_deprecated_time of this System.


        :param system_deprecated_time: The system_deprecated_time of this System.  # noqa: E501
        :type: datetime
        """

        self._system_deprecated_time = system_deprecated_time

    @property
    def system_is_vm(self):
        """Gets the system_is_vm of this System.  # noqa: E501


        :return: The system_is_vm of this System.  # noqa: E501
        :rtype: bool
        """
        return self._system_is_vm

    @system_is_vm.setter
    def system_is_vm(self, system_is_vm):
        """Sets the system_is_vm of this System.


        :param system_is_vm: The system_is_vm of this System.  # noqa: E501
        :type: bool
        """

        self._system_is_vm = system_is_vm

    @property
    def host_system(self):
        """Gets the host_system of this System.  # noqa: E501


        :return: The host_system of this System.  # noqa: E501
        :rtype: int
        """
        return self._host_system

    @host_system.setter
    def host_system(self, host_system):
        """Sets the host_system of this System.


        :param host_system: The host_system of this System.  # noqa: E501
        :type: int
        """

        self._host_system = host_system

    @property
    def company(self):
        """Gets the company of this System.  # noqa: E501


        :return: The company of this System.  # noqa: E501
        :rtype: list[int]
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this System.


        :param company: The company of this System.  # noqa: E501
        :type: list[int]
        """

        self._company = company

    @property
    def location(self):
        """Gets the location of this System.  # noqa: E501


        :return: The location of this System.  # noqa: E501
        :rtype: int
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this System.


        :param location: The location of this System.  # noqa: E501
        :type: int
        """

        self._location = location

    @property
    def serviceprovider(self):
        """Gets the serviceprovider of this System.  # noqa: E501


        :return: The serviceprovider of this System.  # noqa: E501
        :rtype: int
        """
        return self._serviceprovider

    @serviceprovider.setter
    def serviceprovider(self, serviceprovider):
        """Sets the serviceprovider of this System.


        :param serviceprovider: The serviceprovider of this System.  # noqa: E501
        :type: int
        """

        self._serviceprovider = serviceprovider

    @property
    def contact(self):
        """Gets the contact of this System.  # noqa: E501


        :return: The contact of this System.  # noqa: E501
        :rtype: int
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this System.


        :param contact: The contact of this System.  # noqa: E501
        :type: int
        """

        self._contact = contact

    @property
    def tag(self):
        """Gets the tag of this System.  # noqa: E501


        :return: The tag of this System.  # noqa: E501
        :rtype: list[int]
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this System.


        :param tag: The tag of this System.  # noqa: E501
        :type: list[int]
        """

        self._tag = tag

    @property
    def case(self):
        """Gets the case of this System.  # noqa: E501


        :return: The case of this System.  # noqa: E501
        :rtype: list[int]
        """
        return self._case

    @case.setter
    def case(self, case):
        """Sets the case of this System.


        :param case: The case of this System.  # noqa: E501
        :type: list[int]
        """

        self._case = case

    @property
    def system_api_time(self):
        """Gets the system_api_time of this System.  # noqa: E501


        :return: The system_api_time of this System.  # noqa: E501
        :rtype: datetime
        """
        return self._system_api_time

    @system_api_time.setter
    def system_api_time(self, system_api_time):
        """Sets the system_api_time of this System.


        :param system_api_time: The system_api_time of this System.  # noqa: E501
        :type: datetime
        """

        self._system_api_time = system_api_time

    @property
    def system_create_time(self):
        """Gets the system_create_time of this System.  # noqa: E501


        :return: The system_create_time of this System.  # noqa: E501
        :rtype: datetime
        """
        return self._system_create_time

    @system_create_time.setter
    def system_create_time(self, system_create_time):
        """Sets the system_create_time of this System.


        :param system_create_time: The system_create_time of this System.  # noqa: E501
        :type: datetime
        """

        self._system_create_time = system_create_time

    @property
    def system_created_by_user_id(self):
        """Gets the system_created_by_user_id of this System.  # noqa: E501


        :return: The system_created_by_user_id of this System.  # noqa: E501
        :rtype: int
        """
        return self._system_created_by_user_id

    @system_created_by_user_id.setter
    def system_created_by_user_id(self, system_created_by_user_id):
        """Sets the system_created_by_user_id of this System.


        :param system_created_by_user_id: The system_created_by_user_id of this System.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and system_created_by_user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `system_created_by_user_id`, must not be `None`")  # noqa: E501

        self._system_created_by_user_id = system_created_by_user_id

    @property
    def system_modify_time(self):
        """Gets the system_modify_time of this System.  # noqa: E501


        :return: The system_modify_time of this System.  # noqa: E501
        :rtype: datetime
        """
        return self._system_modify_time

    @system_modify_time.setter
    def system_modify_time(self, system_modify_time):
        """Sets the system_modify_time of this System.


        :param system_modify_time: The system_modify_time of this System.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and system_modify_time is None:  # noqa: E501
            raise ValueError("Invalid value for `system_modify_time`, must not be `None`")  # noqa: E501

        self._system_modify_time = system_modify_time

    @property
    def system_modified_by_user_id(self):
        """Gets the system_modified_by_user_id of this System.  # noqa: E501


        :return: The system_modified_by_user_id of this System.  # noqa: E501
        :rtype: int
        """
        return self._system_modified_by_user_id

    @system_modified_by_user_id.setter
    def system_modified_by_user_id(self, system_modified_by_user_id):
        """Sets the system_modified_by_user_id of this System.


        :param system_modified_by_user_id: The system_modified_by_user_id of this System.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and system_modified_by_user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `system_modified_by_user_id`, must not be `None`")  # noqa: E501

        self._system_modified_by_user_id = system_modified_by_user_id

    @property
    def system_export_markdown(self):
        """Gets the system_export_markdown of this System.  # noqa: E501


        :return: The system_export_markdown of this System.  # noqa: E501
        :rtype: bool
        """
        return self._system_export_markdown

    @system_export_markdown.setter
    def system_export_markdown(self, system_export_markdown):
        """Sets the system_export_markdown of this System.


        :param system_export_markdown: The system_export_markdown of this System.  # noqa: E501
        :type: bool
        """

        self._system_export_markdown = system_export_markdown

    @property
    def system_export_spreadsheet(self):
        """Gets the system_export_spreadsheet of this System.  # noqa: E501


        :return: The system_export_spreadsheet of this System.  # noqa: E501
        :rtype: bool
        """
        return self._system_export_spreadsheet

    @system_export_spreadsheet.setter
    def system_export_spreadsheet(self, system_export_spreadsheet):
        """Sets the system_export_spreadsheet of this System.


        :param system_export_spreadsheet: The system_export_spreadsheet of this System.  # noqa: E501
        :type: bool
        """

        self._system_export_spreadsheet = system_export_spreadsheet

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, System):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, System):
            return True

        return self.to_dict() != other.to_dict()
