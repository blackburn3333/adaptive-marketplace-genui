-- =============================================================================
-- Migration: 001_create_foods_table.sql
-- Description: Creates the core foods catalog table with structured JSON
--              support for dietary tags and nutritional macros.
-- =============================================================================

CREATE TABLE IF NOT EXISTS foods (
    -- Unique primary key identifier
    id INT AUTO_INCREMENT PRIMARY KEY,

    -- Display name of the food product
    name VARCHAR(255) NOT NULL,

    -- Price per unit in Sri Lankan Rupees (LKR)
    price_per_unit DECIMAL(10, 2) NOT NULL,

    -- Unit of measure (e.g., 'pack', 'kg', 'bottle')
    unit VARCHAR(50) NOT NULL,

    -- Detailed item description
    description TEXT,

    -- Categorical tags array for filtering (e.g., ["vegan", "organic", "spicy"])
    tags JSON NOT NULL,

    -- Image URL for frontend card rendering
    image_url VARCHAR(500),

    -- Macro breakdown per serving (e.g., {"calories": 160, "protein": 7})
    nutrition_facts JSON NOT NULL,

    -- Creation timestamp
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);