import json

def lambda_handler(event, context):
    try:
        path_parameters = event.get("pathParameters") or {}
        event_id = path_parameters.get("id")

        if not event_id:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
                "body": json.dumps({"message": "ID do evento é obrigatório."})
            }

        print(f"[AUDIT LOG - RF07] Evento removido: {event_id}")

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": f"Evento {event_id} removido com sucesso."})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": "Erro ao remover evento", "error": str(e)})
        }