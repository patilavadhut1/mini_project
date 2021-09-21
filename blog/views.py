from django.shortcuts import render
import rest_framework
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login,logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def signup(request):
    data=JSONParser().parse(request)
    username=data['username']
    password1=data['password1']
    password2=data['password2']
    email=data['email']
    first_name=data['first_name']
    last_name=data['last_name']

    if password1 != password2:
        return Response({'message':'Please enter a correct password.'})
    
    user = User.objects.create_user(username, email, password1)
    user.first_name=first_name
    user.last_name=last_name
    user.save()

    return Response({'messsage':f'{user.username} created successfully.'})

class Login(APIView):

    def post(self, request):
        data = JSONParser().parse(request)
        username = data['username']
        password = data['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            login(request, user)
            return Response({"meassage": " Successfully Logged In.",'refresh_token': str(refresh),
             'access_token': str(refresh.access_token)})
        else:
            return Response({"meassage": " Invalid Crediantials."})

def logout_view(request):
    logout(request)

class ListBlog(ListAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

class RetriveBlog(RetrieveAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

class CreateBlog(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
            data = JSONParser().parse(request)
            title = data['title']
            content = data['content']

            blog = Blog.objects.create(
                title=title, content=content,created_by=request.user)

            return Response({'message': 'Blog created successfully.'})

    def put(self, request):
        data = JSONParser().parse(request)
        title = data['title']
        content = data['content']
        id=data['id']
        blog = Blog.objects.get(pk=id)
        if title:
            blog.title = title
        if content:
            blog.content = content
        blog.save()
        return Response({'message': 'Blog Updated successfully.'})



class DestroyView(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
