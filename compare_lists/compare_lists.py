def list_difference(list_a, list_b):
    in_a_not_in_b = list(set(list_a) - set(list_b))
    in_b_not_in_a = list(set(list_b) - set(list_a))
    
    difference = []
    for item in in_a_not_in_b:
        difference.append(f"O item '{item}' existe na lista A, mas não na lista B")
    for item in in_b_not_in_a:
        difference.append(f"O item '{item}' existe na lista B, mas não na lista A")
    
    return difference

def save_to_file(data, filename="difference_output.txt"):
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

# Insira as listas que deseja comparar
list_a = [
    'aefefa47-396e-48fe-a6ef-48a8a4ad9237',
    'f5a12c59-a52c-486e-b647-46aef84c9132',
    'bae00aff-a241-4754-86f0-8b7c0b096d2b',
    '9d81f9d0-c692-47a1-b90f-b0cd4cbd285f',
    'c45edb09-5807-446d-8bb0-f579355a6972'
]

# Insira as listas que deseja comparar
list_b = [
    'aefefa47-396e-48fe-a6ef-48a8a4ad9237',
    'f5a12c59-a52c-486e-b647-46aef84c9132',
    'bae00aff-a241-4754-86f0-8b7c0b096d2b',
    '9d81f9d0-c692-47a1-b90f-b0cd4cbd285f'
]

difference = list_difference(list_a, list_b)
print('✅Arquivo salvo com sucesso, verifique o arquivo "difference_output.txt"')

save_to_file(difference)
