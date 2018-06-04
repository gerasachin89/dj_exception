from djbugger.models import ExceptionsHistory
from djbugger.utils import get_request_object, format_exception
import traceback
import sys
import datetime

class ExceptionGettingMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        request_detail = get_request_object(request)
        exception_name = traceback.format_exception_only(sys.exc_info()[0], sys.exc_info()[1])
        exception_detail = format_exception(traceback.format_stack())
        user = request.user
        if request.user.is_authenticated():
            user = request.user
        else:
            user = None
        try:
            exception = ExceptionsHistory.objects.get(exception=exception_name, request_url = request_detail['request_url'],request_method = request_detail['request_method'],url_path = request_detail['url_path'])
            exception.updated = datetime.datetime.now()
        except ExceptionsHistory.DoesNotExist:
            exception = ExceptionsHistory.objects.create(exception=exception_name,
                                                        detail = exception_detail,
                                                        user = user,
                                                        created = datetime.datetime.now(),
                                                        status = "Pending",
                                                        request_url = request_detail['request_url'],
                                                        request_method = request_detail['request_method'],
                                                        url_path = request_detail['url_path']
                                                        )
            exception.exception_id = "BUG"+str(exception.id)
            exception.save()
