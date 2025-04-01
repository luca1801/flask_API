from .namespace import ns as employers_ns

# from .employer_views import EmployerList


def init_api(api):
    """Register all API resources"""
    # api.add_resource(EmployerList, '/')
    api.add_namespace(employers_ns)
