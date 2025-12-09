# -*- coding: utf-8 -*-
from google import genai

client = genai.Client(api_key="")

while True:
    question = input("What is your question?\n")

    prompt = f"""
    System: You are a teenage boy, about the age of 15 in the early 2000s. Respond as such.
    User: {question}
    """

    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=prompt
    )

    print(response.text)
