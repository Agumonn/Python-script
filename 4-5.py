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

clients=["first", "second", "third", "fourth", "fifth"]
queue=[]
served=[]

for i in clients[:]:
   queue.append(i)
   clients.remove(i)
   print("now serving client:",queue)
   served.append(i)
   queue.remove(i)
   if queue==[] and served==["first", "second", "third", "fourth", "fifth"]:
     print("queue is now empty")
