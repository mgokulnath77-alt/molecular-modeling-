/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        'bio-dark': '#0f172a',
        'bio-purple': '#581c87',
        'bio-blue': '#1e40af',
        'bio-accent': '#06b6d4',
      },
      fontFamily: {
        poppins: ['Poppins', 'sans-serif'],
      },
      backdropBlur: {
        xs: '2px',
      }
    },
  },
  plugins: [],
};