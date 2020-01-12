from datetime import date

from rest_framework import serializers
from .models import *


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'capital']


# class CountryFormSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Country
#         fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']


class PersonSerializer(serializers.ModelSerializer):
    fullname = serializers.SerializerMethodField()
    company_name = serializers.SerializerMethodField()
    format_birthday = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = ['id', 'fullname', 'format_birthday', 'internal', 'company_name']

    def get_fullname(self, obj):
        return '%s %s' % (obj.first_name, obj.last_name)

    def get_company_name(self, obj):
        return obj.company.name

    def get_format_birthday(self, obj):
        return obj.birthday.strftime("%d.%m.%Y")


class PersonDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'birthday', 'internal', 'company']


class PersonValidationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name']


class TicketDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ['id', 'title', 'state', 'content', 'customer', 'contributor']


class TicketSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField()
    # state_name = serializers.SerializerMethodField()
    # actual_date = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = ['id', 'title', 'state', 'content', 'customer_name', 'contributor']

    def get_customer_name(self, obj):
        return obj.customer.name
