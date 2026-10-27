import json

def lambda_handler(event, context):
    try:
        params = event.get("queryStringParameters") or {}
        city_filter = params.get("city")
        category_filter = params.get("category")

        events = [
            {"id": "evt_1", "name": "Campeonato Regional", "date": "2026-11-10", "city": "São Paulo", "category": "skate"},
            {"id": "evt_2", "name": "Encontro Noturno", "date": "2026-11-15", "city": "Rio de Janeiro", "category": "bmx"}
        ]

        if city_filter:
            events = [e for e in events if e["city"].lower() == city_filter.lower()]
        if category_filter:
            events = [e for e in events if e["category"].lower() == category_filter.lower()]

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"events": events, "count": len(events)})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": "Erro ao buscar eventos", "error": str(e)})
        }