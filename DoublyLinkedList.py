from DoublyLinkedList import DoublyLinkedList

def merge_linked_lists(srt_lst1,srt_lst2):
	def merge_sublists(node1,node2,acc):
		#BASE CASE
		if node1 == srt_lst1.trailer:
			while node2.next != None:
				acc.add_last(node2.data)
				node2 = node2.next
			return acc
		elif node1 == srt_lst2.trailer:
			while node1.next != None:
				acc.add_last(node1.data)
				node1 = node1.next
			return acc
		elif node1 == srt_lst1.trailer and node2 == srt_lst2.trailer:
			return acc

		#RECURSIVE CASE
		if node2.data>node1.data:
			acc.add_last(node1.data)
			return merge_sublists(node1.next, node2,acc)
		elif node1.data>node2.data:
			acc.add_last(node2.data)
			return merge_sublists(node1, node2.next,acc)
		else:
			acc.add_last(node2.data)
			acc.add_last(node1.data)
			return merge_sublists(node1.next, node2.next,acc)
	if srt_lst1.is_empty():
		return srt_lst2
	elif srt_lst2.is_empty():
		return srt_lst1
	else:
		cursor1 = srt_lst1.first_node()
		cursor2 = srt_lst2.first_node()
		return merge_sublists(cursor1,cursor2,DoublyLinkedList())
	#
