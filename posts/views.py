from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import *
from .serializers import *


class PostView(APIView):
    def get(self, request):
        print('path: ' + str(request.path))
        path = request.path

        if path == '/api/home/':
            data = []
            next_page = 1
            previous_page = 1
            posts = Post.objects.filter(sport='general')

            page = request.GET.get('page', 1)
            paginator = Paginator(posts, 2)
            try:
                data = paginator.page(page)
            except PageNotAnInteger:
                data = paginator.page(1)
            except EmptyPage:
                data = paginator.page(paginator.num_pages)

            serializer = EventSerializer(data, context={'request': request}, many=True)

            if data.has_next():
                next_page = data.next_page_number()
            if data.has_previous():
                previous_page = data.previous_page_number()

            return Response({'posts': serializer.data, 'count': paginator.count, 'numpages': paginator.num_pages,
                             'nextlink': '/api/home/?page=' + str(next_page),
                             'prevlink': '/api/home/?page=' + str(previous_page)})

        elif path == '/api/football/news/':
            posts = Post.objects.filter(sport='football')
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data)
        else:
            return Response({'detail': "Your error message"}, status=status.HTTP_400_BAD_REQUEST)
            # return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CurrentPostView(APIView):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = CurrentPostSerializer(post)
        return Response(serializer.data)


class EventView(APIView):
    def get(self, request):
        active_events = Event.objects.filter(status='active').order_by('-id')[0:6]
        upcoming_events = Event.objects.filter(status='upcoming').order_by('-id')[0:6]
        past_events = Event.objects.filter(status='past').order_by('-id')[0:6]
        events = active_events.union(upcoming_events, past_events)
        print(events)
        serializer = EventSerializer(events, many=True)
        print(serializer.data)
        return Response(serializer.data)


class CurrentEventView(APIView):
    def get(self, request, pk):
        event = Event.objects.get(id=pk)
        serializer = CurrentEventSerializer(event)
        return Response(serializer.data)


class CurrentSportEventView(APIView):
    def get(self, request):
        data = []
        next_page = 1
        previous_page = 1
        print(request.path)

        if request.path == '/api/football/events/active':
            events = Event.objects.filter(status='active')
            sport = 'football'
        elif request.path == '/api/football/events/upcoming':
            events = Event.objects.filter(status='upcoming')
            sport = 'football'
        elif request.path == '/api/football/events/past':
            events = Event.objects.filter(status='past')
            sport = 'football'

        elif request.path == '/api/volleyball/events/active':
            events = Event.objects.filter(status='active')
            sport = 'volleyball'
        elif request.path == '/api/volleyball/events/upcoming':
            events = Event.objects.filter(status='upcoming')
            sport = 'volleyball'
        elif request.path == '/api/volleyball/events/past':
            events = Event.objects.filter(status='past')
            sport = 'volleyball'

        else:
            print('ALARM ALARM ALARM ALARM ALARM ALARM ALARM ALARM ALARM ALARM ALARM')

        page = request.GET.get('page', 1)
        paginator = Paginator(events, 2)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = EventSerializer(data, context={'request': request}, many=True)

        if data.has_next():
            next_page = data.next_page_number()
        if data.has_previous():
            previous_page = data.previous_page_number()

        return Response({'posts': serializer.data, 'count': paginator.count, 'numpages': paginator.num_pages,
                         'nextlink': '/api/' + sport + '/?page=' + str(next_page),
                         'prevlink': '/api/' + sport + '/?page=' + str(previous_page)})
