from fastapi import FastAPI
from utils.configs import args
from fastapi.responses import JSONResponse
from fastapi import status
from routers import summary_app
app = FastAPI()

@app.get("/")
def read_root():
    """
    Welcome message to check if the server is running
    """
    return JSONResponse(
        {
            "status_code": status.HTTP_200_OK,
            "message": "Welcome to the Summary AI server",
        }
    )

if __name__ == "__main__":
    import uvicorn
    app.include_router(summary_app)
    uvicorn.run(app, host="0.0.0.0", port=4800)