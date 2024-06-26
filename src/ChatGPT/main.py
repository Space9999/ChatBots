import openai
API_KEY = input("Enter API Key: ")
openai.api_key = API_KEY
def query(prompt):
  try:
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message
  except openai.error.OpenAIError as e:
    print(f"OpenAI API error: {e}")
  except Exception as e:
    print(f"Error querying OpenAI: {e}")
end = False;
while (end == False):
  prompt = input("Enter prompt to CHATGPT: ")
  print(query(prompt))
  checkEnd = input("End (Y/N): ")
  if (checkEnd == "Y"):
    end = True;
