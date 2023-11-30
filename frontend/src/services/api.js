export async function customFetch(url, method = 'GET', data = null) {
  try {
      const options = {
          method,
          headers: {
              'Content-Type': 'application/json',
          },
      };

      if (data) {
          options.body = JSON.stringify(data);
      }

      const response = await fetch(`http://localhost:8000${url}`, options);

      if (!response.ok) {
          throw new Error(`Network response was not ok: ${response.statusText}`);
      }

      return response.json();
  } catch (error) {
      console.error('Fetch error:', error);
      throw error;
  }
}

export function fetchData() {
  return customFetch('/');
}
export function postData(data) {
  return customFetch('/', 'POST', data);
}
export function viewPrivate() {
  return customFetch('/private');
}
export function loginRedirect() {
  return customFetch('/login');
}
export function logoutRedirect() {
  return customFetch('/logout');
}

