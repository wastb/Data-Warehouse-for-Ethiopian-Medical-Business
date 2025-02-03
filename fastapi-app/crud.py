from sqlalchemy.orm import Session
import models, schemas

# Retrieve all YOLO detections with pagination
def get_detections(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ObjectDetection).offset(skip).limit(limit).all()

# Retrieve a single detection by ID
def get_detection(db: Session, id: int):
    return db.query(models.ObjectDetection).filter(models.ObjectDetection.id == id).first()

# Create a new YOLO detection
def create_detection(db: Session, detection: schemas.ObjectDetectionCreate):
    new_detection = models.ObjectDetection(
        image=detection.image,
        class_id=detection.class_id,
        confidence=detection.confidence,
        x_center=detection.x_center,
        y_center=detection.y_center,
        width=detection.width,
        height=detection.height
    )
    db.add(new_detection)
    db.commit()
    db.refresh(new_detection)
    return new_detection

# Update an existing YOLO detection
def update_detection(db: Session, detection_id: int, detection_update: schemas.ObjectDetectionUpdate):
    detection = db.query(models.ObjectDetection).filter(models.ObjectDetection.id == detection_id).first()
    if detection:
        detection.image = detection_update.image
        detection.class_id = detection_update.class_id
        detection.confidence = detection_update.confidence
        detection.x_center = detection_update.x_center
        detection.y_center = detection_update.y_center
        detection.width = detection_update.width
        detection.height = detection_update.height
        db.commit()
        db.refresh(detection)
        return detection
    return None  # If detection not found

# Delete a YOLO detection
def delete_detection(db: Session, detection_id: int):
    detection = db.query(models.ObjectDetection).filter(models.ObjectDetection.id == detection_id).first()
    if detection:
        db.delete(detection)
        db.commit()
        return True
    return False  # If detection not found

