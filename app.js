// Paradise Bakes & Cafe Training App JavaScript

class ParadiseCafeApp {
    constructor() {
        this.currentSection = 'home';
        this.timerInterval = null;
        this.timerSeconds = 0;
        
        this.init();
    }

    init() {
        // Wait for DOM to be fully loaded
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => {
                this.setupApp();
            });
        } else {
            this.setupApp();
        }
    }

    setupApp() {
        this.setupNavigation();
        this.setupFilters();
        this.setupSearch();
        this.setupTimer();
        this.setupTools();
        this.setupModals();
        this.setupChecklists();
        this.loadSavedData();
        
        console.log('Paradise Cafe App initialized successfully');
    }

    setupNavigation() {
        const navButtons = document.querySelectorAll('.nav-btn[data-section]');
        const sections = document.querySelectorAll('.content-section');

        console.log('Setting up navigation. Found nav buttons:', navButtons.length);
        console.log('Found sections:', sections.length);

        navButtons.forEach((btn, index) => {
            console.log(`Setting up button ${index}:`, btn.dataset.section);
            
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                const targetSection = btn.dataset.section;
                console.log('Navigation clicked:', targetSection);
                
                // Update active nav button
                navButtons.forEach(navBtn => navBtn.classList.remove('active'));
                btn.classList.add('active');
                
                // Hide all sections
                sections.forEach(section => {
                    section.classList.remove('active');
                    section.style.display = 'none';
                });
                
                // Show target section
                const targetElement = document.getElementById(targetSection);
                console.log('Target element found:', targetElement);
                
                if (targetElement) {
                    targetElement.classList.add('active');
                    targetElement.style.display = 'block';
                    this.currentSection = targetSection;
                    
                    // Save current section
                    try {
                        localStorage.setItem('currentSection', targetSection);
                    } catch (e) {
                        console.warn('Could not save to localStorage:', e);
                    }
                } else {
                    console.error('Target section not found:', targetSection);
                }
            });
        });

        // Set initial state - make sure home is visible
        const homeSection = document.getElementById('home');
        if (homeSection) {
            homeSection.style.display = 'block';
            homeSection.classList.add('active');
        }
    }

    setupFilters() {
        const filterButtons = document.querySelectorAll('.filter-btn');
        const recipeCards = document.querySelectorAll('.recipe-card');

        console.log('Setting up filters. Found filter buttons:', filterButtons.length);

        filterButtons.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                
                // Update active filter button
                filterButtons.forEach(filterBtn => filterBtn.classList.remove('active'));
                btn.classList.add('active');
                
                const filterValue = btn.dataset.filter;
                console.log('Filter clicked:', filterValue);
                
                // Filter recipe cards
                recipeCards.forEach(card => {
                    if (filterValue === 'all') {
                        card.style.display = 'block';
                    } else {
                        const category = card.dataset.category;
                        if (category === filterValue) {
                            card.style.display = 'block';
                        } else {
                            card.style.display = 'none';
                        }
                    }
                });
            });
        });
    }

    setupSearch() {
        const searchBtn = document.getElementById('search-btn');
        const searchModal = document.getElementById('search-modal');
        const searchInput = document.getElementById('search-input');
        const searchResults = document.getElementById('search-results');

        console.log('Setting up search. Found elements:', {
            searchBtn: !!searchBtn,
            searchModal: !!searchModal,
            searchInput: !!searchInput,
            searchResults: !!searchResults
        });

        // Search data
        this.searchData = [
            { name: 'Margherita Pizza', category: 'pizza', type: 'Classic' },
            { name: 'Peppy Paneer Pizza', category: 'pizza', type: 'Spicy' },
            { name: 'Tandoori Veggie Supreme', category: 'pizza', type: 'Fusion' },
            { name: 'Farmhouse Pizza', category: 'pizza', type: 'Classic' },
            { name: 'Corn & Cheese Pizza', category: 'pizza', type: 'Classic' },
            { name: 'Mexican Green Wave', category: 'pizza', type: 'Spicy' },
            { name: 'Classic Aloo Tikki Burger', category: 'burger', type: 'Street Style' },
            { name: 'Paneer Masala Burger', category: 'burger', type: 'Cheesy' },
            { name: 'BBQ Soya Chunk Burger', category: 'burger', type: 'Protein Rich' },
            { name: 'Peri-Peri Veggie Burger', category: 'burger', type: 'Spicy' },
            { name: 'Bombay Grill Sandwich', category: 'sandwich', type: 'Street Style' },
            { name: 'Schezwan Veg Sandwich', category: 'sandwich', type: 'Spicy' },
            { name: 'Paneer Tikka Sandwich', category: 'sandwich', type: 'Fusion' },
            { name: 'Chilli Cheese Toast', category: 'sandwich', type: 'Cheesy' },
            { name: 'Commercial Pizza Oven', category: 'equipment', type: 'Equipment' },
            { name: 'Sandwich Maker', category: 'equipment', type: 'Equipment' },
            { name: 'Deep Fryer', category: 'equipment', type: 'Equipment' },
            { name: 'Hand Washing', category: 'safety', type: 'Food Safety' },
            { name: 'Temperature Control', category: 'safety', type: 'Food Safety' }
        ];

        if (searchBtn && searchModal) {
            searchBtn.addEventListener('click', (e) => {
                e.preventDefault();
                console.log('Search button clicked');
                searchModal.classList.remove('hidden');
                if (searchInput) {
                    searchInput.focus();
                }
            });
        }

        if (searchInput && searchResults) {
            searchInput.addEventListener('input', (e) => {
                const query = e.target.value.toLowerCase();
                this.performSearch(query, searchResults);
            });
        }
    }

    performSearch(query, resultsContainer) {
        if (!resultsContainer) return;
        
        resultsContainer.innerHTML = '';
        
        if (query.length < 2) return;
        
        const results = this.searchData.filter(item => 
            item.name.toLowerCase().includes(query) ||
            item.category.toLowerCase().includes(query) ||
            item.type.toLowerCase().includes(query)
        );
        
        results.forEach(result => {
            const resultItem = document.createElement('div');
            resultItem.className = 'search-result-item';
            resultItem.innerHTML = `
                <strong>${result.name}</strong>
                <br>
                <small>${result.type} • ${result.category}</small>
            `;
            
            resultItem.addEventListener('click', () => {
                this.navigateToResult(result);
                const searchModal = document.getElementById('search-modal');
                if (searchModal) {
                    searchModal.classList.add('hidden');
                }
            });
            
            resultsContainer.appendChild(resultItem);
        });
        
        if (results.length === 0) {
            resultsContainer.innerHTML = '<div class="search-result-item">No results found</div>';
        }
    }

    navigateToResult(result) {
        // Navigate to the appropriate section
        const navButton = document.querySelector(`[data-section="${result.category}"]`);
        if (navButton) {
            navButton.click();
        }
    }

    setupTimer() {
        const timerBtn = document.getElementById('timer-btn');
        const timerPopup = document.getElementById('timer-popup');
        const timerMinutes = document.getElementById('timer-minutes');
        const startTimerBtn = document.getElementById('start-timer');
        const timerDisplay = document.getElementById('timer-display');

        console.log('Setting up timer. Found elements:', {
            timerBtn: !!timerBtn,
            timerPopup: !!timerPopup,
            timerMinutes: !!timerMinutes,
            startTimerBtn: !!startTimerBtn,
            timerDisplay: !!timerDisplay
        });

        if (timerBtn && timerPopup) {
            timerBtn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                console.log('Timer button clicked');
                timerPopup.classList.toggle('hidden');
            });
        }

        if (startTimerBtn && timerMinutes && timerDisplay) {
            startTimerBtn.addEventListener('click', (e) => {
                e.preventDefault();
                const minutes = parseInt(timerMinutes.value) || 0;
                console.log('Starting timer for minutes:', minutes);
                if (minutes > 0) {
                    this.startTimer(minutes * 60, timerDisplay);
                    if (timerPopup) {
                        timerPopup.classList.add('hidden');
                    }
                }
            });
        }

        // Close timer popup when clicking outside
        document.addEventListener('click', (e) => {
            if (timerBtn && timerPopup && 
                !timerBtn.contains(e.target) && 
                !timerPopup.contains(e.target)) {
                timerPopup.classList.add('hidden');
            }
        });
    }

    startTimer(seconds, display) {
        if (this.timerInterval) {
            clearInterval(this.timerInterval);
        }
        
        this.timerSeconds = seconds;
        console.log('Timer started for', seconds, 'seconds');
        
        this.timerInterval = setInterval(() => {
            this.timerSeconds--;
            
            const minutes = Math.floor(this.timerSeconds / 60);
            const secs = this.timerSeconds % 60;
            
            display.textContent = `${minutes.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
            
            if (this.timerSeconds <= 0) {
                clearInterval(this.timerInterval);
                this.timerInterval = null;
                display.textContent = 'Time Up!';
                display.style.color = 'var(--color-error)';
                
                // Play notification sound (visual feedback)
                this.showTimerNotification();
                
                setTimeout(() => {
                    display.textContent = '00:00';
                    display.style.color = 'var(--color-primary)';
                }, 3000);
            }
        }, 1000);
    }

    showTimerNotification() {
        // Create a visual notification
        const notification = document.createElement('div');
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: var(--color-error);
            color: white;
            padding: 16px 24px;
            border-radius: 8px;
            z-index: 2000;
            box-shadow: var(--shadow-lg);
            font-weight: bold;
        `;
        notification.textContent = '⏰ Timer Complete!';
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            if (notification.parentNode) {
                notification.remove();
            }
        }, 5000);
    }

    setupTools() {
        const printBtn = document.getElementById('print-btn');
        
        if (printBtn) {
            printBtn.addEventListener('click', (e) => {
                e.preventDefault();
                window.print();
            });
        }
    }

    setupModals() {
        const modals = document.querySelectorAll('.modal');
        const closeButtons = document.querySelectorAll('.close');
        
        console.log('Setting up modals. Found:', modals.length, 'modals');
        
        // Close modal when clicking close button
        closeButtons.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                const modal = btn.closest('.modal');
                if (modal) {
                    modal.classList.add('hidden');
                }
            });
        });
        
        // Close modal when clicking outside
        modals.forEach(modal => {
            modal.addEventListener('click', (e) => {
                if (e.target === modal) {
                    modal.classList.add('hidden');
                }
            });
        });
        
        // Close modal with Escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                modals.forEach(modal => {
                    modal.classList.add('hidden');
                });
            }
        });
    }

    setupChecklists() {
        const checkboxes = document.querySelectorAll('input[type="checkbox"]');
        
        console.log('Setting up checklists. Found checkboxes:', checkboxes.length);
        
        checkboxes.forEach((checkbox, index) => {
            // Generate a simple ID for the checkbox
            const checkboxId = `checkbox_${index}_${Date.now()}`;
            
            // Load saved state
            try {
                const savedState = localStorage.getItem(checkboxId);
                if (savedState === 'true') {
                    checkbox.checked = true;
                }
            } catch (e) {
                console.warn('Could not load checkbox state:', e);
            }
            
            // Save state on change
            checkbox.addEventListener('change', () => {
                try {
                    localStorage.setItem(checkboxId, checkbox.checked.toString());
                } catch (e) {
                    console.warn('Could not save checkbox state:', e);
                }
                
                // Add visual feedback
                const label = checkbox.closest('label');
                if (label) {
                    if (checkbox.checked) {
                        label.style.textDecoration = 'line-through';
                        label.style.opacity = '0.7';
                    } else {
                        label.style.textDecoration = 'none';
                        label.style.opacity = '1';
                    }
                }
            });
            
            // Apply initial styling
            if (checkbox.checked) {
                const label = checkbox.closest('label');
                if (label) {
                    label.style.textDecoration = 'line-through';
                    label.style.opacity = '0.7';
                }
            }
        });
    }

    loadSavedData() {
        // Load any saved application state
        try {
            const savedSection = localStorage.getItem('currentSection');
            if (savedSection && savedSection !== 'home') {
                const navButton = document.querySelector(`[data-section="${savedSection}"]`);
                if (navButton) {
                    // Delay to ensure all elements are ready
                    setTimeout(() => {
                        navButton.click();
                    }, 100);
                }
            }
        } catch (e) {
            console.warn('Could not load saved data:', e);
        }
    }

    // Utility method to add more recipes dynamically
    addRecipe(category, recipe) {
        const recipesGrid = document.querySelector(`#${category} .recipes-grid`);
        if (!recipesGrid) return;
        
        const recipeCard = document.createElement('div');
        recipeCard.className = 'recipe-card';
        if (recipe.type) {
            recipeCard.dataset.category = recipe.type.toLowerCase();
        }
        
        recipeCard.innerHTML = `
            ${recipe.image ? `<img src="${recipe.image}" alt="${recipe.name}">` : ''}
            <h3>${recipe.name}</h3>
            <div class="recipe-info">
                <span class="recipe-type">${recipe.type || 'Recipe'}</span>
                ${recipe.sizes ? `<span class="recipe-sizes">${recipe.sizes}</span>` : ''}
            </div>
            ${recipe.ingredients && recipe.steps ? `
                <div class="recipe-details">
                    <h4>Ingredients:</h4>
                    <ul>
                        ${recipe.ingredients.map(ingredient => `<li>${ingredient}</li>`).join('')}
                    </ul>
                    <h4>Method (Hinglish):</h4>
                    <ol>
                        ${recipe.steps.map(step => `<li>${step}</li>`).join('')}
                    </ol>
                </div>
            ` : ''}
        `;
        
        recipesGrid.appendChild(recipeCard);
    }

    // Method to export checklist progress
    exportProgress() {
        const checkboxes = document.querySelectorAll('input[type="checkbox"]');
        const progress = {};
        
        checkboxes.forEach((checkbox, index) => {
            const checkboxId = `checkbox_${index}`;
            progress[checkboxId] = checkbox.checked;
        });
        
        const blob = new Blob([JSON.stringify(progress, null, 2)], {
            type: 'application/json'
        });
        
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'paradise_cafe_progress.json';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        
        URL.revokeObjectURL(url);
    }

    // Method to clear all progress
    clearProgress() {
        if (confirm('Are you sure you want to clear all checklist progress? यह सारी progress delete हो जाएगी।')) {
            const checkboxes = document.querySelectorAll('input[type="checkbox"]');
            checkboxes.forEach((checkbox, index) => {
                checkbox.checked = false;
                const checkboxId = `checkbox_${index}`;
                try {
                    localStorage.removeItem(checkboxId);
                } catch (e) {
                    console.warn('Could not clear checkbox state:', e);
                }
                
                const label = checkbox.closest('label');
                if (label) {
                    label.style.textDecoration = 'none';
                    label.style.opacity = '1';
                }
            });
        }
    }
}

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM loaded, initializing Paradise Cafe App...');
    window.paradiseCafeApp = new ParadiseCafeApp();
    
    // Add some helpful global functions
    window.exportProgress = () => {
        if (window.paradiseCafeApp) {
            window.paradiseCafeApp.exportProgress();
        }
    };
    
    window.clearProgress = () => {
        if (window.paradiseCafeApp) {
            window.paradiseCafeApp.clearProgress();
        }
    };
    
    // Add keyboard shortcuts
    document.addEventListener('keydown', (e) => {
        // Ctrl/Cmd + F for search
        if ((e.ctrlKey || e.metaKey) && e.key === 'f') {
            e.preventDefault();
            const searchBtn = document.getElementById('search-btn');
            if (searchBtn) {
                searchBtn.click();
            }
        }
        
        // Ctrl/Cmd + P for print
        if ((e.ctrlKey || e.metaKey) && e.key === 'p') {
            e.preventDefault();
            window.print();
        }
        
        // Ctrl/Cmd + T for timer
        if ((e.ctrlKey || e.metaKey) && e.key === 't') {
            e.preventDefault();
            const timerBtn = document.getElementById('timer-btn');
            if (timerBtn) {
                timerBtn.click();
            }
        }
    });
    
    console.log('🌴 Paradise Bakes & Cafe Training App Loaded Successfully!');
    console.log('Available shortcuts:');
    console.log('- Ctrl/Cmd + F: Search');
    console.log('- Ctrl/Cmd + P: Print'); 
    console.log('- Ctrl/Cmd + T: Timer');
    console.log('- exportProgress(): Export checklist progress');
    console.log('- clearProgress(): Clear all progress');
});