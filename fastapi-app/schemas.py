from pydantic import BaseModel
from typing import Optional

# Base Schema for Object Detection
class ObjectDetectionBase(BaseModel):
    image: str
    class_id: int
    confidence: float
    x_center: float
    y_center: float
    width: float
    height: float

# Schema for creating a detection
class ObjectDetectionCreate(ObjectDetectionBase):
    pass  # No need for an ID when creating

# Schema for updating a detection
class ObjectDetectionUpdate(ObjectDetectionBase):
    pass  # All fields required when updating

# Schema for response (including ID)
class ObjectDetection(ObjectDetectionBase):
    id: int

    class Config:
        orm_mode = True