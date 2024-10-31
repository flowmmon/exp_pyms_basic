from sanic import Sanic,response 
from sanic.response import json  
from sanic.log import logger  
import random  
import string  
import time  
from datetime import datetime  

# 编写用于生成测试数据的函数  
def init_device_data():  
    gen_random_num = lambda x: "".join(random.choices(string.digits, k=x))  
    gen_random_str = lambda x: "".join(random.choices(string.ascii_letters, k=x))  

    device_list = [  
        {  
            "id": gen_random_num(10),  
            "name": gen_random_str(8),  
            "type": random.choice(["controller", "gateway", "adapter"]),  
            "hardware": {  
                "model": random.choice(["Raspberry Pi 4", "x86 PC"]),  
                "sn": gen_random_str(5)  
            },  
            "software": {  
                "version": f"{random.randint(1, 100)}.{random.randint(1, 100)}",  
                "last_update": datetime.fromtimestamp(time.time() - random.randint(1, 10000)).strftime("%Y-%m-%d %H:%M:%S")  
            },  
            "nic": [  
                {  
                    "type": random.choice(["eth", "wifi"]),  
                    "mac": ":".join([f"{random.randint(0, 255):02x}" for _ in range(6)]),  
                    "ipv4": ".".join([str(random.randint(1, 255)) for _ in range(4)]),  
                }  
                for _ in range(random.randint(1, 2))  
            ],  
            "status": random.choice(["online", "offline"])  
        }  
        for _ in range(5)  
    ]  

    # 打印设备 ID 列表  
    logger.info("Created device IDs: " + ", ".join([device["id"] for device in device_list]))  
    return device_list  

# 创建 Sanic 应用  
app = Sanic("DeviceQueryApp")  

# 在服务启动时生成设备数据  
sample_device_data = init_device_data()

app=Sanic("Sample_HTTP_Api")
app.config.FALLBACK_ERROR_FORMAT="json"

@app.get("/v1/devices", ignore_body=False)  
async def get_devices(request):  
    request_dict = request.json  
    if "id" in request_dict:  
        resp_data = [  
            device  
            for device in sample_device_data  
            if request_dict["id"] == device["id"]  
        ]  
    else:  
        if "sn" in request_dict and "model" in request_dict:  
            resp_data = [  
                device  
                for device in sample_device_data  
                if request_dict["sn"] == device["hardware"]["sn"]and request_dict["model"] == device["hardware"]["model"]  
            ]  
        else:  
            return response.json(  
                {  
                    "status": 0,  
                    "message": "请求参数错误"  
                }  
            )  

    return response.json(  
        {  
            "status": 1,  
            "message": "OK",  
            "data": resp_data  
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