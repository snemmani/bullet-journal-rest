# from rest_framework.views import APIView
# from rest_framework.response import Response
# from journal.serializers import TaskSerializer
# from journal.models import Task
# from journal.serializers import NoteSerializer
# from journal.models import Note
# from journal.serializers import EventSerializer
# from journal.models import Event
# from django.utils import timezone
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi

# year_param = openapi.Parameter('year', openapi.IN_QUERY, description="Year of the date", type=openapi.TYPE_INTEGER)
# month_param = openapi.Parameter('month', openapi.IN_QUERY, description="Month of the date", type=openapi.TYPE_INTEGER)
# day_param = openapi.Parameter('day', openapi.IN_QUERY, description="Day of the date", type=openapi.TYPE_INTEGER)


# class MonthView(APIView):
#     """
#     A view to get the list of tasks, events and Notes in a month
#     """
#     def get(self, request, pk):
#         response = dict()
#         tasks = Task.objects.filter(due_date__month=pk)
#         response['tasks'] = TaskSerializer(tasks, many=True).data
#         events = Event.objects.filter(date__month=pk)
#         response['events'] = EventSerializer(events, many=True).data
#         notes = Note.objects.filter(date__month=pk)
#         response['notes'] = NoteSerializer(notes, many=True).data
#         return Response(response)


# class DayView(APIView):
#     """
#     A view to get the list of tasks, events and Notes in a month
#     """

#     @swagger_auto_schema(manual_parameters=[year_param, month_param, day_param])
#     def get(self, request):
#         sysdate = timezone.now()
#         year = request.GET.get('year', sysdate.year)
#         month = request.GET.get('month', sysdate.month)
#         day = request.GET.get('day', sysdate.day)
#         response = dict()
#         tasks = Task.objects.filter(due_date__year=year, due_date__month=month, due_date__day=day)
#         response['tasks'] = TaskSerializer(tasks, many=True).data
#         events = Event.objects.filter(date__year=year, date__month=month, date__day=day)
#         response['events'] = EventSerializer(events, many=True).data
#         notes = Note.objects.filter(date__year=year, date__month=month, date__day=day)
#         response['notes'] = NoteSerializer(notes, many=True).data
#         return Response(response)
