const RECIPES = [
  // --- PIZZA SECTION ---
  {
    name: "Margherita Pizza",
    category: "Pizza",
    size_options: ["7 inch", "10 inch"],
    ingredients_english: [
      "1 Pizza Base (7\" or 10\")",
      "100g Mozzarella Cheese (Grated)",
      "50g Tomato Sauce",
      "Fresh Basil Leaves",
      "2 tsp Olive Oil",
      "Salt to taste"
    ],
    ingredients_hinglish: [
      "1 Pizza Base (7\" ya 10\")",
      "100g Mozzarella Cheese (Grated)",
      "50g Tomato Sauce",
      "Fresh Basil ke Patte",
      "2 tsp Olive Oil",
      "Namak swad anusar"
    ],
    preparation_steps_hinglish: [
      "Oven ko 220°C par preheat kariye.",
      "Pizza base ko tawa ya oven mein rakhiye.",
      "Tomato sauce ko evenly spread kariye.",
      "Mozzarella cheese aur basil leaves daaliye.",
      "Thoda namak aur olive oil drizzle kariye.",
      "Oven mein 10-12 minute tak bake kariye jab tak cheese melt aur golden ho jaye.",
      "Garam garam serve kariye."
    ],
    chef_tips: "Use fresh basil; oven temperature constant rakhein for crispy crust.",
    equipment: ["Commercial Electric Pizza Oven", "Tawa"],
    temperature: "220°C, 10-12 minutes",
    cost_per_unit: 80,
    storage_reheating: "Store airtight, reheat at 200°C for 5 min"
  },
  {
    name: "Peppy Paneer Pizza",
    category: "Pizza",
    size_options: ["7 inch", "10 inch"],
    ingredients_english: [
      "Pizza Base",
      "100g Paneer (Cubes)",
      "Bell Peppers, Sliced",
      "100g Mozzarella Cheese",
      "Pizza Sauce",
      "Oregano",
      "Olive Oil",
      "Salt"
    ],
    ingredients_hinglish: [
      "Pizza Base",
      "100g Paneer Cubes",
      "Shimla Mirch, Sliced",
      "100g Mozzarella Cheese",
      "Pizza Sauce",
      "Oregano",
      "Olive Oil",
      "Namak"
    ],
    preparation_steps_hinglish: [
      "Paneer aur shimla mirch ko thoda marinate kar lo.",
      "Base par sauce lagao, paneer aur veggies spread karo.",
      "Cheese daalo, oregano daalo.",
      "Oven mein 220°C par 10-12 min bake karo.",
      "Serve garma garam."
    ],
    chef_tips: "Paneer ko dahi, namak, mirch powder se 10 min marinate karo for mazedaar flavour.",
    equipment: ["Pizza Oven", "Tawa"],
    temperature: "220°C, 12 min",
    cost_per_unit: 100,
    storage_reheating: "200°C oven, 4 min"
  },
  // --- REPEAT FOR ALL PIZZA VARIANTS ---

  // --- BURGER SECTION ---
  {
    name: "Classic Aloo Tikki Burger",
    category: "Burger",
    ingredients_english: [
      "2 boiled potatoes",
      "1 cup bread crumbs",
      "Chopped coriander",
      "Chopped green chili",
      "Garam Masala",
      "Salt",
      "Burger Buns",
      "Onion Slices",
      "Tomato Slices",
      "Lettuce",
      "Green Chutney",
      "Ketchup"
    ],
    ingredients_hinglish: [
      "2 ubaale aloo",
      "1 cup bread crumb",
      "Hara dhania",
      "Hari mirch",
      "Garam masala",
      "Namak",
      "Burger Bun",
      "Pyaaz ki slice",
      "Tamatar ki slice",
      "Lettuce",
      "Chutney",
      "Ketchup"
    ],
    preparation_steps_hinglish: [
      "Aloo ko mash karo, sab masale aur bread crumb daalo.",
      "Tikki bana kar tawa/fryer par crisp karo.",
      "Bun toast karo, onion, lettuce, tikki lagao.",
      "Chutney, ketchup lagao, close karo.",
      "Serve karo."
    ],
    chef_tips: "Tikki ko corn flour mein roll kar fry karo for crispy texture.",
    equipment: ["Tawa", "Electric Fryer"],
    temperature: "Tawa - medium heat, Fryer - 180°C",
    cost_per_unit: 40,
    storage_reheating: "Fridge mein tikki, tawa/fryer mein reheat"
  },
  // --- REPEAT FOR ALL BURGER VARIANTS ---

  // --- SANDWICH SECTION ---
  {
    name: "Bombay Grill Sandwich",
    category: "Sandwich",
    ingredients_english: [
      "4 Bread Slices",
      "Butter",
      "Boiled Potato Slices",
      "Beetroot Slices",
      "Cucumber Slices",
      "Tomato Slices",
      "Onion Slices",
      "Green Chutney",
      "Chaat Masala",
      "Salt"
    ],
    ingredients_hinglish: [
      "4 bread ke slices",
      "Makkhan",
      "Ubaala aalu, beetroot, kheera, tamatar, pyaaz slices",
      "Hari chutney",
      "Chaat masala",
      "Namak"
    ],
    preparation_steps_hinglish: [
      "Bread par butter aur chutney lagao.",
      "Sab sabziyon ki layer lagao, masala daalo.",
      "Second bread slice se cover karo.",
      "Electric grill/tawa par golden hone tak sekho.",
      "Cut karo, serve karo."
    ],
    chef_tips: "Chutney zyada thick ho to sandwich soggy nahi banega.",
    equipment: ["Electric Sandwich Maker"],
    temperature: "Medium heat, 3-4 min",
    cost_per_unit: 30,
    storage_reheating: "Airtight rakho, grill par dubara sekh lo"
  },
  // --- REPEAT FOR ALL SANDWICH VARIANTS ---
];

