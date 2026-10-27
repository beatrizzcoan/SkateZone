import json

def lambda_handler(event, context):
    try:
        pending_items = [
            {"id": "mod_1", "type": "photo", "targetId": "track_1", "reason": "Imagem sinalizada"},
            {"id": "mod_2", "type": "comment", "targetId": "track_2", "reason": "Linguagem imprópria"}
        ]

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"pendingItems": pending_items, "count": len(pending_items)})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": "Erro ao listar moderação", "error": str(e)})
        }