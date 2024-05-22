def format_ids(ids_string):
    ids_list = ids_string.strip().split('\n')
    formatted_ids = []
    
    for i, id in enumerate(ids_list):
        if i == len(ids_list) - 1:
            formatted_ids.append(f"'{id}'")
        else:
            formatted_ids.append(f"'{id}',")
    
    return '\n'.join(formatted_ids)

def save_to_file(formatted_output, filename="formatted_ids.txt"):
    with open(filename, 'w') as file:
        file.write(formatted_output)

# Insira os IDs que deseja formatar
input_ids = """
aefefa47-396e-48fe-a6ef-48a8a4ad9237
f5a12c59-a52c-486e-b647-46aef84c9132
bae00aff-a241-4754-86f0-8b7c0b096d2b
9d81f9d0-c692-47a1-b90f-b0cd4cbd285f
c45edb09-5807-446d-8bb0-f579355a6972
"""

formatted_output = format_ids(input_ids)
print('✅Arquivo salvo com sucesso, verifique o arquivo "formatted_ids.txt"')

save_to_file(formatted_output)
