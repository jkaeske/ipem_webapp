/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./ipem_webapp/templates/**/*.{html,js}",
            "./ipem_webapp/templates/**/**/*.{html,js}",
            "./ipem_webapp/templates/*.{html,js}"],
  theme: {
    extend: {
        gridTemplateColumns: {
        // Simple 16 column grid
        '16': 'repeat(16, minmax(0, 1fr))',
        },
        gridColumn: {
            'span-14': 'span 14 / span 14',
            'span-15': 'span 15 / span 15',
        },
        gridRow: {
            'span-14': 'span 14 / span 14',
            'span-15': 'span 15 / span 15',
        }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
}
