function listarProduto() {
    fetch(`http://127.0.0.1:8000/produto/`)
        .then(response => response.json())
        .then(produtos => {
            const lista = document.getElementById('lista');
            lista.innerHTML = ''; // limpa a lista antes de adicionar os itens

            produtos.forEach(produto => {
                const item = document.createElement('li');
                item.className = 'list-group-item d-flex justify-content-between align-items-center';
                item.innerHTML = `
                    <div>
                        <strong>${produto.nome}</strong> — ID: ${produto.id}
                    </div>
                    <div>
                        <button class="btn btn-sm btn-primary me-2" onclick="editarProduto(${produto.id})">Editar</button>
                        <button class="btn btn-sm btn-danger" onclick="deletarProduto(${produto.id}, this)">Excluir</button>
                    </div>`;
                lista.appendChild(item);
            });
        })
        .catch(error => console.error('Erro ao buscar produtos:', error));
}

function deletarProduto(id, botao) {
    if (!confirm('Tem certeza que deseja excluir este produto?')) return;

    fetch(`http://127.0.0.1:8000/produto/${id}/`, {
        method: 'DELETE'
    })
    .then(response => {
        if (response.ok) {
            // Remove o item da lista
            const item = botao.closest('li');
            if (item) item.remove();
        } else {
            alert('Erro ao excluir produto.');
        }
    })
    .catch(error => {
        console.error('Erro ao excluir produto:', error);
        alert('Erro ao excluir produto.');
    });
}

function editarProduto(id) {
    // Você pode implementar isso depois
    alert(`Função editarProduto ainda não implementada. ID: ${id}`);
}
