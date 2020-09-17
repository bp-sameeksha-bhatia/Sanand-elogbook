import json

from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render
from .models import *
from accounts.models import User
from django.db.models import Q
from .serializers import *
from rest_framework.decorators import action

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, id=None, email=None):
        if id:
            return self.retrieve(request, id)
        elif request.query_params.get('email'):
            return self.retrieve(request, request.query_params.get('email'))
        else:
            return self.list(request)

    @action(detail=False, methods=["GET"])
    def get_user(self, request):
        if request.query_params.get('email'):
            user = User.objects.get(email=request.query_params.get('email'))
            serialized_data = UserSerializer(user, many=False).data
            return Response(data=serialized_data, status=200)
        else:
            return Response(data="Assortment not found for customer", status=200)


class FormView(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    lookup_field = "id"

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    @action(detail=False, methods=["POST"])
    def get_associate_forms(self, request):
        user = User.objects.get(email=request.data.get('email'))
        all_scheduled_obj = Schedule.objects.filter(user=user)
        all_scheduled_forms = all_scheduled_obj.form.all()
        serialized_data = FormSerializer(all_scheduled_forms, many=True).data

        return Response(data=serialized_data, status=200)