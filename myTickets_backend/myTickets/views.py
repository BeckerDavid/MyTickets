from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import *
from .serializers import *


# Create your views here.

@swagger_auto_schema(method='GET', responses={200: CountrySerializer(many=True)})
@api_view(['GET'])
# @permission_required('myTickets.view_country', raise_exception=True)
def country_list(request):
    countries = Country.objects.all()
    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', responses={200: CountrySerializer(many=True)})
@api_view(['GET'])
# @permission_required('myTickets.view_country', raise_exception=True)
def country_get(request, pk):
    try:
        country = Country.objects.get(pk=pk)
    except country.DoesNotExist:
        return Response({'error': 'Country does not exist.'}, status=404)
    serializer = CountrySerializer(country)
    return Response(serializer.data)


@swagger_auto_schema(method='POST', request_body=CountrySerializer, responses={200: CountrySerializer(many=True)})
@api_view(['POST'])
# @permission_required('myTickets.view_country', raise_exception=True)
def country_create(request):
    data = JSONParser().parse(request)
    serializer = CountrySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.error, status=400)


@swagger_auto_schema(method='PUT', request_body=CountrySerializer, responses={200, CountrySerializer()})
@api_view(['PUT'])
# @permission_required('myTickets.change_country', raise_exception=True)
def country_update(request, pk):
    try:
        country = Country.objects.get(pk=pk)
    except country.DoesNotExist:
        return Response({'error': 'Country does not exist.'}, status=404)

    data = JSONParser().parse(request)
    serializer = CountrySerializer(country, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
# @permission_required('myTickets.delete_country', raise_exception=True)
def country_delete(request, pk):
    try:
        country = Country.objects.get(pk=pk)
    except Country.DoesNotExist:
        return Response({'error': 'Country does not exist.'}, status=404)
    country.delete()
    return Response(status=204)


@swagger_auto_schema(method='GET', responses={200: CompanySerializer(many=True)})
@api_view(['GET'])
# @permission_required('myTickets.view_company', raise_exception=True)
def company_list(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', responses={200: CompanySerializer(many=True)})
@api_view(['GET'])
# @permission_required('myTickets.view_company', raise_exception=True)
def company_get(request, pk):
    try:
        company = Company.objects.get(pk=pk)
    except company.DoesNotExist:
        return Response({'error': 'Company does not exist.'}, status=404)
    serializer = CompanySerializer(company)
    return Response(serializer.data)


@swagger_auto_schema(method='POST', request_body=CompanySerializer, responses={200: CompanySerializer(many=True)})
@api_view(['POST'])
# @permission_required('myTickets.create_company', raise_exception=True)
def company_create(request):
    serializer = CompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.error, status=400)


@swagger_auto_schema(method='PUT', request_body=CompanySerializer, responses={200, CompanySerializer()})
@api_view(['PUT'])
# @permission_required('myTickets.change_company', raise_exception=True)
def company_update(request, pk):
    try:
        company = Company.objects.get(pk=pk)
    except company.DoesNotExist:
        return Response({'error': 'Company does not exist.'}, status=404)

    data = JSONParser().parse(request)
    serializer = CompanySerializer(company, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)



@api_view(['DELETE'])
# @permission_required('myTickets.delete_company', raise_exception=True)
def company_delete(request, pk):
    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return Response({'error': 'Company does not exist.'}, status=404)
    company.delete()
    return Response(status=204)


@swagger_auto_schema(method='GET', responses={200: PersonSerializer(many=True)})
@api_view(['GET'])
# @permission_required('myTickets.view_person', raise_exception=True)
def person_list(request):
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', responses={200: PersonDetailSerializer(many=True)})
@api_view(['GET'])
# @permission_required('myTickets.view_person', raise_exception=True)
def person_get(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except person.DoesNotExist:
        return Response({'error': 'Person does not exist.'}, status=404)
    serializer = PersonDetailSerializer(person)
    return Response(serializer.data)


@swagger_auto_schema(method='POST', request_body=PersonDetailSerializer, responses={200: PersonDetailSerializer(many=True)})
@api_view(['POST'])
# @permission_required('myTickets.create_person', raise_exception=True)
def person_create(request):
    serializer = PersonDetailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.error, status=400)


@swagger_auto_schema(method='PUT', request_body=PersonDetailSerializer, responses={200, PersonDetailSerializer()})
@api_view(['PUT'])
# @permission_required('myTickets.change_person', raise_exception=True)
def person_update(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except person.DoesNotExist:
        return Response({'error': 'Person does not exist.'}, status=404)

    data = JSONParser().parse(request)
    serializer = PersonDetailSerializer(person, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
# @permission_required('myTickets.delete_person', raise_exception=True)
def person_delete(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response({'error': 'Company does not exist.'}, status=404)
    person.delete()
    return Response(status=204)


@swagger_auto_schema(method='GET', responses={200: TicketSerializer(many=True)})
@api_view(['GET'])
# @permission_required('myTickets.view_ticket', raise_exception=True)
def ticket_list(request):
    tickets = Ticket.objects.all()
    serializer = TicketSerializer(tickets, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', responses={200: TicketDetailSerializer(many=True)})
@api_view(['GET'])
# @permission_required('myTickets.view_ticket', raise_exception=True)
def ticket_get(request, pk):
    try:
        ticket = Ticket.objects.get(pk=pk)
    except ticket.DoesNotExist:
        return Response({'error': 'Ticket does not exist.'}, status=404)
    serializer = TicketDetailSerializer(ticket)
    return Response(serializer.data)


@swagger_auto_schema(method='POST', request_body=TicketDetailSerializer, responses={200: TicketDetailSerializer(many=True)})
@api_view(['POST'])
# @permission_required('myTickets.create_ticket', raise_exception=True)
def ticket_create(request):
    serializer = TicketDetailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.error, status=400)


@swagger_auto_schema(method='PUT', request_body=TicketDetailSerializer, responses={200, TicketDetailSerializer()})
@api_view(['PUT'])
# @permission_required('myTickets.change_ticket', raise_exception=True)
def ticket_update(request, pk):
    try:
        ticket = Ticket.objects.get(pk=pk)
    except ticket.DoesNotExist:
        return Response({'error': 'Ticket does not exist.'}, status=404)

    data = JSONParser().parse(request)
    serializer = TicketDetailSerializer(ticket, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
# @permission_required('myTickets.delete_ticket', raise_exception=True)
def ticket_delete(request, pk):
    try:
        ticket = Ticket.objects.get(pk=pk)
    except Ticket.DoesNotExist:
        return Response({'error': 'Company does not exist.'}, status=404)
    ticket.delete()
    return Response(status=204)


@swagger_auto_schema(method='GET', responses={200: PersonValidationSerializer(many=True)})
@api_view(['GET'])
# @permission_required('myTickets.view_person', raise_exception=True)
def personal_validate(request, firstname, lastname):
    person = Person.objects.filter(first_name__iexact=firstname, last_name__iexact=lastname)
    serializer = PersonValidationSerializer(person, many=True)
    return Response(serializer.data)