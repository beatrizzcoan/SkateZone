import json

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body") or "{}")
        item_id = body.get("itemId")
        action = body.get("action")  # 'approve', 'edit', 'remove'

        if not item_id or action not in ["approve", "edit", "remove"]:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
                "body": json.dumps({"message": "itemId e ação válida ('approve', 'edit', 'remove') são obrigatórios."})
            }

        print(f"[AUDIT LOG - RF07] Moderação executada: Item {item_id} -> Ação: {action}")

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({
                "message": f"Moderação '{action}' aplicada com sucesso.",
                "itemId": item_id
            })
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": "Erro ao processar moderação", "error": str(e)})
        }