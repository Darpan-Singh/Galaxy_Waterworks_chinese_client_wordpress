document.addEventListener('DOMContentLoaded', function () {

    // ── Sticky header shadow
    const header = document.getElementById('site-header');
    if (header) {
        window.addEventListener('scroll', () => {
            header.classList.toggle('scrolled', window.scrollY > 40);
        }, { passive: true });
    }

    // ── Mobile nav toggle
    const toggle = document.querySelector('.mobile-menu-toggle');
    const nav    = document.querySelector('.primary-nav');
    if (toggle && nav) {
        toggle.addEventListener('click', function () {
            const open = nav.classList.toggle('open');
            this.setAttribute('aria-expanded', String(open));
            const spans = this.querySelectorAll('span');
            if (open) {
                spans[0].style.cssText = 'transform:rotate(45deg) translate(5px,5px)';
                spans[1].style.cssText = 'opacity:0; transform:scaleX(0)';
                spans[2].style.cssText = 'transform:rotate(-45deg) translate(5px,-5px)';
            } else {
                spans.forEach(s => s.style.cssText = '');
            }
        });
        nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
            nav.classList.remove('open');
            toggle.setAttribute('aria-expanded', 'false');
            toggle.querySelectorAll('span').forEach(s => s.style.cssText = '');
        }));
    }

    // ── FAQ accordion
    document.querySelectorAll('.faq-q').forEach(btn => {
        btn.addEventListener('click', function () {
            const isOpen = this.getAttribute('aria-expanded') === 'true';
            // close all
            document.querySelectorAll('.faq-q').forEach(b => {
                b.setAttribute('aria-expanded', 'false');
                b.nextElementSibling.classList.remove('open');
            });
            // open clicked (unless already open)
            if (!isOpen) {
                this.setAttribute('aria-expanded', 'true');
                this.nextElementSibling.classList.add('open');
            }
        });
    });

    // ── Cases carousel
    const carousel = document.getElementById('casesCarousel');
    const prevBtn  = document.getElementById('carouselPrev');
    const nextBtn  = document.getElementById('carouselNext');
    if (carousel && prevBtn && nextBtn) {
        const scrollBy = () => carousel.querySelector('.case-card')?.offsetWidth + 16 || 300;
        prevBtn.addEventListener('click', () => carousel.scrollBy({ left: -scrollBy(), behavior: 'smooth' }));
        nextBtn.addEventListener('click', () => carousel.scrollBy({ left:  scrollBy(), behavior: 'smooth' }));
    }

    // ── Scroll reveal
    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver(entries => {
            entries.forEach(e => {
                if (e.isIntersecting) {
                    e.target.classList.add('visible');
                    observer.unobserve(e.target);
                }
            });
        }, { threshold: 0.1 });
        document.querySelectorAll('[data-reveal]').forEach(el => observer.observe(el));
    } else {
        document.querySelectorAll('[data-reveal]').forEach(el => el.classList.add('visible'));
    }

    // ── Stat counter animation
    if ('IntersectionObserver' in window) {
        const counterObs = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (!entry.isIntersecting) return;
                const el  = entry.target;
                const sup = el.querySelector('sup');
                const supText = sup ? sup.textContent : '';
                const raw = parseInt(el.textContent.replace(/\D/g, ''), 10);
                if (!raw) return;

                let current = 0;
                const step  = Math.ceil(raw / 60);
                const timer = setInterval(() => {
                    current = Math.min(current + step, raw);
                    el.textContent = current.toLocaleString();
                    if (supText) {
                        const s = document.createElement('sup');
                        s.textContent = supText;
                        el.appendChild(s);
                    }
                    if (current >= raw) clearInterval(timer);
                }, 22);
                counterObs.unobserve(el);
            });
        }, { threshold: 0.6 });

        document.querySelectorAll('.stat-num').forEach(el => counterObs.observe(el));
    }

});
