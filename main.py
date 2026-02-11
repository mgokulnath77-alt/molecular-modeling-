from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import random

app = FastAPI()

# Mock Data for Interaction Analysis
@app.get("/api/docking-results")
async def get_results():
    return {
        "binding_energy": -8.4,
        "stability": "High",
        "h_bonds": 3,
        "vdw_forces": 12,
        "poses": [
            {"id": 1, "energy": -8.4, "affinity": "Strong"},
            {"id": 2, "energy": -7.1, "affinity": "Moderate"},
            {"id": 3, "energy": -6.5, "affinity": "Weak"}
        ]
    }

@app.post("/api/upload-protein")
async def upload_protein(file: File(...)):
    return {"status": "success", "filename": file.filename, "residues": 548, "chains": 2}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)