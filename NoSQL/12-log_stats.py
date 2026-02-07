#!/usr/bin/env python3
""" Modulo para mostrar estadisticas de logs de Nginx """
from pymongo import MongoClient


def log_stats():
    """ Proporciona estadisticas sobre los logs de Nginx en MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # Total de logs
    num_logs = collection.count_documents({})
    print(f"{num_logs} logs")

    # Estadisticas por metodo
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Chequeo de estado especifico
    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
