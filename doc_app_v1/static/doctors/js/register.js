// register.js — light client-side validation & UX

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('registerForm');
  const btn = document.getElementById('registerBtn');

  function setError(fieldName, message) {
    const el = document.querySelector('.field-error[data-field="'+fieldName+'"]');
    if (el) el.textContent = message;
  }

  form.addEventListener('submit', (e) => {
    // clear previous errors
    document.querySelectorAll('.field-error').forEach(n => n.textContent = '');

    const fullName = (form.full_name && form.full_name.value.trim()) || '';
    const email = (form.email && form.email.value.trim()) || '';
    const p1 = (form.password1 && form.password1.value) || '';
    const p2 = (form.password2 && form.password2.value) || '';

    let hasError = false;
    if (!fullName) { setError('full_name', 'Please enter your name'); hasError = true; }
    if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) { setError('email', 'Please enter a valid email'); hasError = true; }
    if (p1 && p2 && p1 !== p2) { setError('password2', 'Passwords do not match'); hasError = true; }

    if (hasError) {
      e.preventDefault();
      btn.scrollIntoView({ behavior: 'smooth', block: 'center' });
    } else {
      // optional: disable button to avoid double submit
      btn.disabled = true;
      btn.textContent = 'Registering...';
    }
  });

  // clear error when user types
  document.querySelectorAll('input, select').forEach(inp => {
    inp.addEventListener('input', () => {
      const box = document.querySelector('.field-error[data-field="'+inp.name+'"]');
      if (box) box.textContent = '';
    });
  });
});
