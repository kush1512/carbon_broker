document.addEventListener('DOMContentLoaded', function() {
    const ngoTabBtn = document.getElementById('ngo-tab-btn');
    const businessTabBtn = document.getElementById('business-tab-btn');
    const ngoForm = document.getElementById('ngo-register-form');
    const businessForm = document.getElementById('business-register-form');

    // Default NGO tab active
    ngoTabBtn.classList.add('tab-btn-active');
    ngoForm.classList.add('active');

    // Tab switching
    ngoTabBtn.addEventListener('click', () => {
        ngoTabBtn.classList.add('tab-btn-active');
        businessTabBtn.classList.remove('tab-btn-active');
        ngoForm.classList.add('active');
        businessForm.classList.remove('active');
    });

    businessTabBtn.addEventListener('click', () => {
        businessTabBtn.classList.add('tab-btn-active');
        ngoTabBtn.classList.remove('tab-btn-active');
        businessForm.classList.add('active');
        ngoForm.classList.remove('active');
    });

    // Next button redirects to KYC page
    document.getElementById('ngo-next-btn').addEventListener('click', () => {
        localStorage.setItem('registrationType', 'ngo');
        window.location.href = 'register-kyc.html';
    });

    document.getElementById('business-next-btn').addEventListener('click', () => {
        localStorage.setItem('registrationType', 'business');
        window.location.href = 'register-kyc.html';
    });
});
