from heapq import heappush, heappop, heapify
from collections import defaultdict 

class HFCode:
	def encode(self,symb2freq):
		heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
		heapify(heap)
		while len(heap) > 1:
			lo = heappop(heap)
			hi = heappop(heap)
			for pair in lo[1:]:
				pair[1] = '0' + pair[1]
			for pair in hi[1:]:
				pair[1] = '1' + pair[1]
			heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
		return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

	def find(self, f, seq):
		count=0
		for item in seq:
			if (item[0]==f):
				return(count)
			count+=1
		return (count)

	def encode1(self, txt, huff):
		str = ""
		for ch in txt:
			ptr=self.find(ch,huff)
			binary = huff[ptr][1]
			#print (binary + '')
			str = str + binary
		return str  
