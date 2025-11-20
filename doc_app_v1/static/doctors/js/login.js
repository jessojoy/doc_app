// login.js — put in static/doctors/js/

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('loginForm');
  const toast = document.getElementById('toast');

  // show toast helper
  function showToast(message, ok=true){
    toast.textContent = message;
    toast.style.background = ok ? 'rgba(2,143,158,0.95)' : 'rgba(176,0,32,0.95)';
    toast.classList.add('show');
    setTimeout(()=> toast.classList.remove('show'), 2600);
  }

  // clear field errors on input
  document.querySelectorAll('input').forEach(inp => {
    inp.addEventListener('input', () => {
      const box = document.querySelector('.field-error[data-field="'+inp.name+'"]');
      if (box) box.textContent = '';
    });
  });

  // simple client-side validation; allow server to handle authentication
  form.addEventListener('submit', (e) => {
    const username = form.username ? form.username.value.trim() : form.elements['username'].value.trim();
    const password = form.password ? form.password.value : form.elements['password'].value;

    let hasError = false;
    if (!username || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(username)) {
      e.preventDefault();
      const el = document.querySelector('.field-error[data-field="username"]');
      if (el) el.textContent = 'Please enter a valid email.';
      hasError = true;
    }
    if (!password || password.length < 4) {
      e.preventDefault();
      const el = document.querySelector('.field-error[data-field="password"]');
      if (el) el.textContent = 'Please enter your password.';
      hasError = true;
    }

    if (hasError) {
      showToast('Please fix the highlighted errors', false);
      return;
    }

    // Optionally show a loading state — let server handle the POST
    const btn = document.getElementById('loginBtn');
    if (btn) { btn.disabled = true; btn.textContent = 'Signing in...'; }
    // If you want AJAX login, replace default submit with fetch here.
  });
});
