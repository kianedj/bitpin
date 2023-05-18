from django.db.models import Avg
from rest_framework import serializers
from .models import Post, Upvote


class UpvoteSerializer(serializers.ModelSerializer):
    points = serializers.IntegerField(min_value=0, max_value=5)

    class Meta:
        model = Upvote
        fields = ("user", "post", "points", "created_at")


class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    upvotes = UpvoteSerializer(many=True, read_only=True)
    upvote_count = serializers.IntegerField(source='upvotes.count', read_only=True)
    avg_upvote = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'created', 'updated', 'user', 'upvote_count', 'avg_upvote', 'upvotes')
        read_only_fields = ('upvote_count', 'avg_upvote')

    def get_avg_upvote(self, instance):
        aggrigate_value = Upvote.objects.filter(post=instance).aggregate(Avg("points"))['points__avg']
        return aggrigate_value
