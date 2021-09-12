from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, logout, login
from .models import Share
from django.contrib.auth.models import User
from .serializers import ShareSerializer, UserSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ShareList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        shares = Share.objects.all()
        serializer = ShareSerializer(shares, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShareSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShareDetails(APIView):
    def get_object(self, id):
        try:
            return Share.objects.get(id=id)
        except Share.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        shares = self.get_object(id)
        serializer = ShareSerializer(shares)
        return Response(serializer.data)

    def put(self, request, id):
        share = self.get_object(id)
        serializer = ShareSerializer(share, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        share = self.get_object(id)
        share.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)



'''
class ShareList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):

    queryset = Share.objects.all()
    serializer_class = ShareSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class ShareDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    queryset = Share.objects.all()
    serializer_class = ShareSerializer

    lookup_field = 'id'
    def get(self, request, id):
        return self.retrieve(request, id=id)

    def put(self, request, id):
        return self.update(request, id=id)

    def delete(self, request, id):
        return self.destroy(request, id=id)

'''

'''
@api_view(['GET','POST'])
def share(request):
    if request.method == 'GET':
        shares = Share.objects.all()
        serializer = ShareSerializer(shares, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ShareSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def share_details(request, pk):
    try:
        share = Share.objects.get(pk=pk)
    except Share.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = ShareSerializer(share)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ShareSerializer(share, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        share.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
'''

'''
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('/login')'''
