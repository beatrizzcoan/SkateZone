import json
import math

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Raio da Terra em km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def lambda_handler(event, context):
    try:
        params = event.get("queryStringParameters") or {}
        user_lat = float(params.get("lat", -23.55052))
        user_lng = float(params.get("lng", -46.633308))

        all_tracks = [
            {"id": "track_1", "name": "Pista Central", "lat": -23.55052, "lng": -46.633308},
            {"id": "track_2", "name": "Bowl do Parque", "lat": -23.561414, "lng": -46.655881}
        ]

        for track in all_tracks:
            track["distanceKm"] = round(calculate_distance(user_lat, user_lng, track["lat"], track["lng"]), 2)

        sorted_tracks = sorted(all_tracks, key=lambda x: x["distanceKm"])

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"nearbyTracks": sorted_tracks})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": "Erro ao buscar pistas próximas", "error": str(e)})
        }