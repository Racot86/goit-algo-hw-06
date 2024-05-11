У завданні зроблена симуляція доставки товару торгівельним судном на якому я зараз працюю.

**Висновки до Завдання 2**

Якщо брати за початкову вершину порт Ningbo:
    
    DFS:

        Ningbo - Shanghai - Los Angeles - Oakland - Honolulu - Dutch Harbour - Pusan - Kwangyang - Incheon
        
        Висновок: Через те що DFS шукає у глибину, пошук видав найдовшу гілку

    BFS:

        Ningbo - Shanghai - Los Angeles - Oakland(Dutch Harbor)(Honolulu - Pusan) - Kwangyang - Incheon

        Висновок: Через те що BFS шукає по ширині, пошук видав дерево з усіма можливми пов'язаними вершинами

На цьому прикладі можна побачити що BFS знайде значно коротший шлях.  