"""
    DFIRTrack

    OpenAPI 3 - Documentation of DFIRTrack API  # noqa: E501

    The version of the OpenAPI document: v0.4.7
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from dfirtrackapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)


class Artifact(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('artifact_name',): {
            'max_length': 4096,
        },
        ('artifact_md5',): {
            'max_length': 32,
        },
        ('artifact_sha1',): {
            'max_length': 40,
        },
        ('artifact_sha256',): {
            'max_length': 64,
        },
        ('artifact_source_path',): {
            'max_length': 4096,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'artifact_name': (str,),  # noqa: E501
            'artifacttype': (int,),  # noqa: E501
            'system': (int,),  # noqa: E501
            'artifact_created_by_user_id': (int,),  # noqa: E501
            'artifact_modified_by_user_id': (int,),  # noqa: E501
            'artifact_id': (int,),  # noqa: E501
            'artifact_uuid': (str,),  # noqa: E501
            'artifactstatus': (int,),  # noqa: E501
            'case': (int, none_type,),  # noqa: E501
            'artifact_md5': (str, none_type,),  # noqa: E501
            'artifact_sha1': (str, none_type,),  # noqa: E501
            'artifact_sha256': (str, none_type,),  # noqa: E501
            'artifact_source_path': (str, none_type,),  # noqa: E501
            'artifact_storage_path': (str,),  # noqa: E501
            'artifact_acquisition_time': (datetime, none_type,),  # noqa: E501
            'artifact_requested_time': (datetime, none_type,),  # noqa: E501
            'artifact_create_time': (datetime,),  # noqa: E501
            'artifact_modify_time': (datetime,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'artifact_name': 'artifact_name',  # noqa: E501
        'artifacttype': 'artifacttype',  # noqa: E501
        'system': 'system',  # noqa: E501
        'artifact_created_by_user_id': 'artifact_created_by_user_id',  # noqa: E501
        'artifact_modified_by_user_id': 'artifact_modified_by_user_id',  # noqa: E501
        'artifact_id': 'artifact_id',  # noqa: E501
        'artifact_uuid': 'artifact_uuid',  # noqa: E501
        'artifactstatus': 'artifactstatus',  # noqa: E501
        'case': 'case',  # noqa: E501
        'artifact_md5': 'artifact_md5',  # noqa: E501
        'artifact_sha1': 'artifact_sha1',  # noqa: E501
        'artifact_sha256': 'artifact_sha256',  # noqa: E501
        'artifact_source_path': 'artifact_source_path',  # noqa: E501
        'artifact_storage_path': 'artifact_storage_path',  # noqa: E501
        'artifact_acquisition_time': 'artifact_acquisition_time',  # noqa: E501
        'artifact_requested_time': 'artifact_requested_time',  # noqa: E501
        'artifact_create_time': 'artifact_create_time',  # noqa: E501
        'artifact_modify_time': 'artifact_modify_time',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, artifact_name, artifacttype, system, artifact_created_by_user_id, artifact_modified_by_user_id, *args, **kwargs):  # noqa: E501
        """Artifact - a model defined in OpenAPI

        Args:
            artifact_name (str):
            artifacttype (int):
            system (int):
            artifact_created_by_user_id (int):
            artifact_modified_by_user_id (int):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            artifact_id (int): [optional]  # noqa: E501
            artifact_uuid (str): [optional]  # noqa: E501
            artifactstatus (int): [optional]  # noqa: E501
            case (int, none_type): [optional]  # noqa: E501
            artifact_md5 (str, none_type): [optional]  # noqa: E501
            artifact_sha1 (str, none_type): [optional]  # noqa: E501
            artifact_sha256 (str, none_type): [optional]  # noqa: E501
            artifact_source_path (str, none_type): [optional]  # noqa: E501
            artifact_storage_path (str): [optional]  # noqa: E501
            artifact_acquisition_time (datetime, none_type): [optional]  # noqa: E501
            artifact_requested_time (datetime, none_type): [optional]  # noqa: E501
            artifact_create_time (datetime): [optional]  # noqa: E501
            artifact_modify_time (datetime): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.artifact_name = artifact_name
        self.artifacttype = artifacttype
        self.system = system
        self.artifact_created_by_user_id = artifact_created_by_user_id
        self.artifact_modified_by_user_id = artifact_modified_by_user_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
