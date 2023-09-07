from typing import Any, Type, TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound="MongoBase")


class MongoBase(BaseModel):
    """Class that handles conversions between MongoDB '_id' key and our own 'id' key.

    MongoDB uses `_id` as an internal default index key.
    We can use that to our advantage.
    """

    class Config:
        """basic config."""

        from_attributes = True
        populate_by_name = True

    @classmethod
    def from_mongo(
        cls: Type[T], data: dict[str, dict[str, Any | None]]
    ) -> T | dict[str, dict[str, Any | None]]:
        """Convert "_id" (str object) into "id" (UUID object)."""

        if not data:
            return data

        mongo_id = data.pop("_id", None)
        return cls(**dict(data, id=mongo_id))

    def to_mongo(self, **kwargs: Any) -> dict[str, Any | None]:
        """Convert "id" (UUID object) into "_id" (str object)."""

        parsed = self.dict(**kwargs)

        if "_id" not in parsed and "id" in parsed:
            parsed["_id"] = str(parsed.pop("id"))

        return parsed
