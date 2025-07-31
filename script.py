# I'll create the complete Paradise Bakes & Cafe training application with all required files
# Let me start by creating the comprehensive HTML structure

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paradise Bakes & Cafe - Professional Training Manual</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="manifest" href="manifest.json">
    <meta name="description" content="Paradise Bakes & Cafe Professional Training Manual - PCMC, Pune">
    <meta name="theme-color" content="#e74c3c">
    <link rel="icon" type="image/png" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA1klEQVRYhe2XMQ6CMBiFX4wJiYkjcQFGZmYnJ3dsJydmdmdmcoAJJ9DJ0cnBgQF7gKYplPDw">
</head>
<body>
    <!-- Loading Screen -->
    <div id="loading-screen" class="loading-screen">
        <div class="loading-content">
            <div class="logo-large">🌴 Paradise Bakes & Cafe</div>
            <div class="loading-spinner"></div>
            <p>Loading Training Manual...</p>
        </div>
    </div>

    <!-- Emergency Banner -->
    <div id="emergency-banner" class="emergency-banner">
        🚨 EMERGENCY: Call 108 (Medical) | 101 (Fire) | 100 (Police) 🚨
        <button class="close-emergency" onclick="closeEmergencyBanner()">×</button>
    </div>

    <!-- Header -->
    <header class="header">
        <div class="container">
            <div class="header-content">
                <div class="logo-section">
                    <h1 class="logo">🌴 Paradise Bakes & Cafe</h1>
                    <p class="tagline">Professional Training Manual</p>
                    <p class="location">📍 PCMC, Pune | Vegetarian Fast Food Excellence</p>
                </div>
                <div class="header-controls">
                    <button id="theme-toggle" class="theme-toggle" title="Toggle Dark Mode">🌙</button>
                    <button id="emergency-btn" class="emergency-btn" title="Emergency Procedures">🚨</button>
                </div>
            </div>
        </div>
    </header>

    <!-- Main Navigation -->
    <nav class="main-nav">
        <div class="container">
            <div class="nav-grid">
                <button class="nav-btn active" data-section="home">
                    <span class="nav-icon">🏠</span>
                    <span class="nav-text">Dashboard</span>
                </button>
                <button class="nav-btn" data-section="recipes">
                    <span class="nav-icon">📖</span>
                    <span class="nav-text">Recipe Collection</span>
                </button>
                <button class="nav-btn" data-section="equipment">
                    <span class="nav-icon">🔧</span>
                    <span class="nav-text">Equipment Guide</span>
                </button>
                <button class="nav-btn" data-section="safety">
                    <span class="nav-icon">🛡️</span>
                    <span class="nav-text">Food Safety</span>
                </button>
                <button class="nav-btn" data-section="bulk">
                    <span class="nav-icon">📊</span>
                    <span class="nav-text">Bulk Prep</span>
                </button>
                <button class="nav-btn" data-section="maintenance">
                    <span class="nav-icon">📋</span>
                    <span class="nav-text">Maintenance</span>
                </button>
                <button class="nav-btn" data-section="emergency">
                    <span class="nav-icon">🚨</span>
                    <span class="nav-text">Emergency</span>
                </button>
            </div>
        </div>
    </nav>

    <!-- Floating Utility Panel -->
    <div class="utility-panel">
        <button class="utility-btn" id="timer-btn" title="Kitchen Timers">
            <span class="icon">⏰</span>
        </button>
        <button class="utility-btn" id="search-btn" title="Search Recipes">
            <span class="icon">🔍</span>
        </button>
        <button class="utility-btn" id="converter-btn" title="Unit Converter">
            <span class="icon">🔄</span>
        </button>
        <button class="utility-btn" id="calculator-btn" title="Cost Calculator">
            <span class="icon">💰</span>
        </button>
    </div>

    <!-- Main Content Container -->
    <main class="main-content">
        <div class="container">
            <!-- Home Dashboard Section -->
            <section id="home-section" class="section active">
                <div class="welcome-banner">
                    <h2>Welcome to Paradise Bakes & Cafe Training System</h2>
                    <p>Professional vegetarian fast food training for PCMC, Pune market</p>
                </div>
                
                <div class="dashboard-grid">
                    <div class="dashboard-card recipes-card" onclick="navigateToSection('recipes')">
                        <div class="card-icon">📖</div>
                        <h3>Recipe Collection</h3>
                        <p>36+ Vegetarian Recipes</p>
                        <div class="stats">
                            <span>🍕 12 Pizzas | 🍔 12 Burgers | 🥪 12 Sandwiches</span>
                        </div>
                    </div>
                    
                    <div class="dashboard-card equipment-card" onclick="navigateToSection('equipment')">
                        <div class="card-icon">🔧</div>
                        <h3>Equipment Guide</h3>
                        <p>9 Professional Equipment</p>
                        <div class="stats">
                            <span>Complete Operating & Maintenance Guides</span>
                        </div>
                    </div>
                    
                    <div class="dashboard-card safety-card" onclick="navigateToSection('safety')">
                        <div class="card-icon">🛡️</div>
                        <h3>Food Safety & Hygiene</h3>
                        <p>FSSAI Compliance</p>
                        <div class="stats">
                            <span>Personal Hygiene | Kitchen Sanitation</span>
                        </div>
                    </div>
                    
                    <div class="dashboard-card bulk-card" onclick="navigateToSection('bulk')">
                        <div class="card-icon">📊</div>
                        <h3>Bulk Preparation</h3>
                        <p>Professional Scaling</p>
                        <div class="stats">
                            <span>Cost Calculation | Time Estimation</span>
                        </div>
                    </div>
                    
                    <div class="dashboard-card maintenance-card" onclick="navigateToSection('maintenance')">
                        <div class="card-icon">📋</div>
                        <h3>Maintenance</h3>
                        <p>Equipment Care</p>
                        <div class="stats">
                            <span>Daily | Weekly | Monthly Schedules</span>
                        </div>
                    </div>
                    
                    <div class="dashboard-card emergency-card" onclick="navigateToSection('emergency')">
                        <div class="card-icon">🚨</div>
                        <h3>Emergency Procedures</h3>
                        <p>Safety Protocols</p>
                        <div class="stats">
                            <span>Fire | Electrical | Medical | Equipment</span>
                        </div>
                    </div>
                </div>

                <div class="quick-stats">
                    <div class="stat-item">
                        <div class="stat-number">36+</div>
                        <div class="stat-label">Recipes</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-number">9</div>
                        <div class="stat-label">Equipment</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-number">100%</div>
                        <div class="stat-label">FSSAI Compliant</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-number">24/7</div>
                        <div class="stat-label">Available</div>
                    </div>
                </div>
            </section>

            <!-- Recipe Collection Section -->
            <section id="recipes-section" class="section">
                <div class="section-header">
                    <h2>Recipe Collection</h2>
                    <p>Complete guide to all 36+ vegetarian fast food items popular in PCMC, Pune</p>
                </div>

                <div class="recipe-categories">
                    <div class="category-tabs">
                        <button class="tab-btn active" data-category="pizza">🍕 Pizza (12)</button>
                        <button class="tab-btn" data-category="burger">🍔 Burger (12)</button>
                        <button class="tab-btn" data-category="sandwich">🥪 Sandwich (12)</button>
                    </div>

                    <!-- Pizza Recipes -->
                    <div id="pizza-recipes" class="recipe-grid active">
                        <!-- Pizza recipes will be dynamically loaded here -->
                    </div>

                    <!-- Burger Recipes -->
                    <div id="burger-recipes" class="recipe-grid">
                        <!-- Burger recipes will be dynamically loaded here -->
                    </div>

                    <!-- Sandwich Recipes -->
                    <div id="sandwich-recipes" class="recipe-grid">
                        <!-- Sandwich recipes will be dynamically loaded here -->
                    </div>
                </div>
            </section>

            <!-- Equipment Guide Section -->
            <section id="equipment-section" class="section">
                <div class="section-header">
                    <h2>Equipment Guide</h2>
                    <p>Comprehensive guide for all 9 commercial kitchen equipment pieces</p>
                </div>
                
                <div class="equipment-grid" id="equipment-grid">
                    <!-- Equipment cards will be dynamically loaded here -->
                </div>
            </section>

            <!-- Food Safety & Hygiene Section -->
            <section id="safety-section" class="section">
                <div class="section-header">
                    <h2>Food Safety & Hygiene</h2>
                    <p>FSSAI compliant safety protocols and hygiene standards</p>
                </div>
                
                <div class="safety-categories">
                    <div class="safety-tabs">
                        <button class="tab-btn active" data-safety="personal">👤 Personal Hygiene</button>
                        <button class="tab-btn" data-safety="kitchen">🏠 Kitchen Sanitation</button>
                        <button class="tab-btn" data-safety="food">🍽️ Food Safety</button>
                        <button class="tab-btn" data-safety="haccp">📋 HACCP</button>
                    </div>

                    <div class="safety-content" id="safety-content">
                        <!-- Safety content will be dynamically loaded here -->
                    </div>
                </div>
            </section>

            <!-- Bulk Preparation Section -->
            <section id="bulk-section" class="section">
                <div class="section-header">
                    <h2>Bulk Preparation Guide</h2>
                    <p>Professional scaling and bulk preparation for commercial operations</p>
                </div>
                
                <div class="bulk-tools">
                    <div class="bulk-calculator">
                        <h3>Recipe Scaling Calculator</h3>
                        <div class="calculator-form">
                            <div class="form-group">
                                <label>Select Recipe:</label>
                                <select id="bulk-recipe-select">
                                    <option value="">Choose a recipe...</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <label>Target Portions:</label>
                                <input type="number" id="bulk-portions" min="1" max="500" value="25">
                            </div>
                            <button onclick="calculateBulkRecipe()">Calculate Bulk Recipe</button>
                        </div>
                        <div id="bulk-results" class="bulk-results"></div>
                    </div>
                </div>
            </section>

            <!-- Maintenance Section -->
            <section id="maintenance-section" class="section">
                <div class="section-header">
                    <h2>Maintenance Schedule</h2>
                    <p>Equipment maintenance and care schedules</p>
                </div>
                
                <div class="maintenance-timeline">
                    <div class="timeline-tabs">
                        <button class="tab-btn active" data-timeline="daily">📅 Daily</button>
                        <button class="tab-btn" data-timeline="weekly">📊 Weekly</button>
                        <button class="tab-btn" data-timeline="monthly">📋 Monthly</button>
                    </div>
                    
                    <div class="maintenance-content" id="maintenance-content">
                        <!-- Maintenance content will be dynamically loaded here -->
                    </div>
                </div>
            </section>

            <!-- Emergency Section -->
            <section id="emergency-section" class="section">
                <div class="section-header emergency-header">
                    <h2>🚨 Emergency Procedures</h2>
                    <p>Critical safety protocols and emergency response procedures</p>
                </div>
                
                <div class="emergency-grid">
                    <div class="emergency-card fire-emergency">
                        <div class="emergency-icon">🔥</div>
                        <h3>Fire Emergency</h3>
                        <p>Fire prevention and response procedures</p>
                        <button onclick="showEmergencyDetail('fire')">View Details</button>
                    </div>
                    
                    <div class="emergency-card electrical-emergency">
                        <div class="emergency-icon">⚡</div>
                        <h3>Electrical Emergency</h3>
                        <p>Electrical safety and power failure procedures</p>
                        <button onclick="showEmergencyDetail('electrical')">View Details</button>
                    </div>
                    
                    <div class="emergency-card medical-emergency">
                        <div class="emergency-icon">🏥</div>
                        <h3>Medical Emergency</h3>
                        <p>First aid and injury response procedures</p>
                        <button onclick="showEmergencyDetail('medical')">View Details</button>
                    </div>
                    
                    <div class="emergency-card equipment-emergency">
                        <div class="emergency-icon">🔧</div>
                        <h3>Equipment Failure</h3>
                        <p>Equipment malfunction and breakdown procedures</p>
                        <button onclick="showEmergencyDetail('equipment')">View Details</button>
                    </div>
                </div>

                <div class="emergency-contacts">
                    <h3>Emergency Contact Numbers</h3>
                    <div class="contact-grid">
                        <div class="contact-item">
                            <span class="contact-icon">🚑</span>
                            <span class="contact-label">Medical Emergency</span>
                            <span class="contact-number">108</span>
                        </div>
                        <div class="contact-item">
                            <span class="contact-icon">🚒</span>
                            <span class="contact-label">Fire Emergency</span>
                            <span class="contact-number">101</span>
                        </div>
                        <div class="contact-item">
                            <span class="contact-icon">👮</span>
                            <span class="contact-label">Police Emergency</span>
                            <span class="contact-number">100</span>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    </main>

    <!-- Floating Utility Panels -->
    
    <!-- Timer Panel -->
    <div id="timer-panel" class="utility-modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3>Kitchen Timers</h3>
                <button class="close-modal" onclick="closeUtilityModal('timer-panel')">×</button>
            </div>
            <div class="modal-body">
                <div class="timer-controls">
                    <div class="time-input">
                        <input type="number" id="timer-minutes" min="0" max="60" value="5" placeholder="Minutes">
                        <input type="number" id="timer-seconds" min="0" max="59" value="0" placeholder="Seconds">
                    </div>
                    <button onclick="addTimer()">Add Timer</button>
                </div>
                <div id="active-timers" class="active-timers">
                    <!-- Active timers will appear here -->
                </div>
            </div>
        </div>
    </div>

    <!-- Search Panel -->
    <div id="search-panel" class="utility-modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3>Recipe Search</h3>
                <button class="close-modal" onclick="closeUtilityModal('search-panel')">×</button>
            </div>
            <div class="modal-body">
                <div class="search-controls">
                    <input type="text" id="recipe-search" placeholder="Search recipes, ingredients, or equipment...">
                    <div class="search-filters">
                        <label><input type="checkbox" value="pizza"> Pizza</label>
                        <label><input type="checkbox" value="burger"> Burger</label>
                        <label><input type="checkbox" value="sandwich"> Sandwich</label>
                    </div>
                </div>
                <div id="search-results" class="search-results">
                    <!-- Search results will appear here -->
                </div>
            </div>
        </div>
    </div>

    <!-- Converter Panel -->
    <div id="converter-panel" class="utility-modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3>Unit Converter</h3>
                <button class="close-modal" onclick="closeUtilityModal('converter-panel')">×</button>
            </div>
            <div class="modal-body">
                <div class="converter-tabs">
                    <button class="tab-btn active" data-converter="weight">⚖️ Weight</button>
                    <button class="tab-btn" data-converter="volume">🥤 Volume</button>
                    <button class="tab-btn" data-converter="temperature">🌡️ Temperature</button>
                </div>
                <div class="converter-content" id="converter-content">
                    <!-- Converter content will be loaded here -->
                </div>
            </div>
        </div>
    </div>

    <!-- Calculator Panel -->
    <div id="calculator-panel" class="utility-modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3>Cost Calculator</h3>
                <button class="close-modal" onclick="closeUtilityModal('calculator-panel')">×</button>
            </div>
            <div class="modal-body">
                <div class="cost-calculator">
                    <div class="calc-input">
                        <label>Recipe:</label>
                        <select id="cost-recipe-select">
                            <option value="">Choose a recipe...</option>
                        </select>
                    </div>
                    <div class="calc-input">
                        <label>Portions:</label>
                        <input type="number" id="cost-portions" min="1" value="1">
                    </div>
                    <button onclick="calculateCost()">Calculate Cost</button>
                    <div id="cost-results" class="cost-results">
                        <!-- Cost calculation results will appear here -->
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Recipe Detail Modal -->
    <div id="recipe-modal" class="recipe-modal">
        <div class="modal-content large">
            <div class="modal-header">
                <h3 id="recipe-title"></h3>
                <button class="close-modal" onclick="closeRecipeModal()">×</button>
            </div>
            <div class="modal-body" id="recipe-detail-content">
                <!-- Recipe details will be loaded here -->
            </div>
        </div>
    </div>

    <!-- Equipment Detail Modal -->
    <div id="equipment-modal" class="equipment-modal">
        <div class="modal-content large">
            <div class="modal-header">
                <h3 id="equipment-title"></h3>
                <button class="close-modal" onclick="closeEquipmentModal()">×</button>
            </div>
            <div class="modal-body" id="equipment-detail-content">
                <!-- Equipment details will be loaded here -->
            </div>
        </div>
    </div>

    <!-- Emergency Detail Modal -->
    <div id="emergency-modal" class="emergency-modal">
        <div class="modal-content large">
            <div class="modal-header emergency-header">
                <h3 id="emergency-title"></h3>
                <button class="close-modal" onclick="closeEmergencyModal()">×</button>
            </div>
            <div class="modal-body" id="emergency-detail-content">
                <!-- Emergency details will be loaded here -->
            </div>
        </div>
    </div>

    <!-- Back to Top Button -->
    <button id="back-to-top" class="back-to-top" onclick="scrollToTop()">↑</button>

    <!-- Mini Timer Display -->
    <div id="mini-timer" class="mini-timer">
        <span id="mini-timer-display">00:00</span>
        <button onclick="toggleMiniTimer()">⏸️</button>
    </div>

    <!-- JavaScript Files -->
    <script src="app.js"></script>
    <script src="recipes.js"></script>
    <script src="equipment.js"></script>
    <script src="safety.js"></script>
    <script src="maintenance.js"></script>
    <script src="emergency.js"></script>
    <script src="utilities.js"></script>
    <script>
        // Register Service Worker for offline functionality
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', function() {
                navigator.serviceWorker.register('sw.js')
                    .then(function(registration) {
                        console.log('ServiceWorker registration successful');
                    })
                    .catch(function(err) {
                        console.log('ServiceWorker registration failed: ', err);
                    });
            });
        }
    </script>
</body>
</html>'''

# Save the main HTML file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Created index.html - Main application file")
print("File size:", len(html_content), "characters")