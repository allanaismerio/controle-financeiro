// Futuramente você pode adicionar alertas, gráficos, etc.
// Exemplo simples de confirmação de exclusão:
document.querySelectorAll(".excluir").forEach(botao => {
    botao.addEventListener("click", (e) => {
        if (!confirm("Tem certeza que deseja excluir esta transação?")) {
            e.preventDefault();
        }
    });
});
