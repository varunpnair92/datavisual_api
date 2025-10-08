from rest_framework import serializers
from .models import Dataset, Entity, Detail


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ["id", "entity", "details"]


class EntitySerializer(serializers.ModelSerializer):
    details = DetailSerializer(many=True, read_only=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Entity
        fields = ["id", "dataset", "name", "volume",
                  "image", "image_url", "details"]
        extra_kwargs = {
            # accept upload but don’t show raw field in output
            "image": {"write_only": True},
        }

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image and hasattr(obj.image, "url"):
            url_path = obj.image.url
            fixed_path = "/data" + url_path  # optional prefix if needed
            if request:
                return request.build_absolute_uri(fixed_path)
            return fixed_path
        return None


class DatasetSerializer(serializers.ModelSerializer):
    entities = serializers.SerializerMethodField()  # use method to sort

    class Meta:
        model = Dataset
        fields = ["id", "heading", "category", "data", "sort_by", "entities"]

    def get_entities(self, obj):
        # Always fetch a fresh queryset from the DB, sorted by volume
        queryset = Entity.objects.filter(dataset=obj).order_by("volume")
        return EntitySerializer(queryset, many=True, context=self.context).data


