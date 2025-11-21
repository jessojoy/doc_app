// Basic behaviour for patient portal sidebar + dashboard buttons

document.addEventListener('DOMContentLoaded', () => {
  const navItems = document.querySelectorAll('.nav-item');
  const newApptBtn = document.getElementById('btnNewAppt');

  // Sidebar navigation using data-go
  navItems.forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.getAttribute('data-go');
      if (target && target !== '#') {
        window.location.href = target;
      }
    });
  });

  // Hook up "Book New Appointment" button
  if (newApptBtn) {
    newApptBtn.addEventListener('click', () => {
      // Replace with real URL when you create it
      alert('Connect this button to your "Book Appointment" page.');
    });
  }

  // Quick actions (demo)
  document.querySelectorAll('.qa-item').forEach(btn => {
    btn.addEventListener('click', () => {
      const action = btn.dataset.action;
      switch (action) {
        case 'searchDoctors':
          alert('Search Doctors clicked');
          break;
        case 'viewHistory':
          alert('View Booking History clicked');
          break;
        case 'viewTreatments':
          alert('View Treatment Records clicked');
          break;
        case 'giveFeedback':
          alert('Give Feedback clicked');
          break;
        default:
          break;
      }
    });
  });
});
