function applyDiscount(price, percent) {
  const discount = (price * percent) / 100 / 100;
  return price - discount;
}

module.exports = { applyDiscount };
