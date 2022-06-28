from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionReceiveSentence(Action):

    def name(self) -> Text:
        return "action_save_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']

        return [SlotSet("name", text)]



class ActionSaySentence(Action):

    def name(self) -> Text:
        return "action_say_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")

        if not name:
            dispatcher.utter_message(text="I don't know your name")
        else:
            dispatcher.utter_message(text=f"Good to hear from you {name}, I can help you discuss mental disorders (ex: Depression, Anxiety, OCD, PTSD & ADHD), their symptoms and remedies!")
        return []










