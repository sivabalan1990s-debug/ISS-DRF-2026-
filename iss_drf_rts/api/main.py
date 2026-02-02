from fastapi import FastAPI
from iss_drf_rts.core.verify import verify_profile
# If the above import fails, use:
# from core.verify import verify_profile

app = FastAPI(title="ISS-DRF Real-Time Verification API")


@app.get("/")
def root():
    """
    Health check endpoint.
    """
    return {"status": "ISS-DRF RTS running"}


@app.post("/verify")
def verify(profile: dict):
    """
    Verify a researcher profile using ISS-DRF trust logic.
    """
    return verify_profile(profile)
