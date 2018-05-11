"""Defines the classes for representing a connection between two interface parameters within a recipe definition"""
from __future__ import unicode_literals

from abc import ABCMeta, abstractmethod


class NodeConnection(object):
    """Abstract base class that represents a connection between two interface parameters
    """

    __metaclass__ = ABCMeta

    def __init__(self, input_name):
        """Constructor

        :param input_name: The name of the node's input
        :type input_name: string
        """

        self.input_name = input_name

    @abstractmethod
    def add_parameter_to_interface(self, interface, recipe_input_interface, node_output_interfaces):
        """Adds the parameter for this connection to the interface

        :param interface: The interface to add the parameter to
        :type interface: :class:`data.interface.interface.Interface`
        :param recipe_input_interface: The interface for the recipe input
        :type recipe_input_interface: :class:`data.interface.interface.Interface`
        :param node_output_interfaces: The output interface for each node stored by node name
        :type node_output_interfaces: dict
        :returns: A list of warnings discovered during validation
        :rtype: list

        :raises :class:`recipe.definition.exceptions.InvalidDefinition`: If the definition is invalid
        """

        raise NotImplementedError()

    # TODO: raise exception for invalid data
    @abstractmethod
    def add_argument_to_data(self, data, recipe_input, node_output):
        """Adds the parameter for this connection to the interface

        :param data: The data to add the argument to
        :type data: :class:`data.data.data.Data`
        :param recipe_input: The recipe input data
        :type recipe_input: :class:`data.data.data.Data`
        :param node_output: The output data for each node stored by node name
        :type node_output: dict
        :returns: A list of warnings discovered during validation
        :rtype: list
        """

        raise NotImplementedError()
