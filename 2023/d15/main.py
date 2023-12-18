import sys
with open(sys.argv[1],"r") as f:
    data = f.read().rstrip().split(",")

def hash(str):
    val=0
    for ch in str:
        val+=ord(ch)
        val*=17
        val%=256
    print("for word", str, "hash val: ", val)
    return val

print(hash("HASH"))

ans=0
print(data)
for word in data:
    ans+=hash(word) 
print(ans)

#p2
print("p2 start")

boxes = [{} for _ in range(256)]
for word in data:
    if "-" in word:
        label = word[:-1]
        op = "-"
    elif "=" in word:
        label = word.split("=")[0]
        num = word.split("=")[-1]
        op="="
    
    h = hash(label)
    if op == "=":
        if label in boxes[h]:
            boxes[h][label]=num
        else:
            boxes[h][label]=num
    elif op == "-":
        if label in boxes[h]:
            boxes[h].pop(label)

ans = 0
for i, box in enumerate(boxes):
    for j, (lbel, focal_len) in enumerate(box.items()):
        print(lbel)
        print(f"{i+1}*{j+1}*{int(focal_len)}")
        ans += (i+1)*(j+1)*int(focal_len)

print(ans)