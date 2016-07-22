import re
import os

"""线上日志报参数错误：The object to be validated must not be null
    此对象用于解析IP调用方
"""
def read():
    result = {}
    pattern = re.compile(r'.*ip:(?P<ip>[\d\.]+)-.*"param":"".*')
    for root, dir, files in os.walk("E:\RTX\paramnull\logs"):
        for file in files:
            print(root)
            print(file)
            with open(os.path.join(root, file),encoding="UTF-8") as f:
                for row in f:
                    match = pattern.match(row)
                    if match:
                        ip = match.groupdict()["ip"]
                        if ip not in result:
                            result[ip] = 1
                        else:
                            result[ip] += 1
    print(result)



read()
