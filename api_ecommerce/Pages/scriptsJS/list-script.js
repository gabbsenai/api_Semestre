function listarCategoria() {
    fetch(`http://127.0.0.1:8000/categoria/`)
    .then(response => response.json())
    .then(categorias => {
        const lista = document.getElementById('lista');
        lista.innerHTML = ''; // limpa a lista antes de adicionar os itens

        categorias.forEach(categoria => {
            const item = document.createElement('li');
            item.className = 'list-group-item d-flex justify-content-between align-items-center';
            item.innerHTML = `
                <div>
                    <strong>${categoria.nome}</strong> — ID: ${categoria.id}
                </div>
                <div>
                    <button class="btn btn-sm btn-primary me-2" onclick="editarCategoria(${categoria.id})">Editar</button>
                    <button class="btn btn-sm btn-danger" onclick="excluirCategoria(${categoria.id}, this)">Excluir</button>
                </div>`;
            lista.appendChild(item);
        });
    })
    .catch(error => console.error('Erro ao buscar categorias:', error));
}

function deletarCategoria(id, botao) {
    if (!confirm('Tem certeza que deseja excluir esta categoria?')) return;

    fetch(`http://127.0.0.1:8000/categoria/${id}/`, {
        method: 'DELETE'
    })
    .then(response => {
        if (response.ok) {
            // Remove o item da tela (pai do botão)
            const item = botao.closest('li');
            if (item) item.remove();
        } else {
            alert('Erro ao excluir categoria.');
        }
    })
    .catch(error => {
        console.error('Erro ao excluir categoria:', error);
        alert('Erro ao excluir categoria.');
    });
}
