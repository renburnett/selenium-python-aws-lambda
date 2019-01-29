from kexp_crawler import recent_songs

from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard

songs = recent_songs(event, context)

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
        if songs[0]['name'] == 'Now Playing':
            speech_text = "The current song is " + songs[1]['name'] + " by " + songs[1]['artist'] + " off of the album " + songs[1]['album']
        else:
            speech_text = "The current song is " + songs[0]['name'] + " by " + songs[0]['artist'] + " off of the album " + songs[0]['album']

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Now Playing", speech_text)).set_should_end_session(
            True)
        return handler_input.response_builder.response