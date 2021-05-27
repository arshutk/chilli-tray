from rest_framework import serializers

from hierarchy.models import AppModel


class AppModelSerializer(serializers.ModelSerializer):
    ''' Serializer for the AppModel, here we have used get_parent method defined on parent field to display the nested realtions'''    
    
    parent = serializers.SerializerMethodField()

    class Meta:
        model = AppModel
        fields = ('id', 'title', 'parent',)

    def get_parent(self, instance):
        if instance.parent is not None:
            return AppModelSerializer(instance.parent).data
        else:
            return None
