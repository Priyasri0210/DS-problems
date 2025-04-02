#efficiently using the memory
#Traditional way of storing all the contents in memory
with open('E:/Git/DS-problems/Classes/advanced/sample.txt','r') as f:
    data = f.readlines()
    
for i in data:
    print(i)

#generators - it won't store all the contents in the memory at a time
#yield

def log_generator():
    with open('E:/Git/DS-problems/Classes/advanced/sample.txt','r') as f:
        for line in f:
            yield line

for log in log_generator():
    print(log)
