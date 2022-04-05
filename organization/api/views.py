from rest_framework.views import APIView
from rest_framework.response import Response
from organization.models import Employee, Team, Department, Designation
from organization.api.serializers import EmployeeSerializer, TeamSerializer, DesignationSerializer, DepartmentSerializer
from rest_framework import status


class EmployeeAV(APIView):
    def get(self, request):
        employee_list = Employee.objects.all()
        serializer = EmployeeSerializer(employee_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailAV(APIView):
    def get(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response({'error': 'Please check the URL'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        return Response("Deleted", status=status.HTTP_204_NO_CONTENT)

#
# class WatchListAV(APIView):
#     def get(self, request):
#         movie = WatchList.objects.all()
#         serializer = WatchListSerializer(movie, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = WatchListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class WatchDetailAV(APIView):
#     def get(self, request, pk):
#         try:
#             movie = WatchList.objects.get(pk=pk)
#             serializer = WatchListSerializer(movie)
#             return Response(serializer.data)
#         except WatchList.DoesNotExist:
#             return Response({'error': 'Not found'}, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk):
#         movie = WatchList.objects.get(pk=pk)
#         serializer = WatchListSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         movie = WatchList.objects.get(pk=pk)
#         movie.delete()
#         return Response("Deleted", status=status.HTTP_204_NO_CONTENT)
