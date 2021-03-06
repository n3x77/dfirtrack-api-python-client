# coding: utf-8

"""
    DFIRTrack

    OpenAPI 3 - Documentation of DFIRTrack API  # noqa: E501

    The version of the OpenAPI document: 0.4.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import dfirtrackapi_client
from dfirtrackapi_client.models.reason import Reason  # noqa: E501
from dfirtrackapi_client.rest import ApiException

class TestReason(unittest.TestCase):
    """Reason unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Reason
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dfirtrackapi_client.models.reason.Reason()  # noqa: E501
        if include_optional :
            return Reason(
                reason_id = 56, 
                reason_name = '0'
            )
        else :
            return Reason(
                reason_name = '0',
        )

    def testReason(self):
        """Test Reason"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
