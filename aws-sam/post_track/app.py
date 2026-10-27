import json
import uuid

def lambda_handler(event, context):
    try:
        user_id = event.get("requestContext", {}).get("authorizer", {}).get("claims", {}).get("sub", "user_12345")
        body = json.loads(event.get("body") or "{}")

        name = body.get("name")
        address = body.get("address")
        lat = body.get("lat")
        lng = body.get("lng")

        if not name or not address or lat is None or lng is None:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
                "body": json.dumps({"message": "Campos obrigatórios: name, address, lat, lng."})
            }

        new_track = {
            "id": f"track_{uuid.uuid4().hex[:8]}",
            "name": name,
            "address": address,
            "type": body.get("type", "Geral"),
            "lat": lat,
            "lng": lng,
            "createdBy": user_id
        }

        print(f"[AUDIT LOG - RF07] Pista cadastrada: {new_track['id']} por {user_id}")

        return {
            "statusCode": 201,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": "Pista cadastrada com sucesso.", "track": new_track})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": "Erro ao cadastrar pista", "error": str(e)})
        }