from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    """
    permission_classes = [DjangoModelPermissions]
    permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]
    permission_classes = [AllowAny]
    IsAdminUser makes only member with staff true to access the API
    AllowAny works according to name.
    IsAuthenticatedOrReadOnly gives access to only Authenticated User and also gives read only to everyone
    IsAutheticated gives access to only authenticated user.
    DjangoModelPermissions gives you abilty to set permissions manually accordingly.
    DjangoModelPermissionsOrAnonReadOnly works same as DjangoModelPermissions + gives readonly for Unautherized User.

    """  