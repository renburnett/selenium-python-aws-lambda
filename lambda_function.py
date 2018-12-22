
from kexp_crawler import recent_songs
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard

class LaunchRequestHandler(AbstractRequestHandler):
     def can_handle(self, handler_input):
         # type: (HandlerInput) -> bool
         return is_request_type("LaunchRequest")(handler_input)

     def handle(self, handler_input):
         # type: (HandlerInput) -> Response
         speech_text = "Welcome! I can tell you the song that's currently playing on Kay-Ee-Ex-Pea or I can tell you the last few songs played!"

         handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Would you like to hear the recent songs on Kay-Ee-Ex-Pea?", speech_text)).set_should_end_session(
            False)
         return handler_input.response_builder.response

class NowPlayingIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("NowPlayingIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        songs = recent_songs(event, context)
        index = len(songs)

        speech_text = "Hello World"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Hello World", speech_text)).set_should_end_session(
            True)
        return handler_input.response_builder.response