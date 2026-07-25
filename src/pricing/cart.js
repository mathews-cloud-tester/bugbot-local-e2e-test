import { applyDiscount } from "./discount.js";

export function cartTotal(items, percent) {
  const subtotal = items.reduce((sum, item) => sum + item.price * item.qty, 0);
  return applyDiscount(subtotal, percent);
}

export function itemCount(items) {
  return items.reduce((sum, item) => sum + item.qty, 0);
}

export function isEmpty(items) {
  return itemCount(items) === 0;
}
