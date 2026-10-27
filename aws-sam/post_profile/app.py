import json

def lambda_handler(event, context):
    try:
        user_id = event.get("requestContext", {}).get("authorizer", {}).get("claims", {}).get("sub", "user_12345")
        body = json.loads(event.get("body") or "{}")

        updated_profile = {
            "id": user_id,
            "name": body.get("name", "João da Silva"),
            "city": body.get("city", "São Paulo"),
            "avatarUrl": body.get("avatarUrl", "https://s3.amazonaws.com/bucket/avatar.jpg"),
            "updatedAt": "2026-10-26T20:00:00Z"
        }

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": "Perfil atualizado com sucesso.", "profile": updated_profile})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": "Erro ao atualizar perfil", "error": str(e)})
        }