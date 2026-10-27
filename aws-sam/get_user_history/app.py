import json

def lambda_handler(event, context):
    try:
        user_id = event.get("requestContext", {}).get("authorizer", {}).get("claims", {}).get("sub", "user_12345")

        user_history = {
            "userId": user_id,
            "interestedEvents": [{"id": "evt_1", "name": "Campeonato Regional"}],
            "createdTracks": [{"id": "track_1", "name": "Pista Central Skatepark"}],
            "ratings": [{"trackId": "track_2", "score": 5}]
        }

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps(user_history)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": "Erro ao carregar histórico", "error": str(e)})
        }