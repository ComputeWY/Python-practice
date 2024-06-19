hash_table = [0 for _ in range(100)]

def hash_function(key):
    return hash(key) % 100

def set_data(key,value):
    hash_value = hash_function(key)
    hash_table[hash_value] = value
    #인덱스가 숫자가 아니라 문자
    #따로 인덱스에 대한 명시가 없어도 된다.
    
def get_data(key):
    hash_value = hash_function(key)
    return hash_table[hash_value]

set_data('Rdav', 2022)
set_data('hello', 77)
print(get_data('Rdav'))
print(get_data('hello'))
print(hash_table)
