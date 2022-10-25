# Few-shot Learning for Sequential Data
Learn data-efficient few shot strategies to harness knowledge from large pretrained models for sequential prediction tasks.

## 1. Code setup
### 1.1. Getting GPT-3
1. Get access to OpenAI APIs. Head to https://beta.openai.com/ and create your account with free credits.
2. Set env vars under `.env` file. Add OPENAI_API_KEY
3. Sample snippet to call inference.
```python
response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(prompts),
            temperature=0.6,
        )
result = response.choices[0].text
```
## 2. Robust Fine-tuning GPT-Neo for sequence prediction task
**Steps:**
*Creating meta-learning episodes*
1. Create a support set of examples each as a list of different activities.
2. Append the incomplete query example to the support set at the end.
*Fine-tuning*
3. Apply a loss mask to the label outputs that GPT must optimize for correctly. Zero out loss for other inputs.
4. Ensure padding and attention masks (for causal inference Left to Right)
5. Freeze inner layers. Run backprop, minimize error with SGD.

## Dataset
https://github.com/epic-kitchens/epic-kitchens-100-annotations#epic_100_test_timestampscsv
