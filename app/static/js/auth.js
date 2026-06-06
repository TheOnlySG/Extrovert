const API_URL = window.location.origin;

function getToken() {
    return localStorage.getItem('access_token');
}

function saveToken(token) {
    localStorage.setItem('access_token', token);
}

function removeToken() {
    localStorage.removeItem('access_token');
}

function getAuthHeaders() {
    const token = getToken();
    const headers = {
        'Content-Type': 'application/json'
    };
    if (token) {
        headers['Authorization'] = `Bearer ${token}`;
    }
    return headers;
}

function isLoggedIn() {
    return !!getToken();
}

function logout() {
    removeToken();
    window.location.href = 'login.html';
}

function checkAuthOrRedirect() {
    if (!isLoggedIn()) {
        window.location.href = 'login.html';
    }
}

function checkGuestOrRedirect() {
    if (isLoggedIn()) {
        window.location.href = 'feed.html';
    }
}

function formatDate(dateString) {
    if (!dateString) return '';
    const date = new Date(dateString);
    return date.toLocaleString([], { hour: '2-digit', minute: '2-digit', month: 'short', day: 'numeric' });
}
