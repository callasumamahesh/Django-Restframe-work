from rest_framework import viewsets
from .models import UserData
from .serializers import UserDataSerializer

class UserDataViewSet(viewsets.ModelViewSet):     # ⭐ important
    queryset = UserData.objects.all()             # All records
    serializer_class = UserDataSerializer         # Serializer we created
