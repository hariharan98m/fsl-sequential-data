import numpy as np
import openai
import os
from dotenv import load_dotenv
load_dotenv()

from sklearn.model_selection import train_test_split

openai.api_key = os.getenv("OPENAI_API_KEY")

def raw_predict(prompt, model = 'text-davinci-002'):
        response = openai.Completion.create(
                model= model, #"text-davinci-002",
                prompt=prompt,
                temperature=0.6,
                max_tokens = 200
            )
        result = response.choices[0].text
        return result

def predict_ns(task, examples, query, query_instruct_text):
        prompt = f'''{task}
        {examples}

        {query_instruct_text}
        {query}'''
        
        return raw_predict(prompt)