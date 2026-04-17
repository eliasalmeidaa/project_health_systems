const API = "http://localhost:8000";

// ---- Utilitários ----

function badgeStatus(status) {
  const map = {
    "Operacional":   "badge-ok",
    "Em Manutenção": "badge-manutencao",
    "Inativo":       "badge-inativo",
  };
  const cls = map[status] || "badge-ok";
  return `<span class="badge ${cls}">${status}</span>`;
}

function mostrarMensagem(texto, tipo) {
  const el = document.getElementById("mensagem");
  el.textContent = texto;
  el.className = tipo; // "sucesso" ou "erro"
  setTimeout(() => { el.className = ""; el.style.display = "none"; }, 3500);
}

// ---- Listar ----

async function listar() {
  try {
    const res = await fetch(`${API}/equipamentos`);
    const dados = await res.json();
    const tbody = document.getElementById("tabela-body");

    if (!dados.length) {
      tbody.innerHTML = `<tr><td colspan="8" id="sem-dados">Nenhum equipamento cadastrado.</td></tr>`;
      return;
    }

    tbody.innerHTML = dados.map(e => `
      <tr>
        <td>${e.nome}</td>
        <td>${e.marca} / ${e.modelo}</td>
        <td>${e.numero}</td>
        <td>${e.registro}</td>
        <td>${e.setor}</td>
        <td>${badgeStatus(e.status)}</td>
        <td>${e.ultima_manutencao}</td>
        <td>
          <button class="btn-edit" onclick='iniciarEdicao(${JSON.stringify(e)})'>Editar</button>
          <button class="btn-delete" onclick="deletar('${e.numero}')">Excluir</button>
        </td>
      </tr>
    `).join("");
  } catch {
    mostrarMensagem("Erro ao conectar com a API. Verifique se ela está rodando.", "erro");
  }
}

// ---- Cadastrar / Editar ----

document.getElementById("form-equipamento").addEventListener("submit", async (e) => {
  e.preventDefault();

  const editNumero = document.getElementById("edit-numero").value;
  const dados = {
    nome:              document.getElementById("nome").value,
    marca:             document.getElementById("marca").value,
    modelo:            document.getElementById("modelo").value,
    numero:            document.getElementById("numero").value,
    registro:          document.getElementById("registro").value,
    setor:             document.getElementById("setor").value,
    status:            document.getElementById("status").value,
    ultima_manutencao: document.getElementById("ultima_manutencao").value,
  };

  try {
    let res;
    if (editNumero) {
      res = await fetch(`${API}/equipamentos/${editNumero}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dados),
      });
    } else {
      res = await fetch(`${API}/equipamentos`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dados),
      });
    }

    const result = await res.json();
    if (result.erro) {
      mostrarMensagem(result.erro, "erro");
    } else {
      mostrarMensagem(editNumero ? "Equipamento editado com sucesso!" : "Equipamento cadastrado com sucesso!", "sucesso");
      limparForm();
      listar();
    }
  } catch {
    mostrarMensagem("Erro ao salvar. Verifique a API.", "erro");
  }
});

// ---- Deletar ----

async function deletar(numero) {
  if (!confirm(`Deseja realmente excluir o equipamento ${numero}?`)) return;
  try {
    const res = await fetch(`${API}/equipamentos/${numero}`, { method: "DELETE" });
    const result = await res.json();
    if (result.erro) {
      mostrarMensagem(result.erro, "erro");
    } else {
      mostrarMensagem("Equipamento excluído.", "sucesso");
      listar();
    }
  } catch {
    mostrarMensagem("Erro ao excluir.", "erro");
  }
}

// ---- Editar (preenche o form) ----

function iniciarEdicao(e) {
  document.getElementById("form-titulo").textContent = "Editar Equipamento";
  document.getElementById("btn-submit").textContent = "Salvar Alterações";
  document.getElementById("btn-cancelar").style.display = "inline-block";

  document.getElementById("edit-numero").value         = e.numero;
  document.getElementById("nome").value                = e.nome;
  document.getElementById("marca").value               = e.marca;
  document.getElementById("modelo").value              = e.modelo;
  document.getElementById("numero").value              = e.numero;
  document.getElementById("numero").readOnly           = true;
  document.getElementById("registro").value            = e.registro;
  document.getElementById("setor").value               = e.setor;
  document.getElementById("status").value              = e.status;
  document.getElementById("ultima_manutencao").value   = e.ultima_manutencao;

  window.scrollTo({ top: 0, behavior: "smooth" });
}

function cancelarEdicao() {
  limparForm();
}

function limparForm() {
  document.getElementById("form-equipamento").reset();
  document.getElementById("edit-numero").value              = "";
  document.getElementById("numero").readOnly                = false;
  document.getElementById("form-titulo").textContent        = "Cadastrar Equipamento";
  document.getElementById("btn-submit").textContent         = "Cadastrar";
  document.getElementById("btn-cancelar").style.display     = "none";
}

// ---- Iniciar ----
listar();
