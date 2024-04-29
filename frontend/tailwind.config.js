/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      height: {
        "chatheight": "calc(100vh - 9rem)",
      },
    },
  },
  plugins: [],
};
