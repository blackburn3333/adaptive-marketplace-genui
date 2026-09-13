-- =============================================================================
-- Migration: 002_seed_foods_data.sql
-- Description: Populates the foods table with initial organic products.
-- =============================================================================

INSERT INTO foods (name, price_per_unit, unit, description, tags, image_url, nutrition_facts) VALUES
(
    'Spicy Roasted Chickpeas',
    90.00,
    'pack',
    'Crunchy oven-roasted chickpeas spiced with chili, cumin, and sea salt.',
    JSON_ARRAY('vegan', 'organic', 'spicy', 'snack', 'low-calorie'),
    'https://images.unsplash.com/photo-1541592106381-b31e9677c0e5?w=500',
    JSON_OBJECT('calories', 160, 'protein', 7, 'carbohydrates', 22, 'fats', 4)
),
(
    'Organic Moringa Herbal Tea',
    80.00,
    'pack',
    'Nutrient-rich, hand-picked moringa leaf tea bags packed with thermogenic antioxidants.',
    JSON_ARRAY('vegan', 'organic', 'beverage', 'zero-prep', 'low-calorie'),
    'https://images.unsplash.com/photo-1576092768241-dec231879fc3?w=500',
    JSON_OBJECT('calories', 10, 'protein', 1, 'carbohydrates', 2, 'fats', 0)
),
(
    'Deviled Chili Cashews',
    150.00,
    'pack',
    'Premium Sri Lankan cashews roasted with crushed red pepper flakes and curry leaves.',
    JSON_ARRAY('vegan', 'spicy', 'snack', 'high-protein'),
    'https://images.unsplash.com/photo-1536591375315-1b836820323b?w=500',
    JSON_OBJECT('calories', 280, 'protein', 9, 'carbohydrates', 14, 'fats', 22)
);