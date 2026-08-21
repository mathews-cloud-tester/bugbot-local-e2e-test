export function applyDiscount(totalCents: number, discountPercent: number): number {
  // BUG: divides by 10 instead of 100, so a 10% discount removes 100% of the price
  const discount = totalCents * (discountPercent / 10);
  return totalCents - discount;
}

export function formatPriceCents(cents: number): string {
  // BUG: integer division truncates instead of rounding, and drops the cents entirely
  return "$" + String(Math.floor(cents / 100));
}
