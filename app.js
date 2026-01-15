// app.js (Updated)

// --- Configuration ---
// Set this to your Flask server address
const API_BASE_URL = 'http://127.0.0.1:5000/api'; 

// --- Real API Calls (Replacing Simulation) ---

async function getCategories() {
    try {
        const response = await fetch(`${API_BASE_URL}/categories`);
        if (!response.ok) throw new Error('Failed to fetch categories');
        // The API returns a list of objects: [{"id": 1, "name": "Food"}, ...]
        const data = await response.json(); 
        // We convert it back to the expected list of tuples format for simplicity
        return data.map(cat => [cat.id, cat.name]); 
    } catch (error) {
        console.error('Error fetching categories:', error);
        return [];
    }
}

// Example of the POST request handler (e.g., for Add Category)
document.getElementById('addCategoryForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const name = document.getElementById('categoryName').value.trim();
    const messageElement = document.getElementById('addCategoryMessage');
    messageElement.textContent = 'Adding...';

    try {
        const response = await fetch(`${API_BASE_URL}/add_category`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name: name })
        });

        const result = await response.json();

        if (response.ok) {
            messageElement.style.color = 'green';
            messageElement.textContent = result.message;
            e.target.reset();
        } else {
            messageElement.style.color = 'red';
            messageElement.textContent = `Error: ${result.message}`;
        }
    } catch (error) {
        messageElement.style.color = 'red';
        messageElement.textContent = 'Network error. Check server status.';
        console.error('Fetch error:', error);
    }
});

// The other functions (getExpenses, getSummary, addExpenseForm, deleteCategoryForm)
// should be updated similarly to use the 'fetch' API instead of simulation.