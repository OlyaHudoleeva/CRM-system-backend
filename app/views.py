from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from app.models import Company
from app.serializers import CompanySerializer


class CompanyViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     GenericViewSet):
    """
    The following endpoints are fully provided by mixins:
    * List view
    * Create view
    * Retrieve view
    * Update view
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    # permission_classes = (permissions.IsAuthenticated,)
