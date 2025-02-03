from sqlalchemy import Column, Integer, String, Text, Float
from database import Base

class ObjectDetection(Base):
    __tablename__ = "yolo_detection"

    id = Column(Integer, primary_key=True, index=True)
    image = Column(String, index=True)
    class_id = Column(Integer)
    confidence = Column(Float)
    x_center = Column(Float)
    y_center = Column(Float)
    width = Column(Float)
    height = Column(Float)