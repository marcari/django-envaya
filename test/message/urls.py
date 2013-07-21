try:
    from django.conf.urls import patterns, include, url
except ImportError:
    from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('message.views',
    url(
          r'^receive_incoming/$'
        , 'receive_incoming'
        , name='receive_incoming'
    ),
    url(
          r'^receive_outgoing/$'
        , 'receive_outgoing'
        , name='receive_outgoing'
    ),
    url(
          r'^receive_send_status/$'
        , 'receive_send_status'
        , name='receive_send_status'
    ),
)