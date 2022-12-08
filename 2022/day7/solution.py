import json

data = []
with open('test.in', 'r') as f:
    for line in f.readlines():
        data.append(line.strip())
        print(line.strip())

# Just find what each folder contains
curr_dir = None
filesystem = {}
len_latest_dir = 0
for i, line in enumerate(data):
    line = line.split()
    if line[0] == '$' and line[1] == 'cd':
        if line[2] != '..':
            if line[2] == '/':
                curr_dir = ''
            else:
                curr_dir = curr_dir + '/' + line[2]
        else:
            len_latest_dir = len(line[2])
            curr_dir = curr_dir[:-len_latest_dir]
        
    elif line[0] == '$' and line[1] == 'ls':
        stuff = []
        for inner in data[i+1:]:
            inner = inner.split()
            if inner[0] == '$':
                break
            stuff.append((inner[0], inner[1]))
        #print(f"Folder '{curr_dir}'\n Contains:{stuff}")
        
        filesystem[curr_dir if curr_dir != '' else '/'] = stuff

print(json.dumps(filesystem, indent=2))

# Now we have all folders and what they contain

for k, v in filesystem.items():
    curr_dir = '/'
    for item in v:
        first, second = item

        if first == 'dir':
            curr_dir += second

"""
size_of_folder = {}

for k, v in filesystem.items():
    tot_size = 0
    for item in v:
        first, second = item
        if first == 'dir':
            # Look up that dir in the
            # dict and find its size
            pass
        else:
            tot_size += int(first)
            
    if k in size_of_folder:
        print(k)
    size_of_folder[k] = tot_size
    
#print(json.dumps(size_of_folder, indent=4))

size_folder_all = {}

for k, v in filesystem.items():
    curr_dir = k
    tot_size = 0
    for item in v:
        if item[0]=='dir':
            print(item[1])
            tot_size += size_of_folder['/'+item[1]] 
        else:
            tot_size += int(item[0])
    size_folder_all[curr_dir] = tot_size

#print(json.dumps(size_folder_all, indent=4))

tot_size = 0
for k, v in size_folder_all.items():
    if v <= 100_000:
        tot_size += v
print(tot_size)
"""

# 1. go through all lines in data
# 2a. capture all files in array
# 2b. capture all dirs in array/map