from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Post(models.Model):
    header = models.CharField("Header", max_length=50, blank=True)
    shortDescription = models.CharField("Short description", max_length=255, blank=True)
    fullDescription = models.TextField("Full description", blank=True)

    general = 'general'
    football = 'football'
    sport_choices = [(general, 'general'),
                     (football, 'football')]
    sport = models.CharField('Status', choices=sport_choices, default='general', max_length=255)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.header


class Event(models.Model):
    header = models.CharField("Header", max_length=50, blank=True)
    shortDescription = models.CharField("Short description", max_length=255, blank=True)
    fullDescription = models.TextField("Full description", blank=True)

    football = 'football'
    sport_choices = [(football, 'football')]
    sport = models.CharField('Status', choices=sport_choices, default='football', max_length=255)

    active = 'active'
    upcoming = 'upcoming'
    past = 'past'
    status_choices = [(active, 'active'), (upcoming, 'upcoming'),
                      (past, 'past')]
    status = models.CharField('Status', choices=status_choices, default='upcoming', max_length=255)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        # abstract = True

    def __str__(self):
        return self.header


# class FootballEvent(Event):
#     sport = 'football'
#
#
# class VolleyballEvent(Event):
#     sport = 'volleyball'
