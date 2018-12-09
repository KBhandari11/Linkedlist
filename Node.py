#Creating a class that links one node to another
class Node(object):
    
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next
        
#Class that creates a linked list with it's method that acts as a queue
class LinkedList(object):
	def __init__(self, head= None):
		self.head = head
#adds a node at the end of the list
	def enqueue(self, data):
	   if not self.head:
	       self.head = Node(data=data)
	       return
	   current = self.head
	   while current.next_node:
	       current = current.next_node
	   current.next_node = Node(data=data)
    		
#Return the size of the list
	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.get_next()
		return count	

#Return the index value of the element in the list
	def search(self, data):
	    current = self.head
	    count = 0
	    index = " "
	    while current:
	    	count += 1
	    	if (current.get_data() == data):
	    		index = index+ " "+str(count) 
	    	current = current.get_next()
	    return (index)
	    
#Remove the first item of the list
	def dequeue(self):
		current = self.head
		data = current.get_data()
		self.head = current.get_next()
		if current is None:
			raise ValueError("Data not in list")
			
#Print the whole list
	def display(self):
		data = " "
		current = self.head 
		while current:
			data = data +" "+str(current.get_data())	
			current = current.get_next()
		return (data)
		

				



