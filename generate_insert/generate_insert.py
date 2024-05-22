import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_json_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def write_array_to_file_as_generic_type(file_path, array_data):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in array_data:
            file.write(f"{item}\n")

def generate_insert_queries(json_data, table_name):
    insert_queries = []
    
    for data in json_data:
        fields = list(data.keys())
        
        values = []
        for field in fields:
            if isinstance(data[field], str) and data[field] == '':
                values.append('null')
            elif isinstance(data[field], str):
                values.append(f"'{data[field]}'")
            else:
                values.append(str(data[field]))
        
        values_str = ', '.join(values)
        fields_str = ', '.join([f'"{field}"' for field in fields])
        
        insert_query = f"""
            INSERT INTO {table_name} ({fields_str})
            VALUES ({values_str});
        """
        insert_queries.append(insert_query.strip())
    
    return insert_queries

def main():
    # Nome da tabela
    table_name = "product"

    # Carregar dados JSON
    json_data = load_json_file_content('generate_insert/json/example_json_product.json')
    
    # Gerar instruções INSERT
    insert_queries = generate_insert_queries(json_data, table_name)
    
    # Nome do arquivo de saída
    file_name = 'insert_products.sql'
    
    # Salvar instruções INSERT no arquivo
    write_array_to_file_as_generic_type(file_name, insert_queries)
    
    # Log de sucesso
    logger.info(f"✅Foram gerados {len(insert_queries)} INSERTs e salvos em {file_name}")

if __name__ == "__main__":
    main()
