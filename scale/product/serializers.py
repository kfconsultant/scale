"""Defines the serializers for products"""
from __future__ import unicode_literals

import rest_framework.fields as fields
import rest_framework.serializers as serializers

from batch.serializers import BatchBaseSerializerV6
from recipe.serializers import RecipeTypeBaseSerializerV6
from storage.serializers import ScaleFileSerializerV6
from util.rest import ModelIdSerializer


class ProductFileBaseSerializer(ScaleFileSerializerV6):
    """Converts product file model fields to REST output"""
    is_published = serializers.BooleanField()
    has_been_published = serializers.BooleanField()
    is_superseded = serializers.BooleanField()

    published = serializers.DateTimeField()
    unpublished = serializers.DateTimeField()
    superseded = serializers.DateTimeField()

    source_started = serializers.DateTimeField()
    source_ended = serializers.DateTimeField()

    job_type = ModelIdSerializer()
    job = ModelIdSerializer()
    job_exe = ModelIdSerializer()

    recipe_type = ModelIdSerializer()
    recipe = ModelIdSerializer()
    batch = ModelIdSerializer()


class ProductFileSerializer(ProductFileBaseSerializer):
    """Converts product file model fields to REST output"""
    from job.job_type_serializers import JobTypeBaseSerializerV6

    job_type = JobTypeBaseSerializerV6()
    batch = BatchBaseSerializerV6()
    recipe_type = RecipeTypeBaseSerializerV6()


class ProductFileDetailsSerializer(ProductFileSerializer):
    """Converts product file model fields to REST output"""
    pass


class ProductFileUpdateField(fields.Field):
    """Field for displaying the update information for a product file"""

    type_name = 'UpdateField'
    type_label = 'update'

    def to_representation(self, value):
        """Converts the model to its update information

        :param value: the product file model
        :type value: :class:`product.models.ProductFile`
        :rtype: dict
        :returns: the dict with the update information
        """

        if value.is_deleted:
            action = 'DELETED'
            when = value.deleted
        elif value.is_published:
            action = 'PUBLISHED'
            when = value.published
        else:
            action = 'UNPUBLISHED'
            when = value.unpublished

        return {'action': action, 'when': when}


class ProductFileUpdateSerializer(ProductFileSerializer):
    """Converts product file updates to REST output"""
    from source.serializers import SourceFileBaseSerializer

    update = ProductFileUpdateField(source='*')
    source_files = SourceFileBaseSerializer(many=True)
