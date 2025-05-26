from config import GEMINI_API_KEY
from google import genai

client = genai.Client(api_key=GEMINI_API_KEY)

instructions=""" 
You are a social media comment analysis system. Your role is to evaluate the context of these comments, filter and classify them.  
You must return data ONLY in JSON format, with no additional explanations:
{
    "sentiment": "value",
    "intensity": value
}
sentiment is of type String, and can only be one of the following values: Positive, Negative, or Neutral.

intensity is a numeric value, following a scale from -5 to +5. You must choose a number that represents the intensity of the comment's sentiment.

If the comment contains xenophobic, racist, prejudiced or discriminatory content, reject the evaluation and return : NULL.
"""

comment="""
eu acho que a bitcoin parece que vai subir nos próximos 7 dias
"""
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=comment,
    config=genai.types.GenerateContentConfig(
        system_instruction=instructions)
)
print(response.text)
