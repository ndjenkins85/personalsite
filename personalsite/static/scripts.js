// Modern vanilla JavaScript - no jQuery needed

// Toggle visibility of element
function togglehide(elemId) {
  const elem = document.getElementById(elemId);
  if (!elem) return;
  
  elem.style.display = elem.style.display === 'none' ? 'block' : 'none';
}

// Smooth scroll to anchor (for Projects link)
document.addEventListener('DOMContentLoaded', () => {
  const links = document.querySelectorAll('a[href^="#"]');
  
  links.forEach(link => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');
      if (href === '#') return;
      
      e.preventDefault();
      const target = document.querySelector(href);
      
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
});

// Gallery: Simple image lazy loading hint
if ('loading' in HTMLImageElement.prototype) {
  const images = document.querySelectorAll('img.lazy');
  images.forEach(img => {
    img.src = img.dataset.src;
  });
}
