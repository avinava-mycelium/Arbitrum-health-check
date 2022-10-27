import uvicorn
from fastapi import FastAPI
import json
import http3

url = "http://nd-arb-1:8545"

app = FastAPI()

@app.get("/")
def root ():
    return {"message": "Hello Avi"}

client = http3.AsyncClient()
@app.get("/sync")
async def index():
      resp = await client.post(url,json={"jsonrpc":"2.0","method":"eth_syncing","params":[],"id":67})
      data = resp.text
      parsed = json.loads(data)
      return parsed['result']
      

 # at last, the bottom of the file/module
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    
# https://stackoverflow.com/questions/70815650/fast-api-shows-msg-field-required-type-value-error-missing