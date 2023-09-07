from dotenv import load_dotenv
from pydantic import BaseSettings


class Configuration(BaseSettings):
    """Configuration parameters."""

    # project metadata
    app_name: str
    version: str

    # database url
    db_url: str


load_dotenv()

config = Configuration()
""" Configuration parameters instance. """
