// profile.js – basic navigation + edit button placeholder

document.addEventListener('DOMContentLoaded', () => {
  // make sidebar buttons navigate via the data-go attribute
  document.querySelectorAll('.nav-item').forEach(btn => {
    const target = btn.getAttribute('data-go');
    if (target && target !== '#') {
      btn.addEventListener('click', () => {
        window.location.href = target;
      });
    }
  });

  // Edit Profile button – hook this to your real edit form later
  const editBtn = document.getElementById('btnEditProfile');
  if (editBtn) {
    editBtn.addEventListener('click', () => {
      alert('Hook this to your "Edit Profile" page or modal.');
    });
  }
});
