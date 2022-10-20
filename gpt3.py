import openai
import os
from dotenv import load_dotenv
load_dotenv()
import tqdm
openai.api_key = os.getenv("OPENAI_API_KEY")

# example for summarization of the Caesarian section dataset
prompt = '''We have another case of a 29-year old woman in her second timely delivery, with a normal blood pressure but heart problems. She delivered by caesarian.
At 40 years old, this woman is delivering for the first time. She has a normal blood pressure but has heart issue. She delivered by caesarian.
We have another case of a 29-year old woman in her second timely delivery, with a normal blood pressure but heart problems. She delivered by caesarian.
A 32-year old woman is delivering for the third time, but this time it's timely. She has a normal blood pressure but has heart issue. She delivered normally.
We have a 17-year old woman who is delivering for the first time. She has a low blood pressure but no heart problems. She delivered by caesarian.
A 21-year old woman is making a premature delivery for the second time. She has low blood pressure and heart problems. As a result, she delivered by caesarian.
And lastly, a 20-year old woman delivering for the first time in a timely manner but with high blood pressure and heart problems. She delivered by caesarian.
A 32 year woman in her second timely delivery is going through a heart problem but has normal blood pressure. She delivered by caesarian.
A 21-year old woman is making a premature delivery for the second time. She has low blood pressure and heart problems. As a result, she delivered by caesarian.
A 27-year old woman is in her first premature delivery but has a normal blood pressure with no heart problems. She delivered by caesarian.
Now here comes a 37-year old woman delivering timely for the 3rd time. She has a normal blood pressure but has heart issue. She delivered by caesarian.
A 27-year old woman is in her first premature delivery but has a normal blood pressure with no heart problems. She delivered by caesarian.
Last but not least, a 19-year old woman in her first timely delivery. She has a normal blood pressure and no heart problems. But she delivered by caesarian.
This 29-year old woman is in her second premature delivery. She has a high blood pressure and no heart problems. She also delivered by caesarian.
A 32 year woman in her second timely delivery is going through a heart problem but has normal blood pressure. She delivered by caesarian.
And lastly, a 26-year old woman in her second delivery but latecomer stage. She has a normal blood pressure but no heart problems. She delivered normally.
Its the first delivery for a young woman in her early 20s. She has a high blood pressure, but no heart problems and a late delivery. Fortunately, her delivery result was normal.
Its the first delivery for a young woman in her early 20s. She has a high blood pressure, but no heart problems and a late delivery. Fortunately, her delivery result was normal.
In another case, we have a 36-year old woman in her first timely delivery with a perfectly fine blood pressure and no heart issues. Her result was normal.
Its the first delivery for a 19-year old woman. She has a normal blood pressure and no heart problems. But she delivered by caesarian.
A 26-year old woman in her second premature delivery has a normal blood pressure but a heart condition. Despite this, she had a normal delivery.
Its the second delivery for a 25-year old woman and everything is going on timely. She has a normal blood pressure and no heart problems. Her delivery result was normal.
Its the first delivery for a 19-year old woman. She has a normal blood pressure and no heart problems. But she delivered by caesarian.
In this case, we have a 20-year old woman in her first timely delivery. She has a normal blood pressure but has a heart issue. Fortunately, she was able to deliver normally.
A 25-year old woman in her first delivery, and everything is going as it should be. She has a normal blood pressure and no heart problems. Her delivery was normal.
A 26-year old woman in her first timely delivery with a perfectly fine blood pressure and no heart issues. Her result was normal.
Its the second delivery for a 25-year old woman and everything is going on timely. She has a normal blood pressure and no heart problems. Her delivery result was normal.
In this case, we have a 35-year old woman in her first premature delivery. She has low blood pressure and no heart problems. Her delivery was normal.
Its the first delivery for a young woman in her early 30s. She has a normal blood pressure, no heart problems and a timely delivery. Naturally her delivery result was normal.
A first-time 25-year old woman with low blood pressure and no heart problems had a normal, timely delivery.

Tl;dr
'''

if __name__ == '__main__':
    model = 'text-davinci-002'
    # models out there in decreasing order of size: text-curie-001, text-babbage-001, text-ada-001
    response = openai.Completion.create(
            model= model, #"text-davinci-002",
            prompt=prompt,
            temperature=0.6, # use this temperature setting.
            max_tokens = 500
            # stop = '\n'
        )
    result = response.choices[0].text
    print(result)
    # result will be
    # '\n\nA variety of different factors can affect the delivery method of a baby, with the most common being the age and health of the mother. In general, younger mothers and those with no health problems are more likely to have a normal delivery, while older mothers and those with health problems are more likely'