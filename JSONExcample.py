import json
def readJson():
    # some JSON:
    x = '{ "name":"John", "age":30, "city":"New York"}'
    # parse x:
    y = json.loads(x)
    # the result is a Python dictionary:
    print(y["age"])

def writeJson():
    # สร้างข้อมูลที่เราต้องการแปลง(ประเภท dictionary)
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    # คำสั่งที่ใช้ในการแปลง
    y = json.dumps(x)
    # มาลองดูผลลัพธ์กัน
    print(y)
    
writeJson()
readJson()
