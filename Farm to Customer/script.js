console.log("FreshFarm Direct script loaded.");

document.addEventListener('DOMContentLoaded', () => {
    const addToCartButtons = document.querySelectorAll('.product-info button');

    addToCartButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            // Find the parent product card
            const productCard = event.target.closest('.product-card');
            if (productCard) {
                // Find the product name (h3) within the card
                const productNameElement = productCard.querySelector('.product-info h3');
                const productName = productNameElement ? productNameElement.textContent : 'Unknown Product';

                console.log(`Added "${productName}" to cart.`);
                // In a real application, you would add logic here
                // to update a cart state, make an API call, etc.

                // Optional: Provide visual feedback
                event.target.textContent = 'Added!';
                event.target.disabled = true; // Prevent multiple clicks
                setTimeout(() => {
                    event.target.textContent = 'Add to Cart';
                    event.target.disabled = false;
                }, 1500); // Reset after 1.5 seconds
            }
        });
    });
});
