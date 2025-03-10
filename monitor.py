
#### **monitor.py**
```python
import subprocess
import sys
import json

def ping(host, count=5):
    cmd = ["ping", "-c", str(count), host]
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        lines = result.stdout.split("\n")
        summary = [line for line in lines if "rtt" in line]
        return {"host": host, "status": "reachable", "details": summary}
    else:
        return {"host": host, "status": "unreachable"}

if len(sys.argv) > 1:
    result = ping(sys.argv[1])
    print(json.dumps(result, indent=4))
else:
    print("Usage: python monitor.py <hostname>")
