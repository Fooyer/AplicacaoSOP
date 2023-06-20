# Estrutura de dados para representar um bloco de memória
class MemoryBlock:
    def __init__(self, start_address, size):
        self.start_address = start_address
        self.size = size
        self.allocated = False

# Tamanho total da memória disponível
total_memory = 1024  # 1GB = 1024MB

# Lista de blocos de memória disponíveis
memory_blocks = [MemoryBlock(0, total_memory)]

# Função para alocar memória usando o algoritmo worst-fit
def allocate_memory_worst_fit(size):
    worst_fit_block = None
    for block in memory_blocks:
        if not block.allocated and block.size >= size:
            if worst_fit_block is None or block.size > worst_fit_block.size:
                worst_fit_block = block

    if worst_fit_block is not None:
        worst_fit_block.allocated = True
        if worst_fit_block.size - size > 0:
            new_block = MemoryBlock(worst_fit_block.start_address + size, worst_fit_block.size - size)
            memory_blocks.append(new_block)
            worst_fit_block.size = size
        return worst_fit_block.start_address

    return None

# Função para desalocar um espaço na memória
def deallocate_memory(address):
    for block in memory_blocks:
        if block.start_address == address and block.allocated:
            block.allocated = False
            merge_adjacent_blocks()
            return True
    return False

# Função auxiliar para realizar a fusão de blocos adjacentes não alocados
def merge_adjacent_blocks():
    global memory_blocks
    merged_blocks = []
    memory_blocks.sort(key=lambda block: block.start_address)

    i = 0
    while i < len(memory_blocks):
        current_block = memory_blocks[i]
        if i < len(memory_blocks) - 1:
            next_block = memory_blocks[i + 1]
            if not current_block.allocated and not next_block.allocated:
                merged_block = MemoryBlock(current_block.start_address, current_block.size + next_block.size)
                i += 1
            else:
                merged_block = current_block
        else:
            merged_block = current_block

        merged_blocks.append(merged_block)
        i += 1

    memory_blocks = merged_blocks

# Função para listar os blocos alocados
def list_allocated_blocks_w():
    allocated_blocks = [block for block in memory_blocks if block.allocated]
    if len(allocated_blocks) > 0:
        print("Blocos Alocados:")
        print("")
        for block in allocated_blocks:
            print(f"Endereço: {block.start_address}, Tamanho: {block.size}")
    else:
        print("Não há blocos alocados.")

# Função para listar os blocos não alocados
def list_unallocated_blocks_w():
    unallocated_blocks = [block for block in memory_blocks if not block.allocated]
    if len(unallocated_blocks) > 0:
        print("Blocos Não Alocados:")
        print("")
        for block in unallocated_blocks:
            print(f"Endereço: {block.start_address}, Tamanho: {block.size}")
    else:
        print("Não há blocos não alocados.")

def alocarMemoria_w(valor):
    allocated_address = allocate_memory_worst_fit(valor)

    if allocated_address is not None:
        print(f"Memória alocada com sucesso no endereço {allocated_address}.")
    else:
        print("Não há memória disponível para alocar 512MB.")

def desalocarMemoria_w(endereco):
    deallocated = deallocate_memory(endereco)

    if deallocated:
        print("Espaço de memória desalocado com sucesso.")
    else:
        print("Não foi possível desalocar o espaço de memória.")
