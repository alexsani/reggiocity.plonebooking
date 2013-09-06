    # -*- coding: utf-8 -*-
from zope.interface import Interface
from five import grok
from Products.PloneBooking.interfaces import IBookingCenter
import json
from zope.component import getMultiAdapter

# Search for templates in the 'templates' directory
grok.templatedir('templates')


class BookingCenterView(grok.View):
    """ Render the title and description of item only (example)
    """

    # The view is available on every content item type
    grok.context(IBookingCenter)
    grok.name("bookingcenter_view")
    grok.template("bookingcenter_view")
    grok.require("zope2.Public")
    
    def getSetupJavascript(self):
        """
        Set some global helpers
        """
        defaultCalendarView = {
            'day': 'agendaDay',
            'week': 'agendaWeek',
            'month': 'month'
        }
        
        calendarStartingHour = self.context.getCalendarStartingHour()
        calendarEndingHour = self.context.getCalendarEndingHour()
        defaultCalendarView = defaultCalendarView[self.context.getDefaultCalendarView()] #day, week, month
        return u""" <script type="text/javascript" class="javascript-settings">
                        var calendarStartingHour = %s;
                        var calendarEndingHour = %s;
                        var defaultCalendarView = '%s';
                        var events = new Array();
                    </script>""" %(calendarStartingHour, calendarEndingHour, defaultCalendarView)
                    