from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from django.db.models import Q
from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filterset_fields = ["status", "owner"]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "updated_at", "status"]
    ordering = ["-created_at"]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return Post.objects.filter(status="approved")

        if user.role in ["moderator", "admin"]:
            return Post.objects.all()

        return Post.objects.filter(Q(status="approved") | Q(owner=user))
