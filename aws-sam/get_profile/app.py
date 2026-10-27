import json

def lambda_handler(event, context):
    try:
        user_id = event.get("requestContext", {}).get("authorizer", {}).get("claims", {}).get("sub", "user_12345")

        profile_data = {
            "id": user_id,
            "name": "João da Silva",
            "email": "joao@exemplo.com",
            "city": "São Paulo",
            "avatarUrl": "https://s3.amazonaws.com/bucket/avatar.jpg"
        }

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps(profile_data)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": "Erro ao carregar perfil", "error": str(e)})
        }