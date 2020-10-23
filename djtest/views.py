from opentelemetry import trace
from django.http import HttpResponse

# this breaks tracing as initialized in wsgi.py
# moving this call to inside the view function fixes it.
tracer = trace.get_tracer(__name__)

def hello(request):
  #tracer = trace.get_tracer(__name__)
  with tracer.start_as_current_span("foo"):
    return HttpResponse("Hello World")