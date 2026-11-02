import json

counts = {"HTTP_200": 0, "HTTP_401": 0, "HTTP_404": 0}

with open("requests.log") as f:
    for line in f:
        status = line.split()[-1] # status code is the last word
        key = "HTTP_" + status
        if key in counts: # matches status
            counts[key] += 1

with open("security_summary.json", "w") as f:
    json.dump(counts, f, indent=2)

print(counts)