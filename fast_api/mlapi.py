from fastapi import FastAPI


app=FastAPI()

@app.get("/")
async def scoring_endpoint():
    return {"hello":"world"}