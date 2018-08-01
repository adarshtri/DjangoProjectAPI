from rest_framework.serializers import ModelSerializer
from .models import Campaign


class CampaignSerializer(ModelSerializer):

    class Meta:
        model = Campaign
        fields = ('campaign_id', 'campaign_name', 'description', 'start_at', 'end_at', 'created_by',
                  'created_at', 'updated_at')
