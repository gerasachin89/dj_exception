import traceback
import sys

def get_request_object(request):
    #import ipdb; ipdb.set_trace()
    request_url = request.build_absolute_uri()
    request_method = request.method
    url_path = request.path
    context = {}
    context['request_url'] = request_url
    context['request_method'] = request_method
    context['url_path'] = url_path
    return context

def format_exception(exception):
    exception = exception[:-2]
    exception.extend(traceback.format_tb(sys.exc_info()[2]))
    exception.extend(traceback.format_exception_only(sys.exc_info()[0], sys.exc_info()[1]))
    exception_str = "Traceback (most recent call last):\n"
    exception_str += "".join(exception)
    # Removing the last \n
    exception_str = exception_str[:-1]
    return exception_str
