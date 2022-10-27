from typing import Dict
import uvicorn
from fastapi import FastAPI
import json
import http3

url = "http://nd-arb-3:8545"

payload = {
  "jsonrpc": "2.0",
  "method": "eth_syncing",
  "params": [],
  "id": 67
}
headers = {
  'Content-Type': 'application/json'
}

app = FastAPI()

@app.get("/")
def root ():
    return {"message": "Hello Avi"}


client = http3.AsyncClient()
async def call_api(urlCheck: str, json = Dict):

    r = await client.post(urlCheck,json)
    return r.text


@app.get("/sync")
async def index():
      resp = await client.post(url,json={"jsonrpc":"2.0","method":"eth_syncing","params":[],"id":67})
      #result = await client.get(url)
      data = resp.text
      parsed = json.loads(data)
      return parsed['result']
      

 # at last, the bottom of the file/module
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    
# https://stackoverflow.com/questions/70815650/fast-api-shows-msg-field-required-type-value-error-missing