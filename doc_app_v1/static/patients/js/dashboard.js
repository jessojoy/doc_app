// dashboard.js – small interactions for patient dashboard

document.addEventListener('DOMContentLoaded', () => {
  const navItems = document.querySelectorAll('.nav-item');
  const upcomingBtn = document.getElementById('btnNewAppt');

  // highlight active nav item
  navItems.forEach(btn => {
    btn.addEventListener('click', () => {
      navItems.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      // here you can route to other pages via location.href
      const section = btn.dataset.section;
      switch (section) {
        case 'profile':
          // window.location.href = '/patient/profile/';
          break;
        case 'book':
          // window.location.href = '/patient/book/';
          break;
        // etc...
      }
    });
  });

  // Book new appointment click handler
  if (upcomingBtn) {
    upcomingBtn.addEventListener('click', () => {
      // replace with your real booking URL
      // window.location.href = '/patient/book/';
      alert('Hook this button to your "Book Appointment" page.');
    });
  }

  // Quick actions buttons
  document.querySelectorAll('.qa-item').forEach(btn => {
    btn.addEventListener('click', () => {
      const action = btn.dataset.action;
      // route / open modals etc. as you wire backend
      switch (action) {
        case 'searchDoctors':
          // window.location.href = '/patient/search-doctor/';
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
      }
    });
  });
});
