function showToast(title, message = '') {
  const toast = document.getElementById('toast-component');
  const toastTitle = document.getElementById('toast-title');
  const toastMessage = document.getElementById('toast-message');
  const toastIcon = document.getElementById('toast-icon');
  
  if (!toast) return;
  
  // Set content
  if (toastTitle) toastTitle.textContent = title;
  if (toastMessage) toastMessage.textContent = message;
  if (toastIcon) toastIcon.textContent = '✅';
  
  // Set color based on title
  toast.className = 'fixed bottom-8 right-8 p-4 px-8 rounded-xl shadow-xl z-50 transition-all duration-300 flex items-center gap-4';
  
  if (title.toLowerCase().includes('error') || title.toLowerCase().includes('gagal')) {
    toast.classList.add('bg-red-100', 'border-2', 'border-red-500');
    if (toastIcon) toastIcon.textContent = '❌';
  } else if (title.toLowerCase().includes('success') || title.toLowerCase().includes('berhasil')) {
    toast.classList.add('bg-green-100', 'border-2', 'border-green-500');
    if (toastIcon) toastIcon.textContent = '✅';
  } else {
    toast.classList.add('bg-blue-100', 'border-2', 'border-blue-500');
    if (toastIcon) toastIcon.textContent = 'ℹ️';
  }
  
  // Show toast
  toast.style.opacity = '1';
  toast.style.transform = 'translateY(0)';
  
  // Hide after 3 seconds
  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(16rem)';
  }, 3000);
}