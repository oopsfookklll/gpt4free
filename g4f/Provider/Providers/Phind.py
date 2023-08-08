# Assuming the Phind provider has similar structure to the Bing provider

import os
import json
import random
import json
import os
import uuid
import ssl
import certifi
import aiohttp
import asyncio

import requests
from ...typing import sha256, Dict, get_type_hints

url = 'https://phind.com/chat'
model = ['gpt-4']
supports_stream = True
needs_auth = False
working = True

ssl_context = ssl.create_default_context()
ssl_context.load_verify_locations(certifi.where())

# Assuming the Phind provider has similar optionsSets and Defaults to the Bing provider
class optionsSets:
    optionSet: dict = {
        'tone': str,
        'optionsSets': list
    }

    jailbreak: dict = {
        "optionsSets": [
            'saharasugg',
            'enablenewsfc',
            'clgalileo',
            'gencontentv3',
            "nlu_direct_response_filter",
            "deepleo",
            "disable_emoji_spoken_text",
            "responsible_ai_policy_235",
            "enablemm",
            "h3precise"
            # "harmonyv3",
            "dtappid",
            "cricinfo",
            "cricinfov2",
            "dv3sugg",
            "nojbfedge"
        ]
    }

class Defaults:
    delimiter = '\x1e'
    ip_address = f'13.{random.randint(104, 107)}.{random.randint(0, 255)}.{random.randint(0, 255)}'

    allowedMessageTypes = [
        'Chat',
        'Disengaged',
        'AdsQuery',
        'SemanticSerp',
        'GenerateContentQuery',
        'SearchQuery',
        'ActionRequest',
        'Context',
        'Progress',
        'AdsQuery',
        'SemanticSerp'
    ]

    sliceIds = [

        # "222dtappid",
        # "225cricinfo",
        # "224locals0"

        'winmuid3tf',
        'osbsdusgreccf',
        'ttstmout',
        'crchatrev',
        'winlongmsgtf',
        'ctrlworkpay',
        'norespwtf',
        'tempcacheread',
        'temptacache',
        '505scss0',
        '508jbcars0',
        '515enbotdets0',
        '5082tsports',
        '515vaoprvs',
        '424dagslnv1s0',
        'kcimgattcf',
        '427startpms0'
    ]

    location = {
        'locale': 'en-US',
        'market': 'en-US',
        'region': 'US',
        'locationHints': [
            {
                'country': 'United States',
                'state': 'California',
                'city': 'Los Angeles',
                'timezoneoffset': 8,
                'countryConfidence': 8,
                'Center': {
                    'Latitude': 34.0536909,
                    'Longitude': -118.242766
                },
                'RegionType': 2,
                'SourceType': 1
            }
        ],
    }

def _format(msg: dict) -> str:
    return json.dumps(msg, ensure_ascii=False) + Defaults.delimiter

async def create_conversation():
    # existing code...
    return conversationId, clientId, conversationSignature

async def stream_generate(prompt: str, mode: optionsSets.optionSet = optionsSets.jailbreak, context: bool or str = False):
    resp_txt = ''
    cache_text = ''
    # existing code...
    return {
        'response_text': resp_txt,
        'cache_text': cache_text
    }
    # existing code...
    return {
        'response_text': resp_txt,
        'cache_text': cache_text
    }

def run(generator):  
    loop = asyncio.new_event_loop()  
    asyncio.set_event_loop(loop)  
    gen = generator.__aiter__()  
  
    while True:  
        try:  
            next_val = loop.run_until_complete(gen.__anext__())  
            yield next_val  
  
        except StopAsyncIteration:  
            break  
    #print('Done')  

def convert(messages):
    context = ""

    for message in messages:
        context += "[%s](#message)\n%s\n\n" % (message['role'],
                                               message['content'])

    return context

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    if model not in ['gpt-4']:
        raise ValueError("Model not supported")
    if len(messages) < 2:
        prompt = messages[0]['content']
        context = False

    else:
        prompt = messages[-1]['content']
        context = convert(messages[:-1])

    response = run(stream_generate(prompt, optionsSets.jailbreak, context))
    for token in response:
        yield (token)

    #print('Done')

params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join(
        [f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])