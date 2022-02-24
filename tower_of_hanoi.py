def tower_of_hanoi(n,source,helper,target):

	if n==1:  #base case
		print("Move disk 1 from rod",source,"to the rod",target)
		return

	tower_of_hanoi(n-1,source,target,helper) #recursive call

	print("Move the disk",n,"from rod",source,"to rod",target)

	tower_of_hanoi(n-1,helper,source,target) #recursive call

n=3 #number of disks

source="A" #the disks are initially present here
helper="B" 
target="C" #final destination of the disks

tower_of_hanoi(n,source,helper,target)

