from django.contrib import admin

from .models import Order, Ticket, TicketType

admin.site.register([Order, Ticket, TicketType])
