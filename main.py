import uvicorn
from fastapi import FastAPI, Response

app=FastAPI()

@app.get("/")
async def base():
    the_message = f"This is the AWS EC2 feature. \nWe will use it to do authentication:) \nTo be continued..."
    rsp = Response(content=the_message, media_type="text/plain")
    return rsp

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8012)