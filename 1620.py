num_pokemon, num_prob = map(int, input().split())

pokemon_dict = {}
pokemon_list = []

for i in range(num_pokemon):
    pokemon_name = input()
    pokemon_list.append(pokemon_name)
    pokemon_dict[pokemon_name] = i+1
    
for i in range(num_prob):
    prob = input()
    if prob.isdigit():
        print(pokemon_list[int(prob)-1])
    else:
        print(pokemon_dict[prob])