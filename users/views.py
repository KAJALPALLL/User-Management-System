from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer, UpdateUserSerializer
from django.db.models import Q
from django.shortcuts import get_object_or_404


class UserAPIView(APIView):
    # API View to handle CRUD operations for the User model.
    def get(self, request, pk=None):
        """ GET method
         is used to fetch user data"""
        if pk:
            user_data = get_object_or_404(User, pk=pk)
            serializer = UserSerializer(instance=user_data, many=False)
            return Response({"success": "1",
                             "message": "Users data fetched successfully",
                             "data": serializer.data}, status=status.HTTP_200_OK)
        else:

            name = request.GET.get('name')
            sort = request.GET.get('sort')
            page = int(request.GET.get('page', 1))
            limit = int(request.GET.get('limit', 5))
            users = User.objects.all()
            # Applying filtering if the name is passed in endpoint
            if name:
                users = users.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
            # Applying ordering if the sort field is passed in endpoint
            if sort:
                users = users.order_by(sort)
            # Show data according to the page and limit
            start = (page - 1) * limit
            end = start + limit
            paginated_users = users[start:end]
            serializer = UserSerializer(paginated_users, many=True)
            return Response({
                "success": "1",
                "message": "Users list fetched successfully",
                "total": users.count(),
                "data": serializer.data
            }, status=status.HTTP_200_OK)

    def post(self, request):
        """ POST method
            is used to add user """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "1",
                             "message": "User added successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"success": "0",
                             "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ PUT method
        is used to update the user data of some specific fields """
        if pk:
            user_data = get_object_or_404(User, pk=pk)
            serializer = UpdateUserSerializer(instance=user_data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"success": "1",
                                 "message": "User data update successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"success": "0",
                                 "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """DELETE method
            is used to delete the user """
        user_data = get_object_or_404(User, pk=pk)
        if user_data:
            user_data.delete()
            return Response({"success": "1", "message":"User deleted successfully"}, status=status.HTTP_200_OK)
