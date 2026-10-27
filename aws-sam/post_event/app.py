import json
import uuid

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body") or "{}")

        name = body.get("name")
        date = body.get("date")
        location = body.get("location")

        if not name or not date or not location:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
                "body": json.dumps({"message": "Campos obrigatórios: name, date e location."})
            }

        new_event = {
            "id": f"evt_{uuid.uuid4().hex[:8]}",
            "name": name,
            "date": date,
            "location": location,
            "description": body.get("description", ""),
            "category": body.get("category", "geral")
        }

        print(f"[AUDIT LOG - RF07] Evento cadastrado: {new_event['id']}")

        return {
            "statusCode": 201,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": "Evento criado com sucesso.", "event": new_event})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": "Erro ao cadastrar evento", "error": str(e)})
        }