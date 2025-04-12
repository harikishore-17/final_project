from google import genai
from google.genai import types


def generate(input_text):
    final=""
    client = genai.Client(
        api_key="AIzaSyA5pq5GCfKCiDhb2PQQATPIOKIXChJeBqU",
    )

    model = "gemini-2.5-pro-exp-03-25"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=input_text+"return the points in html format with suitable tags."),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        final += chunk.text

    return final

def get_food_info(food_name):
    final = ""
    client = genai.Client(
        api_key="AIzaSyA5pq5GCfKCiDhb2PQQATPIOKIXChJeBqU",
    )

    model = "gemini-2.5-pro-exp-03-25"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"Provide the nutritional information of {food_name} in JSON format with the following structure: dish_name, serving_size, note, nutritional_info (calories, macronutrients (fat (total, saturated, polyunsaturated, monounsaturated, trans), protein, carbohydrates (total, dietary_fiber, sugars)), other_nutrients (cholesterol, sodium, potassium, calcium, iron)). Do not include any additional text."),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
    ):
        final += chunk.text
    cleaned_response = final.replace("```json", "").replace("```", "").strip()
    return cleaned_response

# if __name__ == "__main__":
#     get_food_info("Gobi Manchuria")