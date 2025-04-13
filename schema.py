import strawberry
from typing import List
from db import get_session  # Import the function to get Neo4j session

@strawberry.type
class Device:
    name: str
    ip: str
    mac: str

@strawberry.type
class Switch:
    name: str
    

@strawberry.type
class Server:
    name: str
    
@strawberry.type
class Query:

    @strawberry.field
    def all_devices(self) -> List[Device]:
        query = "MATCH (d:Device) RETURN d.name AS name, d.ip AS ip, d.mac AS mac"
        session = get_session()  # Get a session
        result = session.run(query)  # Run the query
        return [Device(**record) for record in result]

    @strawberry.field
    def all_switches(self) -> List[Switch]:
        query = "MATCH (s:Switch) RETURN s.name AS name"
        session = get_session()  # Get a session
        result = session.run(query)  # Run the query
        return [Switch(**record) for record in result]
    
    @strawberry.field
    def all_servers(self) -> List[Server]:
        query = "MATCH (s:Server) RETURN s.name AS name"
        session = get_session()  # Get a session
        result = session.run(query)  # Run the query
        return [Server(**record) for record in result]

    @strawberry.field
    def devices_by_switch(self, switch_name: str) -> List[Device]:
        query = f"""
        MATCH (s:Switch {{name: '{switch_name}'}})-[:CONNECTED_TO]->(d:Device)
        RETURN d.name AS name, d.ip AS ip, d.mac AS mac
        """
        session = get_session()  # Get a session
        result = session.run(query)  # Run the query
        return [Device(**record) for record in result]

# Create schema with the Query class
schema = strawberry.Schema(query=Query)
