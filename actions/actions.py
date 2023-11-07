# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
import pymongo
#
#

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["lvtn_2023"]
products = mydb["products"]

class ActionDefaultFallback(Action):
    def name(sefl) -> Text:
        return "action_default_fallback"
    
    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_default")

        # Revert user message which led to fallback.
        return [UserUtteranceReverted()]

class ActionMaleWatch(Action):
    def name(self) -> Text:
        return "action_male_watch"

    def run(
        self, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        quantity = products.count_documents({"gender": 1})
        dispatcher.utter_message(
            template='utter_male_watch',
            quantity=quantity
        )

        return [UserUtteranceReverted()]

class ActionFemaleWatch(Action):
    def name(self) -> Text:
        return "action_female_watch"

    def run(
        self, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        quantity = products.count_documents({"gender": 2})
        dispatcher.utter_message(
            template='utter_female_watch',
            quantity=quantity
        )

        return [UserUtteranceReverted()]

class ActionCoupleWatch(Action):
    def name(self) -> Text:
        return "action_couple_watch"

    def run(
        self, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        quantity = products.count_documents({"gender": 0})
        dispatcher.utter_message(
            template='utter_couple_watch',
            quantity=quantity
        )

        return [UserUtteranceReverted()]
