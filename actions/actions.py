# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
#
#


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # To get current slot value from the tracker
        name = tracker.get_slot("name")
        country = tracker.get_slot("country")

        leader_name = ''
        if country.lower() == 'america':
            leader_name = 'Joe Biden'
        elif country.lower() == 'india':
            leader_name = 'Mr. Modi'
        else:
            leader_name = "Leader name not found in db."

        message = name + ' belongs to ' + country + ' and leader name is ' + leader_name
        print(message)

        # Used text to display text message
        dispatcher.utter_message(text=message)

        # To set custom slot name using SlotSet module
        return [SlotSet("leader", leader_name)]
