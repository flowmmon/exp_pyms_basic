# 从 Sanic 中引入日志模块  
from sanic.log import logger  

# 编写用于生成测试数据的函数  
def init_device_data():  
    import random  
    import string  
    import time  
    from datetime import datetime  

    gen_random_num = lambda x: "".join(random.choices(string.digits, k=x))  
    gen_random_str = lambda x: "".join(random.choices(string.ascii_letters, k=x))  

    return [  
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

sample_device_data = init_device_data()  
logger.info(f"自动创建如下 ID 的设备：{[device['id'] for device in sample_device_data]}")