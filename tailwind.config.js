/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/templates/**/*.{html,js}",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("flowbite/plugin"), require("flowbite-typography")],
};
