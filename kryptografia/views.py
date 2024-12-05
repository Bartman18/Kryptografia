import secrets
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def generate_key():

    return secrets.token_hex(16)


@csrf_exempt
def encrypt_message(request):

    if request.method == "POST":
        body = json.loads(request.body)
        text = body.get("text", "")
        key = body.get("key", "")
        if not text or not key:
            return JsonResponse({"error": "Text and key are required."}, status=400)

        # Simple encryption algorithm
        key_length = len(key)
        encrypted_text = ''.join(
            chr(ord(char) + ord(key[i % key_length])) for i, char in enumerate(text)
        )

        return JsonResponse({"encrypted_text": encrypted_text})

    return JsonResponse({"error": "Invalid method."}, status=405)


@csrf_exempt
def decrypt_message(request):

    if request.method == "POST":
        body = json.loads(request.body)
        text = body.get("text", "")
        key = body.get("key", "")
        if not text or not key:
            return JsonResponse({"error": "Text and key are required."}, status=400)

        # Simple decryption algorithm
        key_length = len(key)
        decrypted_text = ''.join(
            chr(ord(char) - ord(key[i % key_length])) for i, char in enumerate(text)
        )

        return JsonResponse({"decrypted_text": decrypted_text})

    return JsonResponse({"error": "Invalid method."}, status=405)


@csrf_exempt
def generate_key_view(request):

    if request.method == "GET":
        key = generate_key()
        return JsonResponse({"key": key})

    return JsonResponse({"error": "Invalid method."}, status=405)
