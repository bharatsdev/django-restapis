from rest_framework import serializers

from profile_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serialize a new user profile"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

    def create(self, validated_data):
        """Create a user profile """

        user = models.UserProfile.objects.create_user(
            email=validated_data.get('email'),
            name=validated_data.get('name'),
            password=validated_data.get('password'),
        )

        return user
