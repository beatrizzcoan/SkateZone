import json

def lambda_handler(event, context):
    try:
        user_id = event.get("requestContext", {}).get("authorizer", {}).get("claims", {}).get("sub", "user_12345")
        path_parameters = event.get("pathParameters") or {}
        event_id = path_parameters.get("id")

        if not event_id:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
                "body": json.dumps({"message": "ID do evento é obrigatório."})
            }

        print(f"[INTEREST LOG] Usuário {user_id} marcou interesse no evento {event_id}")

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({
                "message": "Interesse registrado com sucesso.",
                "eventId": event_id,
                "userId": user_id
            })
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": "Erro ao registrar interesse", "error": str(e)})
        }