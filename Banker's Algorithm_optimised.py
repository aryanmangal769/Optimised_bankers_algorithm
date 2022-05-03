INT_MAX = 100000
import math

def count_sort(a,n,pos,idx):
    div = pow (10, pos)
    freq = [0] *10
    position = [0] *10

    for i in range(n):
        x = (a[idx[i]] // div) % 10
        freq[x] += 1

    final = [0] *(n)

    position[0] = 0
    for i in range (1,10):
        position[i] = position[i - 1] + freq[i - 1]

    for i in range(n):
        final[position[(a[idx[i]] // div) % 10]] = idx[i]
        position[(a[idx[i]] // div) % 10] += 1

    for i in range(n):
        idx[i] = final[i]

def radiax_sort(a, n):
    maxele = 1
    for i in range(n):
        maxele = max(maxele, a[i])

    maxdig = (int)(math.log10(maxele))
    idx = [0] *(n)
    for i in range(n):
        idx[i] = i

    for i in range(maxdig+1):
        count_sort (a, n, i, idx)

    return idx


def compute (available_resource, m):
    ans = INT_MAX
    for i in range(m):
        ans = min (ans, available_resource[i])

    return ans



global rows,cols,alloc,maxneed,r1,r2,r3,r4,r5,needed,initialavailable

nor = 3
nop = 4

available_resource = [0]*nor

needed = [[3, 2, 2], [6, 1, 3], [3, 1, 4], [4, 2, 2]]
alloc = [[1, 0, 0], [6, 1, 2], [2, 1, 1], [0, 0, 2]]

initialavailable =[2, 1, 4]

for i in range(nor):
    available_resource[i] = initialavailable[i]

safe_sequence = []
completed_process = [0]*(nop)
maximum_needed_allocation = [0]*(nop)
minimum_available = INT_MAX
for i in range(nop):
    imax = 0
    for j in range(nor):
        imax = max(imax, needed[i][j])
    maximum_needed_allocation[i] = imax
process = radiax_sort(maximum_needed_allocation, nop)
print(process)
isDeadLock = False

for i in range(nop):
    if (maximum_needed_allocation[i] <= minimum_available and completed_process[process[i]] == 0):
        completed_process[process[i]] = 1
        safe_sequence.append(process[i])
        s = f"Granted for P{process[i]+1} ✅"
        print(s)
        s = "Now Available Resources: "
        for j in range(nor):
            available_resource[j] = available_resource[j] + alloc[process[i]][j]
            s += str(available_resource[j]) + ", "
        print(s)
        minimum_available = compute(available_resource,nor)
    else:
        j = 0
        while(j<nor):
            if (needed[process[i]][j] <= available_resource[j]):
                j += 1
                continue 
            else:
                break
        if (j == nor):
            completed_process[process[i]] = 1
            safe_sequence.append(process[i])
            s = f"Granted for P{process[i]+1} ✅"
            print(s)
            s = "Now Available Resources : "
            for j in range(nor):
                available_resource[j] = available_resource[j] + alloc[process[i]][j]
                s += str(available_resource[j]) + ", "
            print(s)

            minimum_available = compute(available_resource,nor)
        else:
            isDeadLock = True
            break        

for i in range(nop):
    # // If anyone of them remains incomplete then deadlock
    if (completed_process[i] == 0):
        isDeadLock = True
        break

print("Analyzing")
if(isDeadLock):
    s = " 💀 DeadLock has Occured 💀"
    print(s)
    if(len(safe_sequence) == 0):
        s =  "No Process can be terminated"
        print(s)
    else:
        s = ""
        for i in range(len(safe_sequence)-1):
            s += f"P{safe_sequence[i]+1} , "
        s += f"and P{safe_sequence[len(safe_sequence)-1]+1} can be terminated but rest cannot be terminated. Hence DeadLock"
        print(s)
else:
    print("✅ System is Safe ✅")
    s = "Safe Sequence ▶ "
    for i in range(len(safe_sequence)-1):
        s += f"P{safe_sequence[i]+1}   ↣   "  
    s += f"P{safe_sequence[len(safe_sequence)-1]+1}"
    print(s)
