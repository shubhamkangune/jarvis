from openai import openAI

client = openAI(
  api_key="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"
)

completion = client.chat.complitions.create(
  model="gpt-3.5-turbo",
  message=[
    {"role": "system","content":"You are a virtual assistance name jarvis skilled in general task like Alexa and Google Claud"},
    {"role": "user", "content": "What is coding"}
  ]
)

print(completion.choices[0].message)