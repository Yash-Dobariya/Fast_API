from pydantic import BaseModel
from datetime import date


class Commonschemas():
    created_at: date
    update_at: date
    is_active: bool
    is_delete: bool
