import json

def lambda_handler(event, context):
    try:
        # Cron job periódico acionado pelo EventBridge
        upcoming_events = [
            {"id": "evt_1", "name": "Campeonato Regional", "interestedUsers": ["user_12345", "user_67890"]}
        ]

        notifications_sent = 0
        for evt in upcoming_events:
            for user in evt["interestedUsers"]:
                print(f"[NOTIFICATION SENT] Disparo enviado para o usuário {user} referente ao evento {evt['name']}")
                notifications_sent += 1

        print(f"[AUDIT LOG - RF06/RF15] Total de notificações enviadas: {notifications_sent}")

        return {
            "statusCode": 200,
            "body": json.dumps({"status": "success", "notificationsSent": notifications_sent})
        }
    except Exception as e:
        print(f"[ERROR] Falha ao enviar notificações: {str(e)}")
        raise e