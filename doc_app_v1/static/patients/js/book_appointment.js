document.addEventListener('DOMContentLoaded', () => {
  const btn = document.getElementById('bookBtn');
  if (!btn) return;

  btn.addEventListener('click', () => {
    alert('Appointment booked (front-end demo only).');
  });
});
