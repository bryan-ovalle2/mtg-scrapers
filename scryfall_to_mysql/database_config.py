from sqlalchemy import create_engine


def create_engine_instance(username, password, host, database_name, port=3306):
    connection_string = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database_name}"
    return create_engine(connection_string)
