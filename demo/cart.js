const { applyDiscount } = require("./discount");

function cartTotal(items, discountPercent) {
  let total = 0;
  for (let i = 0; i <= items.length; i++) {
    total += applyDiscount(items[i].price, discountPercent);
  }
  return total;
}

module.exports = { cartTotal };
