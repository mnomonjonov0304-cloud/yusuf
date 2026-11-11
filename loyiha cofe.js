// Translations
const translations = {
    uz: {
        'nav-home': "Bosh sahifa",
        'nav-menu': "Menyu",
        'nav-about': "Biz haqimizda",
        'nav-contact': "Aloqa",
        'hero-badge': "1998-yildan beri",
        'hero-title-1': "An'anaviy uslubda",
        'hero-title-2': "qahva san'ati",
        'hero-subtitle': "Har bir finjonda o'tmishning nafisligi va hozirgi zamon mahorati birlashadi. Yuqori sifatli donlardan tayyorlangan klassik kofe",
        'hero-btn-menu': "Menyuni ko'rish",
        'hero-btn-contact': "Stol band qilish",
        'footer-text': "Har bir chashkada sifat va muhabbat",
        'footer-links-title': "Tezkor havolalar",
        'footer-hours-title': "Ish vaqti",
        'footer-hours-days': "Dushanba - Yakshanba"
    },
    ru: {
        'nav-home': "Главная",
        'nav-menu': "Меню",
        'nav-about': "О нас",
        'nav-contact': "Контакты",
        'hero-badge': "С 1998 года",
        'hero-title-1': "Традиционное искусство",
        'hero-title-2': "кофе",
        'hero-subtitle': "В каждой чашке сливаются изящество прошлого и мастерство настоящего. Классический кофе из отборных зерен",
        'hero-btn-menu': "Посмотреть меню",
        'hero-btn-contact': "Забронировать стол",
        'footer-text': "Качество и любовь в каждой чашке",
        'footer-links-title': "Быстрые ссылки",
        'footer-hours-title': "Режим работы",
        'footer-hours-days': "Понедельник - Воскресенье"
    },
    en: {
        'nav-home': "Home",
        'nav-menu': "Menu",
        'nav-about': "About Us",
        'nav-contact': "Contact",
        'hero-badge': "Since 1998",
        'hero-title-1': "Traditional Art of",
        'hero-title-2': "Coffee",
        'hero-subtitle': "Each cup blends the elegance of the past with the craftsmanship of today. Classic coffee made from premium beans",
        'hero-btn-menu': "View Menu",
        'hero-btn-contact': "Reserve Table",
        'footer-text': "Quality and love in every cup",
        'footer-links-title': "Quick Links",
        'footer-hours-title': "Opening Hours",
        'footer-hours-days': "Monday - Sunday"
    }
};

let currentLanguage = localStorage.getItem('language') || 'uz';

// Language Switcher
const langBtn = document.getElementById('langBtn');
const langMenu = document.getElementById('langMenu');
const langOptions = document.querySelectorAll('.lang-option');
const currentLangSpan = document.getElementById('currentLang');

if (langBtn) {
    langBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        langMenu.classList.toggle('active');
    });
}

document.addEventListener('click', () => {
    if (langMenu) {
        langMenu.classList.remove('active');
    }
});

if (langMenu) {
    langMenu.addEventListener('click', (e) => {
        e.stopPropagation();
    });
}

langOptions.forEach(option => {
    option.addEventListener('click', () => {
        const lang = option.getAttribute('data-lang');
        changeLanguage(lang);
        langMenu.classList.remove('active');
    });
});

function changeLanguage(lang) {
    currentLanguage = lang;
    localStorage.setItem('language', lang);
    
    // Update current lang display
    if (currentLangSpan) {
        currentLangSpan.textContent = lang.toUpperCase();
    }
    
    // Update active state
    langOptions.forEach(opt => {
        opt.classList.toggle('active', opt.getAttribute('data-lang') === lang);
    });
    
    // Translate elements
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (translations[lang] && translations[lang][key]) {
            element.textContent = translations[lang][key];
        }
    });
}

// Initialize language on page load
document.addEventListener('DOMContentLoaded', () => {
    changeLanguage(currentLanguage);
});

// Mobile Menu Toggle
const hamburger = document.getElementById('hamburger');
const navMenu = document.getElementById('navMenu');
const navLinks = document.querySelectorAll('.nav-link');

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
});

// Close menu when clicking on a link
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
    });
});

// Coffee Slider
const coffeeSlides = document.querySelectorAll('.coffee-slide');
const dots = document.querySelectorAll('.dot');
let currentSlide = 0;
const totalSlides = coffeeSlides.length;

function showSlide(n) {
    coffeeSlides.forEach(slide => slide.classList.remove('active'));
    dots.forEach(dot => dot.classList.remove('active'));
    
    currentSlide = (n + totalSlides) % totalSlides;
    
    coffeeSlides[currentSlide].classList.add('active');
    dots[currentSlide].classList.add('active');
}

function nextSlide() {
    showSlide(currentSlide + 1);
}

// Auto rotate slider every 3.5 seconds
if (coffeeSlides.length > 0) {
    setInterval(nextSlide, 3500);
}

// Dot click handlers
dots.forEach((dot, index) => {
    dot.addEventListener('click', () => {
        showSlide(index);
    });
});

// Add scroll effect to header
window.addEventListener('scroll', () => {
    const header = document.querySelector('.header');
    
    if (window.scrollY > 100) {
        header.style.background = 'rgba(26, 14, 10, 0.98)';
        header.style.boxShadow = '0 4px 30px rgba(0, 0, 0, 0.5)';
    } else {
        header.style.background = 'rgba(26, 14, 10, 0.97)';
        header.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.3)';
    }
});

// Smooth scroll offset for fixed header
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const headerHeight = document.querySelector('.header').offsetHeight;
            const targetPosition = target.getBoundingClientRect().top + window.pageYOffset;
            window.scrollTo({
                top: targetPosition - headerHeight,
                behavior: 'smooth'
            });
        }
    });
});