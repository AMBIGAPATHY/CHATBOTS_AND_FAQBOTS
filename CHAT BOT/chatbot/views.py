from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt

HUGGINGFACE_API_KEY = "Enter-your-api-key-here"

# Use Falcon-7B for generating detailed answers
MODEL_NAME = "tiiuae/falcon-7b-instruct"
# MODEL_NAME = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"

def chatbot_view(request):
    return render(request, "chatbot/index.html")

@csrf_exempt
def chatbot_api(request):
    if request.method == "POST":
        user_input = request.POST.get("message")
        response = get_detailed_response(user_input)
        return JsonResponse({"response": response})
    return JsonResponse({"error": "Invalid request"}, status=400)

def get_detailed_response(user_input):
    """
    Uses Falcon-7B to generate detailed and informative answers.
    """
    url = f"https://api-inference.huggingface.co/models/{MODEL_NAME}"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    data = {"inputs": f"Explain in detail: {user_input}", "parameters": {"max_new_tokens": 300}}

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    # Handle API errors
    if "error" in result:
        return "Sorry, I'm unable to fetch an answer at the moment."

    return result[0]["generated_text"]
