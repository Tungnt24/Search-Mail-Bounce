from pymongo import MongoClient
from backend.settings import Config


def _get_collection():
    mongo_client = MongoClient(Config.MONGODB_URI)
    db = mongo_client.get_database(Config.MONGODB_DB)
    collection = db.get_collection(Config.MONGODB_COLLECTION)
    return collection


def get_result(records):
    results = {"records": []}
    for record in records:
        results['records'].append({
            "Queue_Id": record.get("QueueId"),
            "From": record.get("From"),
            "To": record.get("To"),
            "Message_Id": record.get("MessageId"),
            "Recipient_Smtp_Ip": record.get("RecipientSmtpIp"),
            "Recipient_Smtp_Domain": record.get("RecipientSmtpDomain"),
            "Status": record.get("Status"),
            "Message": record.get("Message"),
            "Sent_At": record.get("SentAt")
        })
    return results
