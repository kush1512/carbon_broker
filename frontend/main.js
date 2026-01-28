// This script is for the register.html page.
document.addEventListener('DOMContentLoaded', function() {
    const ngoTabBtn = document.getElementById('ngo-tab-btn');
    const businessTabBtn = document.getElementById('business-tab-btn');
    const ngoRegisterForm = document.getElementById('ngo-register-form');
    const businessRegisterForm = document.getElementById('business-register-form');

    // Default to NGO tab on page load
    ngoTabBtn.classList.add('tab-btn-active');
    ngoRegisterForm.classList.add('active');

    ngoTabBtn.addEventListener('click', () => {
        ngoTabBtn.classList.add('tab-btn-active');
        businessTabBtn.classList.remove('tab-btn-active');
        ngoRegisterForm.classList.add('active');
        businessRegisterForm.classList.remove('active');
    });
    
    businessTabBtn.addEventListener('click', () => {
        businessTabBtn.classList.add('tab-btn-active');
        ngoTabBtn.classList.remove('tab-btn-active');
        businessRegisterForm.classList.add('active');
        ngoRegisterForm.classList.remove('active');
    });
});
