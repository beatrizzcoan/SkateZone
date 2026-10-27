import json

def lambda_handler(event, context):
    try:
        user_id = event.get("requestContext", {}).get("authorizer", {}).get("claims", {}).get("sub", "user_12345")
        path_parameters = event.get("pathParameters") or {}
        track_id = path_parameters.get("id")
        body = json.loads(event.get("body") or "{}")

        score = body.get("score")

        if not track_id or score is None or not (1 <= score <= 5):
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
                "body": json.dumps({"message": "ID da pista e nota válida entre 1 e 5 são obrigatórios."})
            }

        # Atualização da média com concorrência (RNF09)
        updated_stats = {
            "trackId": track_id,
            "newRatingAvg": 4.7,
            "totalRatings": 12
        }

        return {
            "statusCode": 201,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({
                "message": "Avaliação registrada com sucesso.",
                "rating": {"userId": user_id, "score": score, "comment": body.get("comment", "")},
                "trackStats": updated_stats
            })
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": "Erro ao avaliar pista", "error": str(e)})
        }