/* ============================================================
   Ferguson & Ferguson — Main JavaScript
   Handles: navigation, scroll animations, header behavior
   ============================================================ */

(function () {
  'use strict';

  /* --- Mobile Navigation Toggle --- */
  const navToggle = document.getElementById('navToggle');
  const mainNav = document.getElementById('mainNav');

  if (navToggle && mainNav) {
    navToggle.addEventListener('click', function () {
      mainNav.classList.toggle('active');
      navToggle.classList.toggle('active');
      document.body.classList.toggle('ff-nav-open');
    });

    // Close nav when clicking a link (mobile)
    mainNav.querySelectorAll('a:not(.ff-nav-dropdown__trigger)').forEach(function (link) {
      link.addEventListener('click', function () {
        mainNav.classList.remove('active');
        navToggle.classList.remove('active');
        document.body.classList.remove('ff-nav-open');
      });
    });
  }

  /* --- Dropdown Menus --- */
  document.querySelectorAll('.ff-nav-dropdown__trigger').forEach(function (trigger) {
    trigger.addEventListener('click', function (e) {
      e.preventDefault();
      var parent = this.closest('.ff-nav-dropdown');
      parent.classList.toggle('open');
    });
  });

  // Close dropdown on outside click
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.ff-nav-dropdown')) {
      document.querySelectorAll('.ff-nav-dropdown.open').forEach(function (dd) {
        dd.classList.remove('open');
      });
    }
  });

  /* --- Header Scroll Behavior --- */
  var header = document.getElementById('header');
  var lastScroll = 0;

  if (header) {
    window.addEventListener('scroll', function () {
      var scrollY = window.pageYOffset;

      if (scrollY > 60) {
        header.classList.add('ff-header--scrolled');
      } else {
        header.classList.remove('ff-header--scrolled');
      }

      lastScroll = scrollY;
    }, { passive: true });
  }

  /* --- Scroll Reveal Animations --- */
  var reveals = document.querySelectorAll('.ff-reveal');

  if (reveals.length > 0 && 'IntersectionObserver' in window) {
    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('ff-revealed');
          revealObserver.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.12,
      rootMargin: '0px 0px -40px 0px'
    });

    reveals.forEach(function (el) {
      revealObserver.observe(el);
    });
  } else {
    // Fallback: show everything immediately
    reveals.forEach(function (el) {
      el.classList.add('ff-revealed');
    });
  }

  /* --- Smooth Scroll for Anchor Links --- */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var targetId = this.getAttribute('href');
      if (targetId === '#') return;

      var target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        var headerHeight = header ? header.offsetHeight : 0;
        var targetPos = target.getBoundingClientRect().top + window.pageYOffset - headerHeight - 20;

        window.scrollTo({
          top: targetPos,
          behavior: 'smooth'
        });
      }
    });
  });

  /* --- Counter Animation for Stats --- */
  var statNumbers = document.querySelectorAll('.ff-stat__number');

  if (statNumbers.length > 0 && 'IntersectionObserver' in window) {
    var counterObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          counterObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });

    statNumbers.forEach(function (el) {
      counterObserver.observe(el);
    });
  }

  function animateCounter(el) {
    var text = el.textContent.trim();
    var match = text.match(/^\$?(\d+)/);
    if (!match) return;

    var target = parseInt(match[1], 10);
    var prefix = text.startsWith('$') ? '$' : '';
    var suffix = text.replace(/^\$?\d+/, '');
    var duration = 1600;
    var start = performance.now();

    function step(now) {
      var progress = Math.min((now - start) / duration, 1);
      var eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
      var current = Math.floor(eased * target);
      el.textContent = prefix + current + suffix;

      if (progress < 1) {
        requestAnimationFrame(step);
      }
    }

    requestAnimationFrame(step);
  }

  /* --- Iframe Fallback Detection --- */
  document.querySelectorAll('.ff-iframe-card').forEach(function (card) {
    var iframe = card.querySelector('iframe');
    if (iframe) {
      // Many sites set X-Frame-Options DENY — show fallback after timeout
      var fallbackTimer = setTimeout(function () {
        card.classList.add('ff-iframe-card--fallback');
      }, 5000);

      iframe.addEventListener('load', function () {
        // If it loaded but is blank (blocked), show fallback
        try {
          // Cross-origin will throw — that's expected, means it loaded
          var doc = iframe.contentDocument;
          if (doc && doc.body && doc.body.innerHTML === '') {
            card.classList.add('ff-iframe-card--fallback');
          }
        } catch (e) {
          // Cross-origin = iframe loaded the site successfully
          clearTimeout(fallbackTimer);
        }
      });

      iframe.addEventListener('error', function () {
        card.classList.add('ff-iframe-card--fallback');
        clearTimeout(fallbackTimer);
      });
    }
  });

  /* --- Active Nav Highlighting on Scroll --- */
  var sections = document.querySelectorAll('section[id]');

  if (sections.length > 0) {
    window.addEventListener('scroll', function () {
      var scrollY = window.pageYOffset;
      var headerHeight = header ? header.offsetHeight : 80;

      sections.forEach(function (section) {
        var top = section.offsetTop - headerHeight - 100;
        var bottom = top + section.offsetHeight;
        var id = section.getAttribute('id');
        var link = mainNav ? mainNav.querySelector('a[href="#' + id + '"]') : null;

        if (link) {
          if (scrollY >= top && scrollY < bottom) {
            link.classList.add('ff-nav__active');
          } else {
            link.classList.remove('ff-nav__active');
          }
        }
      });
    }, { passive: true });
  }

})();
