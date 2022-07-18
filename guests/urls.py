from django.urls import path

from guests.views import GuestListView, test_email, save_the_date_preview, save_the_date_random, export_guests, \
    invitation, invitation_email_preview, invitation_email_test, rsvp_confirm, dashboard

urlpatterns = [
    path(r'^guests/$', GuestListView.as_view(), name='guest-list'),
    path(r'^dashboard/$', dashboard, name='dashboard'),
    path(r'^guests/export$', export_guests, name='export-guest-list'),
    path(r'^invite/(?P<invite_id>[\w-]+)/$', invitation, name='invitation'),
    path(r'^invite-email/(?P<invite_id>[\w-]+)/$', invitation_email_preview, name='invitation-email'),
    path(r'^invite-email-test/(?P<invite_id>[\w-]+)/$', invitation_email_test, name='invitation-email-test'),
    path(r'^save-the-date/$', save_the_date_random, name='save-the-date-random'),
    path(r'^save-the-date/(?P<template_id>[\w-]+)/$', save_the_date_preview, name='save-the-date'),
    path(r'^email-test/(?P<template_id>[\w-]+)/$', test_email, name='test-email'),
    path(r'^rsvp/confirm/(?P<invite_id>[\w-]+)/$', rsvp_confirm, name='rsvp-confirm'),
]
