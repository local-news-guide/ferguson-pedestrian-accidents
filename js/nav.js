/* Ferguson & Ferguson — Navigation
   Hamburger toggle + dropdown behavior
   ================================================ */
(function () {
  'use strict';

  var toggle = document.querySelector('.ff-nav-toggle');
  var nav    = document.querySelector('.ff-nav');

  /* ---- Hamburger ---- */
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      nav.classList.toggle('active');
      toggle.classList.toggle('active');
      toggle.setAttribute('aria-expanded', nav.classList.contains('active'));
    });
  }

  /* ---- Dropdown (Service Areas) ---- */
  var dropdowns = document.querySelectorAll('.ff-nav__dropdown');

  dropdowns.forEach(function (dd) {
    var btn  = dd.querySelector('.ff-nav__dropdown-toggle');
    var menu = dd.querySelector('.ff-nav__dropdown-menu');
    if (!btn || !menu) return;

    /* Click / tap to open */
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      var wasOpen = dd.classList.contains('open');

      /* Close all dropdowns first */
      dropdowns.forEach(function (d) { d.classList.remove('open'); });

      if (!wasOpen) dd.classList.add('open');
    });

    /* Desktop: open on hover */
    dd.addEventListener('mouseenter', function () {
      if (window.innerWidth > 600) dd.classList.add('open');
    });
    dd.addEventListener('mouseleave', function () {
      if (window.innerWidth > 600) dd.classList.remove('open');
    });
  });

  /* Close dropdown when clicking outside */
  document.addEventListener('click', function (e) {
    dropdowns.forEach(function (dd) {
      if (!dd.contains(e.target)) dd.classList.remove('open');
    });
  });

  /* Close mobile nav when a link is clicked */
  if (nav) {
    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        if (window.innerWidth <= 600) {
          nav.classList.remove('active');
          toggle.classList.remove('active');
          toggle.setAttribute('aria-expanded', 'false');
        }
      });
    });
  }
})();
