from django.conf import settings
from django_hosts import patterns, host

# Routing for subdomains and root routing for main domain.
host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),  # <-- The `name` we used to in the `DEFAULT_HOST` setting
    host(r'api', 'textsum.urls.api', name='api')   # Routing for the api subdomain
)
