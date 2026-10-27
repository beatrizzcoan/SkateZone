import json

def lambda_handler(event, context):
    try:
        path_parameters = event.get("pathParameters") or {}
        event_id = path_parameters.get("id")
        body = json.loads(event.get("body") or "{}")

        if not event_id:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
                "body": json.dumps({"message": "ID do evento é obrigatório."})
            }

        updated_event = {
            "id": event_id,
            "name": body.get("name"),
            "date": body.get("date"),
            "location": body.get("location")
        }

        print(f"[AUDIT LOG - RF07] Evento editado: {event_id}")

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": "Evento atualizado com sucesso.", "event": updated_event})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": "Erro ao editar evento", "error": str(e)})
        }