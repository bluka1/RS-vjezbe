import heapq

def dijkstra(graph, start):
  udaljenosti = {cvor: float('inf') for cvor in graph}
  udaljenosti[start] = 0
  
  red_prioriteta = [(0, start)]
  posjeceni = set()

  while red_prioriteta:
    trenutna_udaljenost, trenutni_cvor = heapq.heappop(red_prioriteta)
    
    if trenutni_cvor in posjeceni:
      continue
    
    posjeceni.add(trenutni_cvor)
    
    for susjed, udaljenost_susjeda in graph[trenutni_cvor]:
      nova_udaljenost = trenutna_udaljenost + udaljenost_susjeda
      
      if nova_udaljenost < udaljenosti[susjed]:
        udaljenosti[susjed] = nova_udaljenost
        heapq.heappush(red_prioriteta, (nova_udaljenost, susjed))
  
  return udaljenosti

graph = {
  'A': [('B', 1), ('C', 4)],
  'B': [('A', 1), ('C', 2), ('D', 5)],
  'C': [('A', 4), ('B', 2), ('D', 1)],
  'D': [('B', 5), ('C', 1)]
}

print(dijkstra(graph, 'A'))