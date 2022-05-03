from timeit import default_timer as timer

# Number of processes
P = 4

# Number of resources
R = 3

# Function to find the need of each process
def calculateNeed(need, maxm, allot):
	for i in range(P):
		for j in range(R):
			need[i][j] = maxm[i][j] - allot[i][j]


# Function to find the system is insafe state or not
def isSafe(processes, avail, maxm, allot):
	need = []
	for i in range(P):
		l = []
		for j in range(R):
			l.append(0)
		need.append(l)

	calculateNeed(need, maxm, allot)

	finish = [0] * P
	
	safeSeq = [0] * P

	work = [0] * R
	for i in range(R):
		work[i] = avail[i]

	count = 0
	while (count < P):
		found = False
		for p in range(P):
		
			if (finish[p] == 0):
				for j in range(R):
					if (need[p][j] > work[j]):
						break
					
				if (j == R - 1):
					for k in range(R):
						work[k] += allot[p][k]
					safeSeq[count] = p
					count += 1
					finish[p] = 1

					found = True
				
		if (found == False):
			print("System is not in safe state")
			return False

	print("System is in safe state. ✅",
			"\nSafe sequence is: ", end = " ")
	print(*safeSeq)

	return True

if _name_ =="_main_":

	start = timer()

	print('Normal Bankers Algorithm Runtime')
	
	processes = [0, 1, 2, 3]
	avail = [9, 1, 4]
	maxm = [[3, 2, 2], [6, 1, 3], [3, 1, 4], [4, 2, 2]]

	allot = [[1, 0, 0], [6, 1, 2], [2, 1, 1], [0, 0, 2]]
	
	isSafe(processes, avail, maxm, allot)
	end = timer()

print(end - start)