import os
from neo4j import GraphDatabase

uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
username = os.getenv("NEO4J_USERNAME", "neo4j")
password = os.getenv("NEO4J_PASSWORD", "1234567890")

driver = GraphDatabase.driver(uri, auth=(username, password))

def get_session():
    return driver.session()
