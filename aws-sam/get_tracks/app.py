import json

def lambda_handler(event, context):
    try:
        tracks = [
            {"id": "track_1", "name": "Pista Central Skatepark", "lat": -23.55052, "lng": -46.633308, "type": "Street"},
            {"id": "track_2", "name": "Bowl do Parque", "lat": -23.561414, "lng": -46.655881, "type": "Bowl"}
        ]

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"tracks": tracks, "count": len(tracks)})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": "Erro ao carregar mapa de pistas", "error": str(e)})
        }