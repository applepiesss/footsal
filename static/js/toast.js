function showToast(title, message, type = 'normal', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    
    if (!toastComponent) return;

    // Remove all type classes first
    toastComponent.classList.remove(
        'bg-white', 'border-[#75070C]', 'text-[#75070C]',
        'bg-white', 'border-[#4F6815]', 'text-[#4F6815]',
        'bg-white', 'border-gray-300', 'text-gray-800'
    );

    // Set type styles and icon
    if (type === 'success') {
        toastComponent.classList.add('bg-white', 'border-[#4F6815]', 'text-[#4F6815]');
        toastComponent.style.border = '1px solid #4F6815';
    } else if (type === 'error') {
        toastComponent.classList.add('bg-white', 'border-[#75070C]', 'text-[#75070C]');
        toastComponent.style.border = '1px solid #75070C';
    } else {
        toastComponent.classList.add('bg-white', 'border-gray-300', 'text-gray-800');
        toastComponent.style.border = '1px solid #d1d5db';
    } 

    toastTitle.textContent = title;
    toastMessage.textContent = message;

    toastComponent.classList.remove('opacity-0', 'translate-y-64');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-64');
    }, duration);
}