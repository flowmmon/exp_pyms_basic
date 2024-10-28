from sanic import Sanic,response
app=Sanic("Sample_HTTP_Api")
app.config.FALLBACK_ERROR_FORMAT="json"

@app.get("/v1/devices",ignore_body=False)
async def get_devices(request):
    return response.json(
        {
            "status":0,
            "message":"get_devices API not completed."
        }
    )

@app.post("/v1/devices")
async def add_devices(request):
    return response.json(
        {
            "status":0,
            "message":"add_devices API not completed."
        }
    )

@app.put("/v1/devices")
async def update_devices(request):
    return response.json(
        {
            "status":0,
            "message":"update_devices API not completed."
        }
    )

@app.delete("/v1/devices")
async def delete_devices(request):
    return response.json(
        {
            "status":0,
            "message":"delete_devices API not completed."
        }
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,single_process=True)