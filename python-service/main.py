from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"status": "ok", "service": "python"}

@app.post("/relay")
async def relay_data(data: dict):
    target_url = "http://go-service:8080/process-user"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(target_url, json=data, timeout=5.0)
            response.raise_for_status()
            return response.json()
        except (httpx.RequestError, httpx.HTTPStatusError) as exc:
            return JSONResponse(
                status_code=status.HTTP_502_BAD_GATEWAY,
                content={"status": "Error", "message": f"Backend communication failed: {str(exc)}"}
            )
