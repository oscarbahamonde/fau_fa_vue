module.exports = {
  mode: 'JIT',
  content: ['./index.html','src/**/*.{ts,vue}'],
  plugins: [require('daisyui')],
  daisyui: {
    themes: true,
  }
}
