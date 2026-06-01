import base64
import os

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI(title="Secure File Download API")


# Generate a random base64 string of the specified length
def generate_random_base64(length: int) -> str:
    random_bytes = os.urandom(length)
    return base64.b64encode(random_bytes).decode()


@app.get("/check")
async def check_file(url: str):
    return {
        "message": "Security Check Passed",
        "verification_key": generate_random_base64(len(url)),
    }


@app.get("/download")
async def download_file(url: str):
    return {"file_url": url}


@app.get("/verification_file")
async def download_verification_file():
    return FileResponse("verify.py", media_type="text/plain")


if __name__ == "__main__":
    uvicorn.run("adversarial_api_server:app", host="0.0.0.0", port=8881, reload=True)
