import cv2
import numpy as np

def apply_zoom_bytes(image_bytes: bytes, zoom_factor: float) -> bytes:
    """
    Zoom an image (bytes -> bytes). Keeps output size same as input by
    center-cropping then resizing.

    zoom_factor: >1.0 zooms in, ==1.0 no change, (>=0.5 allowed but <1.0 zooms out)
    """
    if zoom_factor <= 0:
        raise ValueError("zoom_factor must be > 0")

    # Decode JPEG/PNG bytes -> BGR image
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("Could not decode image bytes")

    h, w = img.shape[:2]

    # If zoom == 1 → return original bytes unchanged
    if abs(zoom_factor - 1.0) < 1e-6:
        _, buf = cv2.imencode(".jpg", img)
        return buf.tobytes()

    # Compute crop size
    new_w = max(1, int(w / zoom_factor))
    new_h = max(1, int(h / zoom_factor))

    # Center crop coordinates
    x1 = (w - new_w) // 2
    y1 = (h - new_h) // 2
    x2 = x1 + new_w
    y2 = y1 + new_h

    cropped = img[y1:y2, x1:x2]
    zoomed = cv2.resize(cropped, (w, h), interpolation=cv2.INTER_LINEAR)

    # Encode back to JPEG
    ok, buf = cv2.imencode(".jpg", zoomed, [cv2.IMWRITE_JPEG_QUALITY, 90])
    if not ok:
        raise RuntimeError("Failed to encode image")
    return buf.tobytes()
