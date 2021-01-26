from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from .models import Hint, Assignment
from .serializers import HintSerializer, AssignmentSerializer
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

import logging
logger = logging.getLogger('django')


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def assignment_list(request):
    """
    List all assignment or create a new entry.
    """
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 10
        query_result = Assignment.objects.all()
        paginated_query_result = paginator.paginate_queryset(query_result, request)
        serializer = AssignmentSerializer(paginated_query_result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK )

    if request.method == 'POST':
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def assignment_details(request,pk):
    """
    Get, update or delete assignment item
    """
    try:
        item = Assignment.objects.get(pk=pk)
    except Assignment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AssignmentSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = AssignmentSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def hint_list(request):
    """
    List all hints or create a new entry.
    """
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 10
        query_result = Hint.objects.all()

        filter_params = Q()
        if 'description' in request.GET:
            filter_params &= Q(description__icontains=request.GET['description'])
        if 'lte' in request.GET:
            filter_params &= Q(created__lte=request.GET['lte'])
        if 'gte' in request.GET:
            filter_params &= Q(created__gte=request.GET['gte'])
        filtered_result = query_result.filter(filter_params)

        paginated_query_result = paginator.paginate_queryset(filtered_result, request)
        serializer = HintSerializer(paginated_query_result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK )

    if request.method == 'POST':
        serializer = HintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def hint_details(request,pk):
    """
    Get, update or delete assignment item
    """
    try:
        item = Hint.objects.get(pk=pk)
    except Hint.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HintSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = HintSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)