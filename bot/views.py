import json
import requests
import re
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Count
import openai
from .models import Lead
from modularizacion.settings import TELEGRAM_TOKEN

TELEGRAM_TOKEN = TELEGRAM_TOKEN

# Sesiones en memoria (simple para empezar)
SESSIONS = {}

EMAIL_REGEX = r"[^@]+@[^@]+\.[^@]+"
PHONE_REGEX = r"\d{7,15}"


def send_message(chat_id, text):
    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        data={"chat_id": chat_id, "text": text}
    )


@csrf_exempt
def telegram_webhook(request):
    if request.method != "POST":
        return JsonResponse({"ok": True})

    data = json.loads(request.body)

    if "message" not in data:
        return JsonResponse({"ok": True})

    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "").strip().lower()

    # Crear sesión
    if chat_id not in SESSIONS:
        SESSIONS[chat_id] = {
            "step": "nombre",
            "data": {}
        }
        send_message(chat_id, "👋 Hola! Vamos a registrar tus datos.\n\n¿Cuál es tu nombre?")
        return JsonResponse({"ok": True})

    session = SESSIONS[chat_id]

    # PASO 1: Nombre
    if session["step"] == "nombre":
        session["data"]["nombre"] = text.title()
        session["step"] = "apellidos"
        send_message(chat_id, "Genial 😊 ¿Cuáles son tus apellidos?")
        return JsonResponse({"ok": True})

    # PASO 2: Apellidos
    if session["step"] == "apellidos":
        session["data"]["apellidos"] = text.title()
        session["step"] = "email"
        send_message(chat_id, "📧 ¿Cuál es tu email?")
        return JsonResponse({"ok": True})

    # PASO 3: Email
    if session["step"] == "email":
        if not re.match(EMAIL_REGEX, text):
            send_message(chat_id, "❌ Ese email no parece válido. Inténtalo de nuevo.")
            return JsonResponse({"ok": True})

        session["data"]["email"] = text
        session["step"] = "telefono"
        send_message(chat_id, "📞 ¿Tu número de teléfono?")
        return JsonResponse({"ok": True})

    # PASO 4: Teléfono
    if session["step"] == "telefono":
        if not re.search(PHONE_REGEX, text):
            send_message(chat_id, "❌ El teléfono no parece válido. Usa solo números.")
            return JsonResponse({"ok": True})

        session["data"]["telefono"] = text
        session["step"] = "direccion"
        send_message(chat_id, "📍 ¿Tu ciudad o dirección?")
        return JsonResponse({"ok": True})

    # PASO 5: Dirección → Confirmación
    if session["step"] == "direccion":
        session["data"]["direccion"] = text.title()
        session["step"] = "confirmacion"

        d = session["data"]
        resumen = (
            "📝 *Revisa tus datos:*\n\n"
            f"👤 Nombre: {d['nombre']} {d['apellidos']}\n"
            f"📧 Email: {d['email']}\n"
            f"📞 Teléfono: {d['telefono']}\n"
            f"📍 Dirección: {d['direccion']}\n\n"
            "¿Es correcto? ✅ (sí / no)"
        )

        send_message(chat_id, resumen)
        return JsonResponse({"ok": True})

    # PASO 6: Confirmación
    if session["step"] == "confirmacion":
        if text in ["si", "sí", "s"]:
            Lead.objects.create(**session["data"])
            send_message(chat_id, "✅ ¡Perfecto! Tus datos han sido guardados. Gracias 🙌")
            del SESSIONS[chat_id]
            return JsonResponse({"ok": True})

        if text in ["no", "n"]:
            del SESSIONS[chat_id]
            send_message(chat_id, "🔄 Sin problema. Empezamos de nuevo.\n\n¿Cuál es tu nombre?")
            SESSIONS[chat_id] = {"step": "nombre", "data": {}}
            return JsonResponse({"ok": True})

        send_message(chat_id, "❓ Responde con *sí* o *no* por favor 🙂")
        return JsonResponse({"ok": True})

    return JsonResponse({"ok": True})




# ---------- DASHBOARD ----------

def index(request):
    return render(request, "dashboard.html", {
        "total_leads": Lead.objects.count(),
        "ultimos_leads": Lead.objects.order_by("-id")[:5]
    })


def api_total_leads(request):
    return JsonResponse({"total": Lead.objects.count()})


def api_leads_por_dominio(request):
    dominios = (
        Lead.objects
        .extra(select={"dominio": "SUBSTR(email, INSTR(email, '@') + 1)"} )
        .values("dominio")
        .annotate(total=Count("id"))
    )
    return JsonResponse(list(dominios), safe=False)

@csrf_exempt
def edit_lead_api(request, id):
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido"}, status=405)

    lead = Lead.objects.get(id=id)
    data = json.loads(request.body)

    lead.nombre = data.get("nombre", lead.nombre)
    lead.apellidos = data.get("apellidos", lead.apellidos)
    lead.email = data.get("email", lead.email)
    lead.telefono = data.get("telefono", lead.telefono)
    lead.direccion = data.get("direccion", lead.direccion)

    lead.save()

    return JsonResponse({"ok": True})

@csrf_exempt
def delete_lead_api(request, id):
    if request.method != "DELETE":
        return JsonResponse({"error": "Método no permitido"}, status=405)

    lead = Lead.objects.get(id=id)
    lead.delete()

    return JsonResponse({"ok": True})