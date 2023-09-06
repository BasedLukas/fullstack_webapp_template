export async function fetchData() {
    const response = await fetch('https://google.com', {mode: 'no-cors'});
    return response;
  }
  
