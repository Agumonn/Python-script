'''
4-5) Simulate the shop queue

Add new persons to the queue from the list and serve them
in "shop queue":

# initialize list with the values
clients=['first', 'second', "third", "fourth", "fifth"]
queue=[]
# to do - serve a client and then remove them from the queue
# add new client into the queue


Example Output of the simulation: 

Now there are client in the queue:  ['first', 'second', 'third', 'fourth', 'fifth']
Serving client: first
Serving client: second
Serving client: third
Serving client: fourth
Serving client: fifth
Queue is now empty

Extra) How this simulation works if there is a priority for these clients?
'''
def getSortKey(item):
   return item[1]
#client list with priority number
clients=[('first',1), ('second',2), ('third',2), ('fourth',1), ('fifth',3)]
clientsort=(sorted(clients, key=getSortKey))
#clients sorted by priority
queue=[]
served=[]

print("This is the prioritised queue") 
print("The number after the client is the priority number for example 1,2,3") 

for i in clientsort[:]:
   queue.append(i)
   clientsort.remove(i)
   print("now serving client:",queue)
   served.append(i)
   queue.remove(i)
   if queue==[] and clientsort==[]:
     print("queue is now empty")
	 
