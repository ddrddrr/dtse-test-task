from rest_framework import serializers


# Other checks should probably be added based on the domain knowledge/dataset analysis
class PredictHousePriceSerializer(serializers.Serializer):
    longitude = serializers.FloatField(
        min_value=-180,
        max_value=180,
    )
    latitude = serializers.FloatField(
        min_value=-90,
        max_value=90,
    )
    housing_median_age = serializers.IntegerField(
        min_value=0,
    )
    total_rooms = serializers.IntegerField(min_value=1)
    total_bedrooms = serializers.IntegerField(min_value=0)
    population = serializers.IntegerField(min_value=0)
    households = serializers.IntegerField(min_value=0)
    median_income = serializers.FloatField(min_value=0)
    ocean_proximity = serializers.ChoiceField(
        choices=["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"],
    )

    def validate(self, data):
        if data["total_rooms"] < data["total_bedrooms"]:
            raise serializers.ValidationError(
                "`total_rooms` must be greater than `total_bedrooms`"
            )
        return data
