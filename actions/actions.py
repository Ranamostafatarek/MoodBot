from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionReceiveSentence(Action):

    def name(self) -> Text:
        return "action_receive_sentence"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']
        dispatcher.utter_message(text=f"I'll remember your sentence!")
        return [SlotSet("sentence", text)]


class ActionSaySentence(Action):

    def name(self) -> Text:
        return "action_repeat_sentence"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        sentence = tracker.get_slot("sentence").upper()
        if not sentence:
            dispatcher.utter_message(text="I don't know what to repeat")
        else:
            dispatcher.utter_message(text=f"I want to tell you that {sentence}!")
        return []
