'use strict';
const btn = document.querySelector('[data-menu-toggle]');
const nav = document.querySelector('[data-menu]');
if (btn && nav) {
  const close=()=>{nav.classList.remove('is-open');btn.setAttribute('aria-expanded','false');btn.setAttribute('aria-label','Open menu')};
  btn.addEventListener('click',()=>{const isOpen=nav.classList.toggle('is-open');btn.setAttribute('aria-expanded',String(isOpen));btn.setAttribute('aria-label',isOpen?'Close menu':'Open menu')});
  nav.addEventListener('click',e=>{if(e.target.closest('a'))close()});
  document.addEventListener('keydown',e=>{if(e.key==='Escape')close()});
}
