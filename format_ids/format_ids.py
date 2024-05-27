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
insira os ids aqui
"""

formatted_output = format_ids(input_ids)
print('✅Arquivo salvo com sucesso, verifique o arquivo "formatted_ids.txt"')

save_to_file(formatted_output)
