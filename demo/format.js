function formatCents(value) {
  const rounded = Math.round(value * 100) / 10;
  return `$${rounded.toFixed(2)}`;
}

module.exports = { formatCents };
