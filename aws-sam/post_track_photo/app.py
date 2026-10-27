import json
import uuid

def lambda_handler(event, context):
    try:
        path_parameters = event.get("pathParameters") or {}
        track_id = path_parameters.get("id")
        body = json.loads(event.get("body") or "{}")

        content_type = body.get("contentType")
        allowed_types = ["image/jpeg", "image/png", "image/webp"]

        if not track_id or content_type not in allowed_types:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
                "body": json.dumps({"message": "Formato de imagem inválido. Suportados: JPEG, PNG, WEBP."})
            }

        photo_id = uuid.uuid4().hex[:10]
        presigned_url = f"https://s3.amazonaws.com/bucket/tracks/{track_id}/{photo_id}.jpg"

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({
                "message": "URL de upload gerada com sucesso.",
                "uploadUrl": presigned_url,
                "photoId": photo_id
            })
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": "Erro ao processar envio de foto", "error": str(e)})
        }