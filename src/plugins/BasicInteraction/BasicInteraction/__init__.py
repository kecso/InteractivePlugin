"""
This is where the implementation of the plugin code goes.
The BasicInteraction-class is imported from both run_plugin.py and run_debug.py
"""
import sys
import logging
import time
import os
from webgme_bindings import PluginBase

from BasicInteraction.communication import *

# Setup a logger
logger = logging.getLogger('BasicInteraction')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)  # By default it logs to stderr..
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class BasicInteraction(PluginBase):
    def setup_communication(self, communication_file):
        set_communication_file(communication_file)

    def main(self):
        core = self.core
        root_node = self.root_node
        active_node = self.active_node
        # Get the current working directory
        # cwd = os.getcwd()
        # logger.error("Current working directory: {0}".format(cwd))
        running = True

        while running:
            response = ask_user(self, {"title": "Input is required from BasicInteraction plugin:",
            "description":"please fill out the form to your best knowledge",
            "fields": [
                {
                    "name":"doFinish",
                    "displayName": "Do you want to stop plugin execution?",
                    "description": "If flag is set, the plugin will ask no further questions...",
                    "value": False,
                    "valueType": "boolean",
                    "readOnly": False
                },
                {
                "name": "species",
                "displayName": "Animal Species",
                "regex": "^[a-zA-Z]+$",
                "regexMessage": "Name can only contain English characters!",
                "description": "Which species does the animal belong to.",
                "value": "Horse",
                "valueType": "string",
                "readOnly": False
                },
                {
                "name": "age",
                "displayName": "Age",
                "description": "How old is the animal.",
                "value": 3,
                "valueType": "number",
                "minValue": 0,
                "maxValue": 10000,
                "readOnly": False,
                "writeAccessRequired": True
                },
                {
                "name": "gender",
                "displayName": "Gender distribution",
                "description": "What is the ratio between females and males?",
                "value": 0.5,
                "valueType": "number",
                "minValue": 0,
                "maxValue": 1,
                "increment": 0.01
                },
                {
                "name": "carnivore",
                "displayName": "Carnivore",
                "description": "Does the animal eat other animals?",
                "value": False,
                "valueType": "boolean",
                "readOnly": False
                },
                {
                "name": "isAnimal",
                "displayName": "Is Animal",
                "description": "Is this animal an animal? [Read-only]",
                "value": True,
                "valueType": "boolean",
                "readOnly": True
                },
                {
                "name": "classification",
                "displayName": "Classification",
                "description": "",
                "value": "Vertebrates",
                "valueType": "string",
                "valueItems": [
                    "Vertebrates",
                    "Invertebrates",
                    "Unknown"
                ]
                },
                {
                "name": "color",
                "displayName": "Color",
                "description": "The hex color code for the animal.",
                "readOnly": False,
                "value": "#FF0000",
                "regex": "^#([A-Fa-f0-9]{6})$",
                "valueType": "string"
                },
                {
                "name": "food",
                "displayName": "Food",
                "description": "Food preference ordered",
                "readOnly": False,
                "value": [
                    "Grass",
                    "Mushrooms",
                    "Leaves",
                    "Antilope",
                    "Rabbit"
                ],
                "valueType": "sortable",
                "valueItems": [
                    "Grass",
                    "Mushrooms",
                    "Leaves",
                    "Antilope",
                    "Rabbit"
                ]
                },
                {
                "name": "file",
                "displayName": "File",
                "description": "",
                "value": "",
                "valueType": "asset",
                "readOnly": False
                }
            ]})
            logger.error(response)
            if response != None and response['doFinish']:
                running = False

