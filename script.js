document.addEventListener('DOMContentLoaded', () => {
    // State
    const cart = [];
    const cartSidebar = document.querySelector('.cart-sidebar');
    const cartItemsContainer = document.querySelector('.cart-items');
    const totalElement = document.getElementById('cart-total');
    const cartCountElement = document.querySelector('.cart-count');
    
    // Toggle Cart
    window.toggleCart = () => {
        cartSidebar.classList.toggle('open');
    };

    // Add to Cart Logic
    window.addToCart = (item, price) => {
        cart.push({ item, price });
        updateCart();
        toggleCart(); // Open cart to show item added
    };

    // Update Cart UI
    function updateCart() {
        cartItemsContainer.innerHTML = '';
        let total = 0;

        cart.forEach((product, index) => {
            total += product.price;
            const itemEl = document.createElement('div');
            itemEl.classList.add('cart-item');
            itemEl.innerHTML = `
                <div>${product.item}</div>
                <div>$${product.price.toFixed(2)}</div>
            `;
            cartItemsContainer.appendChild(itemEl);
        });

        totalElement.textContent = `$${total.toFixed(2)}`;
        cartCountElement.textContent = cart.length;
    }

    // Scroll Arrows Logic
    document.querySelectorAll('.scroll-arrow').forEach(arrow => {
        arrow.addEventListener('click', function(e) {
            e.stopPropagation(); // Prevent card clicks
            const carousel = this.closest('.menu-carousel');
            if (carousel) {
                carousel.scrollBy({ left: 300, behavior: 'smooth' });
            }
        });
    });
});
