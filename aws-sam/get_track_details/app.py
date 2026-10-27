import json

def lambda_handler(event, context):
    try:
        path_parameters = event.get("pathParameters") or {}
        track_id = path_parameters.get("id")

        if not track_id:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
                "body": json.dumps({"message": "ID da pista é obrigatório."})
            }

        track_details = {
            "id": track_id,
            "name": "Pista Central Skatepark",
            "address": "Av. Paulista, 1000 - São Paulo, SP",
            "ratingAvg": 4.8,
            "photos": ["https://s3.amazonaws.com/bucket/photo1.jpg"],
            "ratings": [{"userId": "user_01", "score": 5, "comment": "Ótima pista!"}]
        }

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps(track_details)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": "Erro ao carregar detalhes da pista", "error": str(e)})
        }