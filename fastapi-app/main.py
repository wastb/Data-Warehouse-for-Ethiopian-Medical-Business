from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

# Create database tables (if not already created)
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API Route: Get all YOLO detections (pagination)
@app.get("/detections/", response_model=list[schemas.ObjectDetection])
def read_detections(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_detections(db, skip=skip, limit=limit)

# API Route: Get a single YOLO detection by ID
@app.get("/detections/{id}", response_model=schemas.ObjectDetection)
def read_detection(id: int, db: Session = Depends(get_db)):
    detection = crud.get_detection(db, id=id)
    if detection is None:
        raise HTTPException(status_code=404, detail="Detection not found")
    return detection

# API Route: Create a new YOLO detection
@app.post("/detections/", response_model=schemas.ObjectDetection)
def create_detection(detection: schemas.ObjectDetectionCreate, db: Session = Depends(get_db)):
    return crud.create_detection(db, detection)

# API Route: Update an existing YOLO detection
@app.put("/detections/{id}", response_model=schemas.ObjectDetection)
def update_detection(id: int, detection_update: schemas.ObjectDetectionUpdate, db: Session = Depends(get_db)):
    updated_detection = crud.update_detection(db, id, detection_update)
    if updated_detection is None:
        raise HTTPException(status_code=404, detail="Detection not found")
    return updated_detection

# API Route: Delete a YOLO detection
@app.delete("/detections/{id}")
def delete_detection(id: int, db: Session = Depends(get_db)):
    success = crud.delete_detection(db, id)
    if not success:
        raise HTTPException(status_code=404, detail="Detection not found")
    return {"detail": "Detection deleted successfully"}
