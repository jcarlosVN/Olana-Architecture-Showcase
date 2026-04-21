"""
FastAPI Routes - Showcase Version
Highlights asynchronous endpoint design and background task integration.
"""

from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from typing import List

app = FastAPI(title="Olana Recovery API")

@app.post("/report/lost")
async def report_lost_pet(
    files: List[UploadFile] = File(...),
    location_data: str = None
):
    """
    Endpoint for reporting a lost pet.
    Triggering background analysis via Celery for non-blocking UI.
    """
    # 1. Save images to GridFS (abstracted)
    # 2. Trigger Background Task
    # process_pet_matching.delay(pet_id)
    return {"message": "Pet report received. Analysis in progress.", "request_id": "olana-uuid-001"}

@app.get("/matches/{request_id}")
async def get_matches(request_id: str):
    """
    Fetches processed matches.
    Demonstrates the separation of submission and retrieval for heavy AI tasks.
    """
    return {
        "request_id": request_id,
        "status": "completed",
        "matches": [
            {"id": "found-001", "confidence": "0.98", "ai_reasoning": "Matching star-shaped chest patch."}
        ]
    }
