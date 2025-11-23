document.querySelectorAll(".excluir").forEach(botao => {
    botao.addEventListener("click", (e) => {
        if (!confirm("Tem certeza que deseja excluir esta transação?")) {
            e.preventDefault();
        }
    });
});
