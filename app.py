from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response, JSONResponse
from zoom_utils import apply_zoom_bytes
import uvicorn

app = FastAPI(title="Hand-Zoom Backend", version="1.0.0")

# Allow your Android device to call the API (same Wi-Fi LAN)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # tighten to your phone's origin/IP in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/upload-image/")
async def upload_image(
    file: UploadFile = File(...),
    zoom: float = Form(1.5)
):
    """
    Gallery mode: send a single image (form-data: file, zoom).
    Returns the zoomed JPEG bytes.
    """
    if zoom <= 0:
        raise HTTPException(status_code=400, detail="zoom must be > 0")

    data = await file.read()
    try:
        out_bytes = apply_zoom_bytes(data, zoom)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return Response(content=out_bytes, media_type="image/jpeg")


@app.post("/upload-frame/")
async def upload_frame(
    file: UploadFile = File(...),
    zoom: float = Form(1.5)
):
    """
    Live mode: send a single camera frame repeatedly (multipart/form-data).
    Returns the zoomed frame as JPEG bytes.
    Your Android app calls this in a loop (or on an interval).
    """
    if zoom <= 0:
        raise HTTPException(status_code=400, detail="zoom must be > 0")

    frame = await file.read()
    try:
        out_bytes = apply_zoom_bytes(frame, zoom)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return Response(content=out_bytes, media_type="image/jpeg")


# Optional: simple JSON echo of server version / config
@app.get("/")
def root():
    return JSONResponse({
        "name": "Hand-Zoom Backend",
        "version": "1.0.0",
        "routes": {
            "health": "GET /health",
            "gallery": "POST /upload-image/ (form-data: file, zoom)",
            "live_frame": "POST /upload-frame/ (form-data: file, zoom)"
        }
    })


if __name__ == "__main__":
    # Run with: python app.py
    # Or: uvicorn app:app --host 0.0.0.0 --port 8000 --reload
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
