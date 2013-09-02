from protorpc import remote, messages
from google.appengine.ext import endpoints

package = ''


class GetGreetingRequest(messages.Message):
  id = messages.IntegerField(1, variant=messages.Variant.INT32)


class HelloGreeting(messages.Message):
  message = messages.StringField(1)


@endpoints.api(name='helloworld', version='v1',
               description='Cloud Endpoints on non-default Module')
class GreetingsApi(remote.Service):
  @endpoints.method(GetGreetingRequest, HelloGreeting,
                    path='greetings/{id}', http_method='GET',
                    name='greetings.get')
  def GetGreeting(self, req):
    return greetings[req.id]


greetings = [
  HelloGreeting(message='hello world!'),
  HelloGreeting(message='goodbye world!')
]

app = endpoints.api_server([GreetingsApi], restricted=False)
