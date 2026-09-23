flower-shop/
├── public/                 # Static assets (brand logos, placeholder images)
├── src/
│   ├── assets/             # Global styles, custom fonts, icons
│   ├── components/         # Shared/reusable UI blocks
│   │   ├── ui/             # Buttons, Inputs, Modals, Badges
│   │   └── layout/         # Header, Mobile Nav, Footer
│   ├── features/           # Domain-specific logic
│   │   ├── catalog/        # Product listings, flower filters, search
│   │   ├── cart/           # Shopping cart state & drawer components
│   │   ├── checkout/       # Address validation, payment forms
│   │   └── orders/         # Order tracking & customer history
│   ├── lib/                # Database clients, API helpers, Stripe config
│   ├── types/              # TypeScript interfaces (Product, Order, User)
│   └── app/                # Route pages (Home, Product Detail, Cart, Checkout)
├── .env.example            # Environment variables template
├── package.json
└── README.md