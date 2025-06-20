export function getCSRFToken() {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let cookie of cookies) {
        const trimmed = cookie.trim();
        if (trimmed.startsWith('csrftoken=')) {
          cookieValue = decodeURIComponent(trimmed.substring('csrftoken='.length));
          break;
        }
      }
    }
    return cookieValue;
  }