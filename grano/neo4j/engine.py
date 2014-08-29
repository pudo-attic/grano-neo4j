from py2neo import neo4j

graph_db = None


def connect():
    global graph_db
    graph_db = neo4j.GraphDatabaseService()
