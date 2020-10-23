from djtest.tracing import init_tracing

def post_fork(server, worker):
    init_tracing()
