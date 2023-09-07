
  // get function
  export async function fetchData() {
    try {
      const response = await fetch('http://localhost:8000');
      if (!response.ok) {
        throw new Error('Network response was not ok ' + response.statusText);
      }
      const data = await response.json();
      return data.message;
    } catch (error) {
      console.error('Fetch error:', error);
      throw error;
    }
  }
  
  // post function
  export async function postData(data) {
    try {
      const response = await fetch('http://localhost:8000', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });
      if (!response.ok) {
        throw new Error('Network response was not ok ' + response.statusText);
      }
      const responseData = await response.json();
      return responseData;
    } catch (error) {
      console.error('Fetch error:', error);
      throw error;
    }
  }